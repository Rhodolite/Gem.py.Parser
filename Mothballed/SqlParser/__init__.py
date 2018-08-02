#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('SqlParser')
def module():
    transport('Capital.Core',                       'true')
    transport('Capital.Global',                     'capital_global')


    capital_global.SQL_parser = true


    share(
        'SQL_parser',   capital_global.SQL_parser,
        'TESTING',      capital_global.TESTING,
    )


    transport('Capital.Cache',                      'produce_conjure_by_name')
    transport('Capital.Core',                       'arrange')
    transport('Capital.Core',                       'line')
    transport('Capital.Core',                       'none')
    transport('Capital.Core',                       'Object')
    transport('Capital.DelayedFileOutput',          'create_DelayedFileOutput')
    transport('Capital.Exception',                  'raise_runtime_error')
    transport('Capital.Global',                     'capital_global')
    transport('Capital.Path',                       'path_join')
    transport('Capital.Path',                       'read_text_from_path')
    transport('Capital.PortrayString',              'portray_raw_string')
    transport('Capital.StringOutput',               'create_StringOutput')
    transport('Capital.System',                     'module_path')
    transport('CoreParser.Atom',                    'lookup_name')
    transport('CoreParser.EmptyLine',               'conjure_empty_line')
    transport('CoreParser.ParserToken',             'ParserToken')
    transport('CoreParser.Tokenizer',               'parse_context')
    transport('CoreParser.Tokenizer',               'raise_unknown_line')
    transport('CoreParser.Tokenizer',               'z_initialize')
