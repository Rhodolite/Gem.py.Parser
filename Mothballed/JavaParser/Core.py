#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('JavaParser.Core')
def gem():
    require_gem('CoreParser.Elemental')
    require_gem('CoreParser.Tokenizer')
    require_gem('Gem.DumpCache')
    require_gem('Gem.Traceback')


    from CoreParser import conjure_keyword_import, conjure_keyword_import__ends_in_newline, conjure_name
    from CoreParser import la, parse_context, qd, qi, qj, qk, ql, qn, qs, raise_unknown_line
    from CoreParser import wd, wd0, wd1, wi, wj, wk, wn, ws, z_initialize
    from Gem import create_cache
    from Gem import module_path, path_join, print_cache, print_exception_chain
    from Gem import program_exit, read_text_from_path, StringOutput


    share(
        #
        #   Imported types
        #
        'StringOutput',     StringOutput,

        
        #
        #   Imported functions (CoreParser)
        #
        'conjure_keyword_import',                   conjure_keyword_import,
        'conjure_keyword_import__ends_in_newline',  conjure_keyword_import__ends_in_newline,
        'conjure_name',                             conjure_name,
        'la',                                       la,
        'qd',                                       qd,
        'qi',                                       qi,
        'qj',                                       qj,
        'qk',                                       qk,
        'ql',                                       ql,
        'qn',                                       qn,
        'qs',                                       qs,
        'raise_unknown_line',                       raise_unknown_line,
        'wd0',                                      wd0,
        'wd1',                                      wd1,
        'wd',                                       wd,
        'wi',                                       wi,
        'wj',                                       wj,
        'wk',                                       wk,
        'wn',                                       wn,
        'ws',                                       ws,
        'z_initialize',                             z_initialize,


        #
        #   Imported functions (Gem)
        #
        'create_cache',             create_cache,
        'path_join',                path_join,
        'print_cache',              print_cache,
        'print_exception_chain',    print_exception_chain,
        'program_exit',             program_exit,
        'read_text_from_path',      read_text_from_path,


        #
        #   Values (CoreParser)
        #
        'parse_context',                            parse_context,


        #
        #   Values (Gem)
        #
        'module_path',          module_path,
    )
