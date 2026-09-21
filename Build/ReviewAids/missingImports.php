#!/usr/bin/env php
<?php

declare(strict_types=1);

/*
 * This file is part of the TYPO3 CMS project.
 *
 * It is free software; you can redistribute it and/or modify it under
 * the terms of the GNU General Public License, either version 2
 * of the License, or any later version.
 *
 * For the full copyright and license information, please read the
 * LICENSE.txt file that was distributed with this source code.
 *
 * The TYPO3 project - inspiring people to share!
 */

/*
 * Report class names a PHP snippet uses without importing them.
 *
 * A snippet is copied into a real extension, so a name it uses has to arrive
 * there as well. A missing `use` statement is invisible in the rendered
 * manual: the example reads correctly and only fails once somebody runs it.
 *
 * Usage, from the repository whose snippets are under review:
 *
 *   ../guide-h2d/Build/ReviewAids/missingImports.php [<path>...]
 *
 * <path> defaults to Documentation and may be a directory or single files.
 * The script parses with nikic/php-parser from the Composer installation of
 * that repository, so `make install` has to have run there.
 *
 * What it cannot see — the reason this is a review aid and not a test
 * (see README.md):
 *
 * - Doc comments. A `@param`, `@return` or generic type such as
 *   `QueryResultInterface<Conference>` names a class the same way code does,
 *   but the parser reads it as text. A name that only ever appears in a doc
 *   comment is missed.
 * - Siblings. A name that resolves into the file's own namespace needs no
 *   import when the class really lives there, and that is the common case in
 *   the example namespace `MyVendor\MyExtension`. Every finding therefore has
 *   to be read as "is this class meant to live in this namespace?", which the
 *   script cannot answer. Expect most findings to be legitimate.
 */

use PhpParser\Node;
use PhpParser\NodeFinder;
use PhpParser\NodeTraverser;
use PhpParser\NodeVisitor\NameResolver;
use PhpParser\NodeVisitor\ParentConnectingVisitor;
use PhpParser\ParserFactory;

if (PHP_SAPI !== 'cli') {
    die('Script must be called from command line.' . chr(10));
}

$paths = array_slice($argv, 1) ?: ['Documentation'];

$files = [];
foreach ($paths as $path) {
    if (is_file($path)) {
        $files[] = $path;
        continue;
    }
    if (!is_dir($path)) {
        fwrite(STDERR, sprintf('Not found: %s%s', $path, PHP_EOL));
        exit(1);
    }
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($path));
    foreach ($iterator as $file) {
        if (!$file->isFile() || $file->getExtension() !== 'php') {
            continue;
        }
        // A generator writes these, and it writes excerpts without a
        // namespace, where an unimported name is the normal case.
        if (str_contains(strtr($file->getPathname(), '\\', '/'), '/CodeSnippets/')) {
            continue;
        }
        $files[] = $file->getPathname();
    }
}
sort($files);

if ($files === []) {
    echo 'No PHP file found.' . PHP_EOL;
    exit(0);
}

/*
 * The parser comes from the reviewed repository, not from this one, and is
 * loaded directly rather than through that repository's Composer autoloader:
 * a manual pins the TYPO3 version of its branch, so its autoloader can carry
 * a platform check for a PHP version newer than the one running this script.
 */
$parserLibrary = getenv('REVIEW_AIDS_PHP_PARSER') ?: null;
$roots = [realpath(dirname($files[0])), getcwd()];
// A linked worktree has no .Build of its own, the main checkout holds it.
$commonDirectory = exec(sprintf(
    'git -C %s rev-parse --path-format=absolute --git-common-dir 2>/dev/null',
    escapeshellarg((string)($roots[0] ?: '.'))
));
if ($commonDirectory !== '') {
    $roots[] = dirname($commonDirectory);
}
foreach (array_filter($roots) as $directory) {
    while ($parserLibrary === null && $directory !== false && $directory !== dirname($directory)) {
        foreach (['/.Build/vendor', '/vendor'] as $vendor) {
            $candidate = $directory . $vendor . '/nikic/php-parser/lib';
            if (is_dir($candidate)) {
                $parserLibrary = $candidate;
                break 2;
            }
        }
        $directory = dirname($directory);
    }
}
if ($parserLibrary === null || !is_dir($parserLibrary)) {
    fwrite(STDERR, 'nikic/php-parser not found, run "make install"'
        . ' in the reviewed repository.' . PHP_EOL);
    exit(1);
}

