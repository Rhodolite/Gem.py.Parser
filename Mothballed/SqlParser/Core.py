#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('SqlParser.Core')
def module():
    transport('Capital.Cache',                      'produce_conjure_by_name')
    transport('Capital.DelayedFileOutput',          'create_DelayedFileOutput')
    transport('Capital.Global',                     'capital_global')
    transport('Capital.Path',                       'path_join')
    transport('Capital.Path',                       'read_text_from_path')
    transport('Capital.StringOutput',               'create_StringOutput')
    transport('Capital.System',                     'module_path')
    transport('CoreParser.Atom',                    'lookup_name')
    transport('CoreParser.EmptyLine',               'conjure_empty_line')
    transport('CoreParser.ParserToken',             'ParserToken')
    transport('CoreParser.Tokenizer',               'parse_context')
    transport('CoreParser.Tokenizer',               'raise_unknown_line')
    transport('CoreParser.Tokenizer',               'z_initialize')
