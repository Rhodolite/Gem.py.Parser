#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.Parse1')
def gem():
    require_gem('PythonParser.Core')

    require_gem('PythonParser.Atom')
    require_gem('PythonParser.BinaryExpression')
    require_gem('PythonParser.Comment')
    require_gem('PythonParser.Parse1Atom')
    require_gem('PythonParser.Parse1Call')
    require_gem('PythonParser.Parse1Complex')
    require_gem('PythonParser.Parse1Expression')
    require_gem('PythonParser.Parse1ExpressionStatement')
    require_gem('PythonParser.Parse1From')
    require_gem('PythonParser.Parse1Function')
    require_gem('PythonParser.Parse1Import')
    require_gem('PythonParser.Parse1Simple')
    require_gem('PythonParser.QuadrupleToken')
    require_gem('PythonParser.Tokenize1Atom')
    require_gem('PythonParser.Tokenize1Header')
    require_gem('PythonParser.Tokenize1Name')
    require_gem('PythonParser.Tokenize1Operator')


    find_parse1_colon_line = {
                                 'else'    : parse1_statement_else_colon,
                                 'except'  : parse1_statement_except_colon,
                                 'finally' : parse1_statement_finally_colon,
                                 'try'     : parse1_statement_try_colon,
                             }.__getitem__


    lookup_parse1_line = {
                             '@'        : parse1_statement_decorator_header,
                             'assert'   : parse1_statement_assert,
                             'break'    : parse1_statement_break,
                             'class'    : parse1_statement_class_header,
                             'continue' : parse1_statement_continue,
                             'def'      : parse1_statement_function_header,
                             'del'      : parse1_statement_delete,
                             'elif'     : parse1_statement_else_if,
                             'except'   : parse1_statement_except,
                             'for'      : parse1_statement_for,
                             'from'     : parse1_statement_from,
                             'if'       : parse1_statement_if,
                             'import'   : parse1_statement_import,
                             'pass'     : parse1_statement_pass,
                             'raise'    : parse1_statement_raise,
                             'return'   : parse1_statement_return,
                             'yield'    : parse1_statement_yield,
                             'while'    : parse1_statement_while,
                             'with'     : parse1_statement_with,
                         }.get


    @share
    def parse1_python_from_path(path):
        data = read_text_from_path(path)

        parse_context = z_initialize(path, data)

        append        = parse_context.append
        many          = parse_context.many
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
                        parse1_line = lookup_parse1_line(atom_s)

                        if parse1_line is not none:
                            append(parse1_line(m))

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
                            parse1_statement_expression__atom(
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
                            parse1_statement_expression__atom(
                                m.group('indented'),
                                analyze_atom(m)
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

        return ((data, parse_context.data_lines, many))
