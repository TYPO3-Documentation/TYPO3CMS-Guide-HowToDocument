<?php

// https://github.com/TYPO3-Documentation/t3docs-codesnippets
// ddev exec vendor/bin/typo3  restructured_api_tools:php_domain public/fileadmin/TYPO3CMS-Guide-HowToDocument/Documentation/CodeSnippets/

return [
    [
        'action'=> 'createCodeSnippet',
        'caption' => 'Documentation/Index.rst of the Getting Started tutorial',
        'sourceFile'=> 'fileadmin/TYPO3CMS-Tutorial-GettingStarted/Documentation/Index.rst',
        'targetFileName' => 'FileStructure/GettingStarted/IndexRst.rst.txt',
        'language' => 'rst',
    ],
    [
        'action'=> 'createCodeSnippet',
        'caption' => 'Documentation/Index.rst of the Dashboard manual',
        'sourceFile'=> 'typo3/sysext/dashboard/Documentation/Index.rst',
        'targetFileName' => 'FileStructure/Dashboard/IndexRst.rst.txt',
        'language' => 'rst',
    ],
    [
        'action'=> 'createCodeSnippet',
        'caption' => 'Documentation/Index.rst of the Examples extension manual',
        'sourceFile'=> 'typo3conf/ext/examples/Documentation/Index.rst',
        'targetFileName' => 'FileStructure/Examples/IndexRst.rst.txt',
        'language' => 'rst',
    ],
    [
        'action'=> 'createCodeSnippet',
        'caption' => 'README.rst of the Getting Started tutorial',
        'sourceFile'=> 'fileadmin/TYPO3CMS-Tutorial-GettingStarted/README.rst',
        'targetFileName' => 'FileStructure/GettingStarted/ReadmeRst.rst.txt',
        'language' => 'rst',
    ],
    [
        'action'=> 'createCodeSnippet',
        'caption' => 'README.rst of the Dashboard manual',
        'sourceFile'=> 'typo3/sysext/dashboard/README.rst',
        'targetFileName' => 'FileStructure/Dashboard/ReadmeRst.rst.txt',
        'language' => 'rst',
    ],
    [
        'action'=> 'createCodeSnippet',
        'caption' => 'README.rst of the Examples extension manual',
        'sourceFile'=> 'typo3conf/ext/examples/README.rst',
        'targetFileName' => 'FileStructure/Examples/ReadmeRst.rst.txt',
        'language' => 'rst',
    ],
    [
        'action'=> 'createCodeSnippet',
        'caption' => 'Documentation/Settings.cfg of the Getting Started tutorial',
        'sourceFile'=> 'fileadmin/TYPO3CMS-Tutorial-GettingStarted/Documentation/Settings.cfg',
        'targetFileName' => 'FileStructure/GettingStarted/SettingsCfg.rst.txt',
        'language' => 'none',
    ],
    [
        'action'=> 'createCodeSnippet',
        'caption' => 'Documentation/Settings.cfg of the Dashboard manual',
        'sourceFile'=> 'typo3/sysext/dashboard/Documentation/Settings.cfg',
        'targetFileName' => 'FileStructure/Dashboard/SettingsCfg.rst.txt',
        'language' => 'none',
    ],
    [
        'action'=> 'createCodeSnippet',
        'caption' => 'Documentation/Settings.cfg of the Examples extension manual',
        'sourceFile'=> 'typo3conf/ext/examples/Documentation/Settings.cfg',
        'targetFileName' => 'FileStructure/Examples/SettingsCfg.rst.txt',
        'language' => 'none',
    ],
];