spl_autoload_register(static function (string $class) use ($parserLibrary): void {
    if (str_starts_with($class, 'PhpParser\\')) {
        $file = $parserLibrary . '/' . str_replace('\\', '/', $class) . '.php';
        if (is_file($file)) {
            require $file;
        }
    }
});

// Names that never come from an import.
const BUILT_IN_NAMES = [
    'self', 'static', 'parent', 'array', 'callable', 'int', 'float', 'bool',
    'string', 'iterable', 'object', 'mixed', 'void', 'null', 'never', 'false',
    'true',
];

$parser = (new ParserFactory())->createForNewestSupportedVersion();
$nodeFinder = new NodeFinder();
$found = 0;

foreach ($files as $file) {
    try {
        $statements = $parser->parse((string)file_get_contents($file));
    } catch (Throwable $exception) {
        printf('%s: cannot be parsed: %s%s', $file, $exception->getMessage(), PHP_EOL);
        $found++;
        continue;
    }
    if ($statements === null) {
        continue;
    }

    $traverser = new NodeTraverser();
    $traverser->addVisitor(new ParentConnectingVisitor());
    $traverser->addVisitor(new NameResolver(null, [
        'preserveOriginalNames' => true,
    ]));
    $statements = $traverser->traverse($statements);

    $namespace = $nodeFinder
        ->findFirstInstanceOf($statements, Node\Stmt\Namespace_::class)
        ?->name?->toString();

    $declared = [];
    $isNamedClass = static fn($node): bool => $node instanceof Node\Stmt\ClassLike
        && $node->name !== null;
    foreach ($nodeFinder->find($statements, $isNamedClass) as $class) {
        $declared[] = strtolower((string)$class->namespacedName);
    }

    $reported = [];
    foreach ($nodeFinder->findInstanceOf($statements, Node\Name::class) as $name) {
        $parent = $name->getAttribute('parent');
        if ($parent instanceof Node\Expr\FuncCall
            || $parent instanceof Node\Expr\ConstFetch
            || $parent instanceof Node\Stmt\Namespace_
            || $parent instanceof Node\Stmt\Use_
            || $parent instanceof Node\Stmt\GroupUse
            || $parent instanceof Node\UseItem
        ) {
            continue;
        }

        $original = $name->getAttribute('originalName') ?? $name;
        if ($original->isFullyQualified() || $original->isQualified()) {
            // Written out, or reached through an imported namespace.
            continue;
        }
        if (in_array(strtolower($original->toString()), BUILT_IN_NAMES, true)) {
            continue;
        }

        $resolved = $name->toString();
        if (in_array(strtolower($resolved), $declared, true)) {
            continue;
        }
        // An imported name resolves to something else than namespace + name.
        $asSibling = ($namespace !== null ? $namespace . '\\' : '') . $original->toString();
        if (strcasecmp($resolved, $asSibling) !== 0) {
            continue;
        }
        if ($namespace === null
            && (class_exists($resolved) || interface_exists($resolved)
                || enum_exists($resolved) || trait_exists($resolved))
        ) {
            // A global file using a class of PHP itself.
            continue;
        }

        $key = $original->toString();
        if (isset($reported[$key])) {
            continue;
        }
        $reported[$key] = true;

        printf(
            '%s:%d  %s  (would resolve to %s)%s',
            $file,
            $name->getStartLine(),
            $key,
            $resolved,
            PHP_EOL
        );
        $found++;
    }
}

printf(
    '%s%d name(s) in %d file(s) are used without an import. Most of them are%s'
    . 'siblings in the same namespace and perfectly fine — see the header.%s',
    PHP_EOL,
    $found,
    count($files),
    PHP_EOL,
    PHP_EOL
);
