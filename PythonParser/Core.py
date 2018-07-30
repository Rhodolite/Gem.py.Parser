#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Core')
def module():
    require_module('Capital.PortrayString')                                #   For builtin `portray_string`


    transport('Capital.Cache2',                     'create_cache')
    transport('Capital.Cache2',                     'produce_conjure_unique_dual')
    transport('Capital.Cache2',                     'produce_conjure_unique_dual__21')
    transport('Capital.Cache2',                     'produce_conjure_unique_triple')
    transport('Capital.Cache2',                     'produce_conjure_unique_triple__312')
    transport('Capital.Cache',                      'produce_conjure_dual')
    transport('Capital.Cache',                      'produce_conjure_dual__21')
    transport('Capital.Cache',                      'produce_conjure_single')
    transport('Capital.Cache',                      'produce_conjure_triple')
    transport('Capital.Cache',                      'produce_conjure_triple__312')
    transport('Capital.Cache',                      'produce_conjure_tuple')
    transport('Capital.DelayedFileOutput',          'create_DelayedFileOutput')
    transport('Capital.DumpCache',                  'print_cache')
    transport('Capital.GeneratedConjureQuadruple',  'produce_conjure_quadruple__4123')
    transport('Capital.Path',                       'path_join')
    transport('Capital.Path',                       'path_normalize')
    transport('Capital.Path',                       'read_text_from_path')
    transport('Capital.System',                     'module_path')
    transport('Capital.System',                     'program_exit')
    transport('Capital.System',                     'slice_all')
    transport('Capital.Traceback',                  'print_exception_chain')
    transport('CoreParser.ActionWord',              'conjure_action_word')
    transport('CoreParser.ActionWord',              'conjure_action_word__ends_in_newline')
    transport('CoreParser.ActionWord',              'conjure_ActionWord_WithNewlines')
    transport('CoreParser.ActionWord',              'initialize_action_word__Meta')
    transport('CoreParser.ActionWord',              'produce_conjure_action_word')
    transport('CoreParser.Atom',                    'conjure_double_quote')
    transport('CoreParser.Atom',                    'conjure_name')
    transport('CoreParser.Atom',                    'conjure_single_quote')
    transport('CoreParser.Atom',                    'DoubleQuote')
    transport('CoreParser.Atom',                    'produce_conjure_atom')
    transport('CoreParser.Atom',                    'SingleQuote')
    transport('CoreParser.Atom',                    'TokenName')
    transport('CoreParser.BookcaseCoupleTwig',      'BookcaseCoupleTwig')
    transport('CoreParser.BookcaseCoupleTwig',      'produce_conjure_bookcase_couple_twig')
    transport('CoreParser.BookcaseDualTwig',        'BookcaseDualTwig')
    transport('CoreParser.BookcaseDualTwig',        'produce_conjure_bookcase_dual_twig')
    transport('CoreParser.ClassOrder',              'CLASS_ORDER__NORMAL_TOKEN')
    transport('CoreParser.ClassOrder',              'CLASS_ORDER__PYTHON_END')
    transport('CoreParser.ClassOrder',              'CLASS_ORDER__PYTHON_START')
    transport('CoreParser.CreateMeta',              'lookup_adjusted_meta')
    transport('CoreParser.CreateMeta',              'store_adjusted_meta')
    transport('CoreParser.CrystalComment',          'conjure_any_comment_line')
    transport('CoreParser.CrystalComment',          'empty_comment_line')
    transport('CoreParser.CrystalIndentation',      'conjure_indentation')
    transport('CoreParser.CrystalIndentation',      'empty_indentation')
    transport('CoreParser.CrystalIndentation',      'next_indentation')
    transport('CoreParser.DualExpressionStatement', 'DualExpressionStatement')
    transport('CoreParser.DualExpressionStatement', 'produce_dual_expression_statement')
    transport('CoreParser.DualFrill',               'conjure_commented_v_frill')
    transport('CoreParser.DualFrill',               'conjure_vw_frill')
    transport('CoreParser.DualTwig',                'DualTwig')
    transport('CoreParser.DualTwig',                'produce_conjure_dual_twig')
    transport('CoreParser.DumpToken',               'create_TokenOutput')
    transport('CoreParser.DumpToken',               'dump_all_tokens')
    transport('CoreParser.Elemental',               'conjure_keyword_import')
    transport('CoreParser.Elemental',               'KeywordAndOperatorBase')
    transport('CoreParser.Elemental',               'KeywordImport')
    transport('CoreParser.EmptyLine',               'conjure_empty_line')
    transport('CoreParser.LineMarker',              'conjure_line_marker')
    transport('CoreParser.LineMarker',              'LINE_MARKER')
    transport('CoreParser.Method',                  'construct__123')
    transport('CoreParser.Method',                  'count_newlines__123')
    transport('CoreParser.Method',                  'display_token__123')
    transport('CoreParser.Method',                  'find_require_module__0')
    transport('CoreParser.Method',                  'is_name__0')
    transport('CoreParser.Method',                  'mutate__self')
    transport('CoreParser.Method',                  'order__ab')
    transport('CoreParser.Method',                  'order__abc')
    transport('CoreParser.Method',                  'order__frill_ab')
    transport('CoreParser.Method',                  'order__s')
    transport('CoreParser.Method',                  'portray__123')
    transport('CoreParser.Method',                  'portray__ab')
    transport('CoreParser.Method',                  'produce_mutate__uncommented')
    transport('CoreParser.Method',                  'produce_transform__ab')
    transport('CoreParser.Method',                  'produce_transform__abc')
    transport('CoreParser.Method',                  'produce_transform__uncommented')
    transport('CoreParser.Method',                  'scout_variables__0')
    transport('CoreParser.Method',                  'transform__remove_comments_0')
    transport('CoreParser.Method',                  'transform__self')
    transport('CoreParser.Nub',                     'conjure_nub')
    transport('CoreParser.Nub',                     'static_conjure_nub')
    transport('CoreParser.ParserToken',             'ParserToken')
    transport('CoreParser.ParserTrunk',             'ParserTrunk')
    transport('CoreParser.TestTree',                'test_count_newlines')
    transport('CoreParser.TestTree',                'test_identical_output')
    transport('CoreParser.TokenCache',              'lookup_indentation')
    transport('CoreParser.TokenCache',              'lookup_line_marker')
    transport('CoreParser.TokenCache',              'lookup_normal_token')
    transport('CoreParser.TokenCache',              'provide_indentation')
    transport('CoreParser.TokenCache',              'provide_line_marker')
    transport('CoreParser.TokenCache',              'provide_normal_token')
    transport('CoreParser.Tokenizer',               'parse_context')
    transport('CoreParser.Tokenizer',               'qd')
    transport('CoreParser.Tokenizer',               'qi')
    transport('CoreParser.Tokenizer',               'qj')
    transport('CoreParser.Tokenizer',               'qk')
    transport('CoreParser.Tokenizer',               'ql')
    transport('CoreParser.Tokenizer',               'qn')
    transport('CoreParser.Tokenizer',               'qs')
    transport('CoreParser.Tokenizer',               'raise_unknown_line')
    transport('CoreParser.Tokenizer',               'wd')
    transport('CoreParser.Tokenizer',               'wd0')
    transport('CoreParser.Tokenizer',               'wd1')
    transport('CoreParser.Tokenizer',               'wi')
    transport('CoreParser.Tokenizer',               'wj')
    transport('CoreParser.Tokenizer',               'wk')
    transport('CoreParser.Tokenizer',               'wn')
    transport('CoreParser.Tokenizer',               'ws')
    transport('CoreParser.Tokenizer',               'z_initialize')
    transport('CoreParser.TripleFrill',             'conjure_commented_vw_frill')
    transport('CoreParser.TripleFrill',             'conjure_vwx_frill')
    transport('CoreParser.TripleTwig',              'produce_conjure_triple_twig')
    transport('CoreParser.TripleTwig',              'TripleTwig')


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
        #   Values (Capital)
        #
        'binary_path',          binary_path,
        'source_path',          source_path,
    )
