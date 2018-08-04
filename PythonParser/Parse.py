#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Parse')
def module():
    require_module('PythonParser.Atom')
    require_module('PythonParser.BinaryExpression')
    require_module('PythonParser.ParseCall')
    require_module('PythonParser.ParseComplex')
    require_module('PythonParser.ParseExpression')
    require_module('PythonParser.ParseExpressionStatement')
    require_module('PythonParser.ParseFrom')
    require_module('PythonParser.ParseFunction')
    require_module('PythonParser.ParseImport')
    require_module('PythonParser.ParseSimple')
    require_module('PythonParser.Parse3')
    require_module('PythonParser.ParseAtom')
    require_module('PythonParser.QuadrupleToken')
    require_module('PythonParser.TokenizeAtom')
    require_module('PythonParser.TokenizeHeader')
    require_module('PythonParser.TokenizeName')


    find_parse1_colon_line = {
                                 'else'    : parse_PYTHON__statement_else_colon,
                                 'except'  : parse_PYTHON__statement_except_colon,
                                 'finally' : parse_PYTHON__statement_finally_colon,
                                 'try'     : parse_PYTHON__statement_try_colon,
                             }.__getitem__


    lookup_parse1_line = {
                             '@'        : parse_PYTHON__statement_decorator_header,
                             'assert'   : parse_PYTHON__statement_assert,
                             'break'    : parse_PYTHON__statement_break,
                             'class'    : parse_PYTHON__statement_class_header,
                             'continue' : parse_PYTHON__statement_continue,
                             'def'      : parse_PYTHON__statement_function_header,
                             'del'      : parse_PYTHON__statement_delete,
                             'elif'     : parse_PYTHON__statement_else_if,
                             'except'   : parse_PYTHON__statement_except,
                             'for'      : parse_PYTHON__statement_for,
                             'from'     : parse_PYTHON__statement_from,
                             'if'       : parse_PYTHON__statement_if,
                             'import'   : parse_PYTHON__statement_import,
                             'pass'     : parse_PYTHON__statement_pass,
                             'raise'    : parse_PYTHON__statement_raise,
                             'return'   : parse_PYTHON__statement_return,
                             'yield'    : parse_PYTHON__statement_yield,
                             'while'    : parse_PYTHON__statement_while,
                             'with'     : parse_PYTHON__statement_with,
                         }.get




    def show_indentation(data_many):
        for v in data_many:
            indentation = v.indentation

            if indentation is none:
                line(v.display_token())
                continue

            line('+%d %s', indentation.total, v.display_token())


    def show_tree(tree_many, vary):
        with create_TokenOutput() as f:
            f.line('===  show_tree  ===')

            for v in tree_many:
                if vary is not 0:
                    v = v.transform(vary)

                    if v is 0:
                        continue

                r = v.dump_token(f)

                assert not r

        partial(f.result)


    @share
    def parse_PYTHON(path, vary = 0, show = 0, test = 0):
        #line("parse_PYTHON(path<%s>, vary<%d>, show<%d>, test<%d>)", path, vary, show, test);

        data = read_text_from_path(path)

        parse_context = z_initialize(path, data)

        append        = parse_context.append
        iterate_lines = parse_context.iterate_lines

        for LOOP in parse_context:
            with parse_context:
                for s in iterate_lines:
                    assert qd() is 0

                    m = line_match(s)

                    if m is none:
                        raise_unknown_line()

                    atom_s = m.group('atom')

                    if atom_s is not none:
                        parse_line = lookup_parse1_line(atom_s)

                        if parse_line is not none:
                            append(parse_line(m))

                            assert qd() is 0
                            continue

                        if m.start('newline') is not -1:
                            append(
                                conjure_expression_statement(
                                    conjure_indentation(m.group('indented')),
                                    conjure_name(atom_s),
                                    conjure_line_marker(s[m.end('atom'):]),
                                ),
                            )

                            assert qd() is 0
                            continue

                        wi(m.end('atom'))
                        wj(m.end())

                        append(
                            parse_PYTHON__statement_expression__atom(
                                m.group('indented'),
                                conjure_name(atom_s),
                            ),
                        )

                        assert qd() is 0
                        continue

                    keyword = m.group('keyword')

                    if keyword is not none:
                        append(find_parse1_colon_line(keyword)(m))

                        assert qd() is 0
                        continue

                    if m.start('something') is not -1:
                        j = m.end('indented')

                        wi(j)
                        wj(j)

                        append(
                            parse_PYTHON__statement_expression__atom(
                                m.group('indented'),
                                analyze_PYTHON_atom(m)
                            ),
                        )

                        assert qd() is 0
                        continue

                    comment_end = m.end('comment')

                    if comment_end is not -1:
                        append(conjure_any_comment_line(m.end('indented'), comment_end))
                        continue

                    if m.end('newline') is -1:
                        raise_unknown_line()

                    append(conjure_empty_line(m.group()))

        data_many  = parse_context.many
        data_lines = parse_context.data_lines

        if show is 5:
            show_indentation(data_many)

        tree_many = parse3_PYTHON(path, data, data_lines, data_many)

        if show is 7:
            show_tree(tree_many, vary)

        if test is 7:
            test_identical_output(path, data, data_many, tree_many)
            test_count_newlines(data_lines, tree_many)

        #dump_newline_meta_cache()
        #dump_caches__OLD('dual-twig')

        return tree_many
