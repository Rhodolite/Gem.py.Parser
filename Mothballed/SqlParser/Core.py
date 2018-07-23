#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('SqlParser.Core')
def gem():
    require_gem('Gem.Cache')
    require_gem('CoreParser.Atom')
    require_gem('CoreParser.EmptyLine')
    require_gem('CoreParser.Tokenizer')
    require_gem('Gem.Cache')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Global')
    require_gem('Gem.Path')
    require_gem('Gem.StringOutput')


    from CoreParser import ParserToken, conjure_empty_line, lookup_name
    from CoreParser import qj, qk, qs, raise_unknown_line, wj, wk, z_initialize
    from Gem import create_DelayedFileOutput, create_StringOutput, gem_global, module_path, path_join
    from Gem import read_text_from_path, produce_conjure_by_name


    share(
        #
        #   Types (CoreParser)
        #
        'ParserToken',  ParserToken,

        
        #
        #   Functions (CoreParser)
        #
        'conjure_empty_line',   conjure_empty_line,
        'lookup_name',          lookup_name,
        'qj',                   qj,
        'qk',                   qk,
        'qs',                   qs,
        'raise_unknown_line',   raise_unknown_line,
        'read_text_from_path',  read_text_from_path,
        'wj',                   wj,
        'wk',                   wk,
        'z_initialize',         z_initialize,


        #
        #   Functions (Gem)
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_StringOutput',          create_StringOutput,
        'path_join',                    path_join,
        'produce_conjure_by_name',      produce_conjure_by_name,


        #
        #   Values (Gem)
        #
        'gem_global',   gem_global,
        'module_path',  module_path,
    )
