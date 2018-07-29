#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Core')
def module():
    require_module('Capital.Cache')
    require_module('Capital.Cache2')
    require_module('Capital.DelayedFileOutput')
    require_module('Capital.DumpCache')
    require_module('Capital.Exception')
    require_module('Capital.GeneratedConjureQuadruple')
    require_module('Capital.Herd')
    require_module('Capital.Method')
    require_module('Capital.Path')
    require_module('Capital.PortrayString')                                #   For builtin `portray_string`
    require_module('Capital.System')
    require_module('Capital.Traceback')
    require_module('CoreParser.ActionWord')
    require_module('CoreParser.Atom')
    require_module('CoreParser.BookcaseCoupleTwig')
    require_module('CoreParser.BookcaseDualTwig')
    require_module('CoreParser.ClassOrder')
    require_module('CoreParser.CreateMeta')
    require_module('CoreParser.CrystalComment')
    require_module('CoreParser.CrystalIndentation')
    require_module('CoreParser.DualExpressionStatement')
    require_module('CoreParser.DualFrill')
    require_module('CoreParser.DualTwig')
    require_module('CoreParser.DumpToken')
    require_module('CoreParser.Elemental')
    require_module('CoreParser.EmptyLine')
    require_module('CoreParser.LineMarker')
    require_module('CoreParser.Method')
    require_module('CoreParser.Nub')
    require_module('CoreParser.ParserToken')
    require_module('CoreParser.ParserTrunk')
    require_module('CoreParser.TestTree')
    require_module('CoreParser.Tokenizer')
    require_module('CoreParser.TripleFrill')
    require_module('CoreParser.TripleTwig')


    from Capital import create_cache, create_DelayedFileOutput, create_SimpleStringOutput, create_StringOutput
    from Capital import empty_herd, module_path, path_join, path_normalize, print_cache, print_exception_chain
    from Capital import produce_conjure_dual, produce_conjure_dual__21
    from Capital import produce_conjure_quadruple__4123
    from Capital import produce_conjure_single, produce_conjure_triple
    from Capital import produce_conjure_triple__312, produce_conjure_tuple
    from Capital import produce_conjure_unique_dual, produce_conjure_unique_dual__21
    from Capital import produce_conjure_unique_triple, produce_conjure_unique_triple__312
    from Capital import program_exit, read_text_from_path, return_self, slice_all
    from CoreParser import BookcaseCoupleTwig, BookcaseDualTwig
    from CoreParser import CLASS_ORDER__INDENTATION
    from CoreParser import CLASS_ORDER__NORMAL_TOKEN, CLASS_ORDER__PYTHON_END, CLASS_ORDER__PYTHON_START
    from CoreParser import conjure_action_word, conjure_action_word__ends_in_newline, conjure_ActionWord_WithNewlines
    from CoreParser import conjure_any_comment_line, conjure_commented_v_frill, conjure_double_quote
    from CoreParser import conjure_empty_line
    from CoreParser import conjure_commented_vw_frill, produce_conjure_dual_twig, produce_conjure_triple_twig
    from CoreParser import conjure_indentation, conjure_keyword_import, conjure_line_marker
    from CoreParser import conjure_name, conjure_nub, conjure_single_quote, conjure_vw_frill, conjure_vwx_frill
    from CoreParser import construct__123, construct__ab, count_newlines__123, count_newlines__ab, create_TokenOutput
    from CoreParser import display_token__123, display_token__ab, DoubleQuote, dump_token, dump_token__12
    from CoreParser import DualExpressionStatement, DualTwig
    from CoreParser import empty_comment_line, empty_indentation, find_require_module__0
    from CoreParser import Identifier, initialize_action_word__Meta, is_name__0, KeywordAndOperatorBase
    from CoreParser import KeywordImport
    from CoreParser import la, LINE_MARKER
    from CoreParser import lookup_adjusted_meta, lookup_indentation, lookup_line_marker, lookup_normal_token
    from CoreParser import mutate__self, next_indentation
    from CoreParser import order__ab, order__abc, order__frill_ab, order__s, order__string
    from CoreParser import parse_context, ParserToken, ParserTrunk, portray__123, portray__ab
    from CoreParser import produce_conjure_action_word, produce_conjure_atom, produce_conjure_dual_twig
    from CoreParser import produce_conjure_bookcase_couple_twig, produce_conjure_bookcase_dual_twig
    from CoreParser import produce_conjure_bookcase_dual_twig, produce_conjure_action_word, produce_conjure_atom
    from CoreParser import produce_dual_expression_statement, produce_mutate__uncommented, produce_transform__ab
    from CoreParser import produce_transform__abc, produce_transform__uncommented
    from CoreParser import provide_indentation, provide_line_marker, provide_normal_token
    from CoreParser import qd, qi, qj, qk, ql, qn, qs
    from CoreParser import raise_unknown_line
    from CoreParser import scout_variables__0, SingleQuote, static_conjure_nub, store_adjusted_meta
    from CoreParser import test_count_newlines, test_identical_output, transform__remove_comments_0, transform__self
    from CoreParser import TripleTwig
    from CoreParser import wd, wd0, wd1, wi, wj, wk, wn, ws, z_initialize


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


    #
    #   Avoid: "SyntaxError: more than 255 arguments" by breaking up the calls to `share`
    #
    share(
        #
        #   Imported types (CoreParser)
        #
        'BookcaseCoupleTwig',       BookcaseCoupleTwig,
        'BookcaseDualTwig',         BookcaseDualTwig,
        'DoubleQuote',              DoubleQuote,
        'DualExpressionStatement',  DualExpressionStatement,
        'DualTwig',                 DualTwig,
        'Identifier',               Identifier,
        'KeywordAndOperatorBase',   KeywordAndOperatorBase,
        'KeywordImport',            KeywordImport,
        'ParserToken',              ParserToken,
        'ParserTrunk',              ParserTrunk,
        'SingleQuote',              SingleQuote,
        'TripleTwig',               TripleTwig,
    )


    share(
        #
        #   Imported functions (Capital)
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
    )


    share(
        #
        #   Imported functions (CoreParser)
        #
        'conjure_single_quote',                     conjure_single_quote,
        'conjure_double_quote',                     conjure_double_quote,
        'conjure_action_word',                      conjure_action_word,
        'conjure_action_word__ends_in_newline',     conjure_action_word__ends_in_newline,
        'conjure_ActionWord_WithNewlines',          conjure_ActionWord_WithNewlines,
        'conjure_any_comment_line',                 conjure_any_comment_line,
        'conjure_commented_v_frill',                conjure_commented_v_frill,
        'conjure_commented_vw_frill',               conjure_commented_vw_frill,
        'conjure_empty_line',                       conjure_empty_line,
        'conjure_indentation',                      conjure_indentation,
        'conjure_keyword_import',                   conjure_keyword_import,
        'conjure_line_marker',                      conjure_line_marker,
        'conjure_name',                             conjure_name,
        'conjure_nub',                              conjure_nub,
        'conjure_vw_frill',                         conjure_vw_frill,
        'conjure_vwx_frill',                        conjure_vwx_frill,
        'construct__123',                           construct__123,
        'construct__ab',                            construct__ab,
        'count_newlines__123',                      count_newlines__123,
        'count_newlines__ab',                       count_newlines__ab,
        'create_TokenOutput',                       create_TokenOutput,
        'display_token__123',                       display_token__123,
        'display_token__ab',                        display_token__ab,
        'dump_token__12',                           dump_token__12,
        'dump_token',                               dump_token,
        'find_require_module__0',                   find_require_module__0,
        'initialize_action_word__Meta',             initialize_action_word__Meta,
        'is_name__0',                               is_name__0,
        'la',                                       la,
        'lookup_adjusted_meta',                     lookup_adjusted_meta,
        'lookup_indentation',                       lookup_indentation,
        'lookup_line_marker',                       lookup_line_marker,
        'lookup_normal_token',                      lookup_normal_token,
        'mutate__self',                             mutate__self,
        'next_indentation',                         next_indentation,
        'order__abc',                               order__abc,
        'order__ab',                                order__ab,
        'order__frill_ab',                          order__frill_ab,
        'order__s',                                 order__s,
        'order__string',                            order__string,
        'portray__123',                             portray__123,
        'portray__ab',                              portray__ab,
        'produce_conjure_action_word',              produce_conjure_action_word,
        'produce_conjure_atom',                     produce_conjure_atom,
        'produce_conjure_bookcase_couple_twig',     produce_conjure_bookcase_couple_twig,
        'produce_conjure_bookcase_dual_twig',       produce_conjure_bookcase_dual_twig,
        'produce_conjure_dual_twig',                produce_conjure_dual_twig,
        'produce_conjure_triple_twig',              produce_conjure_triple_twig,
        'produce_dual_expression_statement',        produce_dual_expression_statement,
        'produce_mutate__uncommented',              produce_mutate__uncommented,
        'produce_transform__abc',                   produce_transform__abc,
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
    )


    share(
        #
        #   Values (Capital)
        #
        'binary_path',          binary_path,
        'empty_herd',           empty_herd,
        'source_path',          source_path,
        'slice_all',            slice_all,
        'tuple_of_2_nones',     ((none, none)),
    )


    share(
        #
        #   Values (CoreParser)
        #
        'CLASS_ORDER__INDENTATION',     CLASS_ORDER__INDENTATION,
        'CLASS_ORDER__NORMAL_TOKEN',    CLASS_ORDER__NORMAL_TOKEN,
        'CLASS_ORDER__PYTHON_END',      CLASS_ORDER__PYTHON_END,
        'CLASS_ORDER__PYTHON_START',    CLASS_ORDER__PYTHON_START,
        'empty_comment_line',           empty_comment_line,
        'empty_indentation',            empty_indentation,
        'LINE_MARKER',                  LINE_MARKER,
        'parse_context',                parse_context,
    )
