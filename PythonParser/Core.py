#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.Core')
def gem():
    require_gem('CoreParser.ActionWord')
    require_gem('CoreParser.Atom')
    require_gem('CoreParser.ClassOrder')
    require_gem('CoreParser.CreateMeta')
    require_gem('CoreParser.CrystalComment')
    require_gem('CoreParser.CrystalIndentation')
    require_gem('CoreParser.DualFrill')
    require_gem('CoreParser.DualTwig')
    require_gem('CoreParser.DumpToken')
    require_gem('CoreParser.Elemental')
    require_gem('CoreParser.EmptyLine')
    require_gem('CoreParser.LineMarker')
    require_gem('CoreParser.Method')
    require_gem('CoreParser.Nub')
    require_gem('CoreParser.ParserToken')
    require_gem('CoreParser.ParserTrunk')
    require_gem('CoreParser.TestTree')
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
    require_gem('Gem.System')
    require_gem('Gem.Traceback')


    from CoreParser import CLASS_ORDER__EMPTY_LINE, CLASS_ORDER__INDENTATION, CLASS_ORDER__LINE_MARKER
    from CoreParser import CLASS_ORDER__NORMAL_TOKEN, CLASS_ORDER__PYTHON_END, CLASS_ORDER__PYTHON_START
    from CoreParser import conjure_action_word, conjure_action_word__ends_in_newline, conjure_ActionWord_WithNewlines
    from CoreParser import conjure_any_comment_line, conjure_commented_v_frill, conjure_empty_line
    from CoreParser import conjure_indentation, conjure_keyword_import, conjure_line_marker
    from CoreParser import conjure_name, conjure_nub, conjure_vw_frill
    from CoreParser import construct__ab, count_newlines__ab, create_TokenOutput
    from CoreParser import display_token__ab, dump_token, dump_token__12, DualTwig
    from CoreParser import empty_comment_line, empty_indentation, find_require_gem__0
    from CoreParser import Identifier, initialize_action_word__Meta, is_name__0, KeywordAndOperatorBase
    from CoreParser import KeywordImport
    from CoreParser import la, LINE_MARKER
    from CoreParser import lookup_adjusted_meta, lookup_indentation, lookup_line_marker, lookup_normal_token
    from CoreParser import mutate__self, next_indentation, order__ab, order__s, order__string
    from CoreParser import parse_context, ParserToken, ParserTrunk, portray__ab
    from CoreParser import produce_conjure_action_word, produce_conjure_atom, produce_conjure_dual_twig
    from CoreParser import produce_mutate__uncommented, produce_transform__ab, produce_transform__uncommented
    from CoreParser import provide_indentation, provide_line_marker, provide_normal_token
    from CoreParser import qd, qi, qj, qk, ql, qn, qs
    from CoreParser import raise_unknown_line, scout_variables__0, static_conjure_nub, store_adjusted_meta
    from CoreParser import test_count_newlines, test_identical_output, transform__remove_comments_0, transform__self
    from CoreParser import wd, wd0, wd1, wi, wj, wk, wn, ws, z_initialize
    from Gem import create_cache, create_DelayedFileOutput, create_SimpleStringOutput, create_StringOutput
    from Gem import empty_herd, module_path, path_join, path_normalize, print_cache, print_exception_chain
    from Gem import produce_conjure_dual, produce_conjure_dual__21
    from Gem import produce_conjure_quadruple__4123
    from Gem import produce_conjure_single, produce_conjure_triple
    from Gem import produce_conjure_triple__312, produce_conjure_tuple
    from Gem import produce_conjure_unique_dual, produce_conjure_unique_dual__21
    from Gem import produce_conjure_unique_triple, produce_conjure_unique_triple__312
    from Gem import program_exit, read_text_from_path, return_self, slice_all


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
        'DualTwig',                 DualTwig,
        'ParserToken',              ParserToken,
        'Identifier',               Identifier,
        'KeywordAndOperatorBase',   KeywordAndOperatorBase,
        'KeywordImport',            KeywordImport,
        'ParserTrunk',              ParserTrunk,

        
        #
        #   Imported functions (CoreParser)
        #
        'conjure_action_word',                      conjure_action_word,
        'conjure_action_word__ends_in_newline',     conjure_action_word__ends_in_newline,
        'conjure_ActionWord_WithNewlines',          conjure_ActionWord_WithNewlines,
        'conjure_any_comment_line',                 conjure_any_comment_line,
        'conjure_commented_v_frill',                conjure_commented_v_frill,
        'conjure_empty_line',                       conjure_empty_line,
        'conjure_indentation',                      conjure_indentation,
        'conjure_keyword_import',                   conjure_keyword_import,
        'conjure_line_marker',                      conjure_line_marker,
        'conjure_name',                             conjure_name,
        'conjure_nub',                              conjure_nub,
        'conjure_vw_frill',                         conjure_vw_frill,
        'construct__ab',                            construct__ab,
        'count_newlines__ab',                       count_newlines__ab,
        'create_TokenOutput',                       create_TokenOutput,
        'display_token__ab',                        display_token__ab,
        'dump_token__12',                           dump_token__12,
        'dump_token',                               dump_token,
        'find_require_gem__0',                      find_require_gem__0,
        'initialize_action_word__Meta',             initialize_action_word__Meta,
        'is_name__0',                               is_name__0,
        'la',                                       la,
        'lookup_adjusted_meta',                     lookup_adjusted_meta,
        'lookup_indentation',                       lookup_indentation,
        'lookup_line_marker',                       lookup_line_marker,
        'lookup_normal_token',                      lookup_normal_token,
        'mutate__self',                             mutate__self,
        'next_indentation',                         next_indentation,
        'order__ab',                                order__ab,
        'order__s',                                 order__s,
        'order__string',                            order__string,
        'portray__ab',                              portray__ab,
        'produce_conjure_action_word',              produce_conjure_action_word,
        'produce_conjure_atom',                     produce_conjure_atom,
        'produce_conjure_dual_twig',                produce_conjure_dual_twig,
        'produce_mutate__uncommented',              produce_mutate__uncommented,
        'produce_transform__ab',                    produce_transform__ab,
        'produce_transform__uncommented',           produce_transform__uncommented,
        'provide_indentation',                      provide_indentation,
        'provide_line_marker',                      provide_line_marker,
        'provide_normal_token',                     provide_normal_token,
        'qd',                                       qd,
        'qi',                                       qi,
        'qj',                                       qj,
        'qk',                                       qk,
        'ql',                                       ql,
        'qn',                                       qn,
        'qs',                                       qs,
        'raise_unknown_line',                       raise_unknown_line,
        'scout_variables__0',                       scout_variables__0,
        'static_conjure_nub',                       static_conjure_nub,
        'store_adjusted_meta',                      store_adjusted_meta,
        'test_count_newlines',                      test_count_newlines,
        'test_identical_output',                    test_identical_output,
        'transform__remove_comments_0',             transform__remove_comments_0,
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
        'CLASS_ORDER__EMPTY_LINE',      CLASS_ORDER__EMPTY_LINE,
        'CLASS_ORDER__INDENTATION',     CLASS_ORDER__INDENTATION,
        'CLASS_ORDER__NORMAL_TOKEN',    CLASS_ORDER__NORMAL_TOKEN,
        'CLASS_ORDER__LINE_MARKER',     CLASS_ORDER__LINE_MARKER,
        'CLASS_ORDER__PYTHON_END',      CLASS_ORDER__PYTHON_END,
        'CLASS_ORDER__PYTHON_START',    CLASS_ORDER__PYTHON_START,
        'empty_comment_line',           empty_comment_line,
        'empty_indentation',            empty_indentation,
        'LINE_MARKER',                  LINE_MARKER,
        'parse_context',                parse_context,


        #
        #   Values (Gem)
        #
        'binary_path',          binary_path,
        'empty_herd',           empty_herd,
        'source_path',          source_path,
        'slice_all',            slice_all,
        'tuple_of_2_nones',     ((none, none)),
    )
