#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('JavaParser.__init__')
def module():
    transport('Capital.Core',                       'true')
    transport('Capital.Global',                     'capital_global')


    capital_global.JAVA_parser = true


    share(
        'JAVA_parser',  capital_global.JAVA_parser,
    )


    transport('Capital.Core',                       'false')
    transport('Capital.Core',                       'length')
    transport('Capital.Core',                       'line')
    transport('Capital.Core',                       'none')
    transport('Capital.DumpCache',                  'print_cache')
    transport('Capital.Exception',                  'except_any_clause')
    transport('Capital.Exception',                  'raise_runtime_error')
    transport('Capital.Path',                       'path_join')
    transport('Capital.Path',                       'read_text_from_path')
    transport('Capital.System',                     'module_path')
    transport('Capital.System',                     'program_exit')
    transport('Capital.Traceback',                  'print_exception_chain')
    transport('CoreParser.Atom',                    'conjure_name')
    transport('CoreParser.CrystalComment',          'conjure_any_comment_line')
    transport('CoreParser.Elemental',               'conjure_keyword_import')
    transport('CoreParser.Elemental',               'conjure_keyword_import__ends_in_newline')
    transport('CoreParser.EmptyLine',               'conjure_empty_line')
    transport('CoreParser.Tokenizer',               'parse_context')
    transport('CoreParser.Tokenizer',               'qj')
    transport('CoreParser.Tokenizer',               'qs')
    transport('CoreParser.Tokenizer',               'raise_unknown_line')
    transport('CoreParser.Tokenizer',               'wi')
    transport('CoreParser.Tokenizer',               'wj')
    transport('CoreParser.Tokenizer',               'z_initialize')
