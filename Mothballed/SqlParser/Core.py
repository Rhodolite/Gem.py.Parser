#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('SqlParser.Core')
def module():
    require_module('Capital.Cache')
    require_module('Capital.Cache')
    require_module('Capital.DelayedFileOutput')
    require_module('Capital.Exception')
    require_module('Capital.Global')
    require_module('Capital.Path')
    require_module('Capital.StringOutput')
    require_module('CoreParser.Atom')
    require_module('CoreParser.EmptyLine')
    require_module('CoreParser.Tokenizer')


    from Capital import capital_global, create_DelayedFileOutput, create_StringOutput, module_path, path_join
    from Capital import read_text_from_path, produce_conjure_by_name
    from CoreParser import ParserToken, conjure_empty_line, lookup_name
    from CoreParser import qj, qk, qs, raise_unknown_line, wj, wk, z_initialize


    share(
        #
        #   Types (CoreParser)
        #
        'ParserToken',  ParserToken,

        
        #
        #   Functions (Capital)
        #
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_StringOutput',          create_StringOutput,
        'path_join',                    path_join,
        'produce_conjure_by_name',      produce_conjure_by_name,


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
        #   Values (Capital)
        #
        'capital_global',   capital_global,
        'module_path',      module_path,
    )
