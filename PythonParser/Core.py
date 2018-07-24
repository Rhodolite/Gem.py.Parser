#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.Core')
def gem():
    require_gem('CoreParser.ActionWord')
    require_gem('CoreParser.Atom')
    require_gem('CoreParser.ClassOrder')
    require_gem('CoreParser.CreateMeta')
    require_gem('CoreParser.Elemental')
    require_gem('CoreParser.Method')
    require_gem('CoreParser.Nub')
    require_gem('CoreParser.Tokenizer')
    require_gem('Gem.Cache')
    require_gem('Gem.Cache2')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.DumpCache')
    require_gem('Gem.Exception')
    require_gem('Gem.GeneratedConjureQuadruple')
    require_gem('Gem.Herd')
    require_gem('Gem.Method')
    require_gem('Gem.Path')
    require_gem('Gem.PortrayString')                                    #   For builtin `portray_string`
    require_gem('Gem.StringOutput')
    require_gem('Gem.System')
    require_gem('Gem.Traceback')


    from CoreParser import CLASS_ORDER__NORMAL_TOKEN, CLASS_ORDER__PYTHON_END, CLASS_ORDER__PYTHON_START
    from CoreParser import conjure_action_word, conjure_action_word__ends_in_newline, conjure_keyword_import
    from CoreParser import conjure_name, conjure_nub, conjure_ActionWord_WithNewlines, CoreParserToken
    from CoreParser import Identifier, initialize_action_word__Meta, is_name__0, KeywordAndOperatorBase
    from CoreParser import KeywordImport, la, lookup_adjusted_meta, lookup_normal_token, mutate__self, order__s
    from CoreParser import parse_context, produce_conjure_action_word, produce_conjure_atom
    from CoreParser import provide_normal_token
    from CoreParser import qd, qi, qj, qk, ql, qn, qs, static_conjure_nub, store_adjusted_meta
    from CoreParser import raise_unknown_line, transform__self, wd, wd0, wd1, wi, wj, wk, wn, ws, z_initialize
    from Gem import create_cache, create_DelayedFileOutput, create_SimpleStringOutput, create_StringOutput
    from Gem import empty_herd, module_path, path_join, path_normalize, print_cache, print_exception_chain
    from Gem import produce_conjure_dual, produce_conjure_dual__21
    from Gem import produce_conjure_quadruple__4123
    from Gem import produce_conjure_single, produce_conjure_triple
    from Gem import produce_conjure_triple__312, produce_conjure_tuple
    from Gem import produce_conjure_unique_dual, produce_conjure_unique_dual__21
    from Gem import produce_conjure_unique_triple, produce_conjure_unique_triple__312
    from Gem import program_exit, read_text_from_path, return_self, slice_all, StringOutput


    path_0 = module_path[0]

    if path_0.endswith('/Gems'):
        root_path   = path_0
        source_path = path_join(root_path, 'py')
    else:
        source_path = path_normalize(path_join(path_0,      '..'))
        root_path   = path_normalize(path_join(source_path, '..'))

    binary_path = path_join(root_path, 'bin')

    if false:
        line('root_path: %s', root_path)
        line('binary_path: %s', binary_path)
        line('source_path: %s', source_path)


    share(
        #
        #   Imported types (CoreParser)
        #
        'CoreParserToken',          CoreParserToken,
        'Identifier',               Identifier,
        'KeywordAndOperatorBase',   KeywordAndOperatorBase,
        'KeywordImport',            KeywordImport,

        
        #
        #   Imported types (Gem)
        #
        'StringOutput',     StringOutput,


        #
        #   Imported functions (CoreParser)
        #
        'conjure_action_word',                      conjure_action_word,
        'conjure_action_word__ends_in_newline',     conjure_action_word__ends_in_newline,
        'conjure_ActionWord_WithNewlines',          conjure_ActionWord_WithNewlines,
        'conjure_keyword_import',                   conjure_keyword_import,
        'conjure_name',                             conjure_name,
        'conjure_nub',                              conjure_nub,
        'initialize_action_word__Meta',             initialize_action_word__Meta,
        'is_name__0',                               is_name__0,
        'la',                                       la,
        'lookup_adjusted_meta',                     lookup_adjusted_meta,
        'lookup_normal_token',                      lookup_normal_token,
        'mutate__self',                             mutate__self,
        'order__s',                                 order__s,
        'produce_conjure_action_word',              produce_conjure_action_word,
        'produce_conjure_atom',                     produce_conjure_atom,
        'provide_normal_token',                     provide_normal_token,
        'qd',                                       qd,
        'qi',                                       qi,
        'qj',                                       qj,
        'qk',                                       qk,
        'ql',                                       ql,
        'qn',                                       qn,
        'qs',                                       qs,
        'raise_unknown_line',                       raise_unknown_line,
        'static_conjure_nub',                       static_conjure_nub,
        'store_adjusted_meta',                      store_adjusted_meta,
        'transform__self',                          transform__self,
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
        'create_cache',                         create_cache,
        'create_DelayedFileOutput',             create_DelayedFileOutput,
        'create_SimpleStringOutput',            create_SimpleStringOutput,
        'create_StringOutput',                  create_StringOutput,
        'path_join',                            path_join,
        'print_cache',                          print_cache,
        'print_exception_chain',                print_exception_chain,
        'produce_conjure_dual__21',             produce_conjure_dual__21,
        'produce_conjure_dual',                 produce_conjure_dual,
        'produce_conjure_single',               produce_conjure_single,
        'produce_conjure_triple__312',          produce_conjure_triple__312,
        'produce_conjure_triple',               produce_conjure_triple,
        'produce_conjure_tuple',                produce_conjure_tuple,
        'produce_conjure_unique_dual__21',      produce_conjure_unique_dual__21,
        'produce_conjure_unique_dual',          produce_conjure_unique_dual,
        'produce_conjure_quadruple__4123',      produce_conjure_quadruple__4123,
        'produce_conjure_unique_triple',        produce_conjure_unique_triple,
        'produce_conjure_unique_triple__312',   produce_conjure_unique_triple__312,
        'program_exit',                         program_exit,
        'read_text_from_path',                  read_text_from_path,
        'return_self',                          return_self,


        #
        #   Values (CoreParser)
        #
        'CLASS_ORDER__NORMAL_TOKEN',                CLASS_ORDER__NORMAL_TOKEN,
        'CLASS_ORDER__PYTHON_END',                  CLASS_ORDER__PYTHON_END,
        'CLASS_ORDER__PYTHON_START',                CLASS_ORDER__PYTHON_START,
        'parse_context',                            parse_context,


        #
        #   Values (Gem)
        #
        'binary_path',          binary_path,
        'empty_herd',           empty_herd,
        'source_path',          source_path,
        'slice_all',            slice_all,
        'tuple_of_2_nones',     ((none, none)),
    )
