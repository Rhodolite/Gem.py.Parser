#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Parse1')
def module():
    require_module('PythonParser.Atom')
    require_module('PythonParser.BinaryExpression')
    require_module('PythonParser.Parse1Atom')
    require_module('PythonParser.Parse1Call')
    require_module('PythonParser.Parse1Complex')
    require_module('PythonParser.Parse1Expression')
    require_module('PythonParser.Parse1ExpressionStatement')
    require_module('PythonParser.Parse1From')
    require_module('PythonParser.Parse1Function')
    require_module('PythonParser.Parse1Import')
    require_module('PythonParser.Parse1Simple')
    require_module('PythonParser.QuadrupleToken')
    require_module('PythonParser.Tokenize1Atom')
    require_module('PythonParser.Tokenize1Header')
    require_module('PythonParser.Tokenize1Name')
    require_module('PythonParser.Tokenize1Operator')


    find_parse1_colon_line = {
                                 'else'    : parse_python__statement_else_colon,
                                 'except'  : parse_python__statement_except_colon,
                                 'finally' : parse_python__statement_finally_colon,
                                 'try'     : parse_python__statement_try_colon,
                             }.__getitem__


    lookup_parse1_line = {
                             '@'        : parse_python__statement_decorator_header,
                             'assert'   : parse_python__statement_assert,
                             'break'    : parse_python__statement_break,
                             'class'    : parse_python__statement_class_header,
                             'continue' : parse_python__statement_continue,
                             'def'      : parse_python__statement_function_header,
                             'del'      : parse_python__statement_delete,
                             'elif'     : parse_python__statement_else_if,
                             'except'   : parse_python__statement_except,
                             'for'      : parse_python__statement_for,
                             'from'     : parse_python__statement_from,
                             'if'       : parse_python__statement_if,
                             'import'   : parse_python__statement_import,
                             'pass'     : parse_python__statement_pass,
                             'raise'    : parse_python__statement_raise,
                             'return'   : parse_python__statement_return,
                             'yield'    : parse_python__statement_yield,
                             'while'    : parse_python__statement_while,
                             'with'     : parse_python__statement_with,
                         }.get


    @share
    def parse_python_from_path(path):
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
                            parse_python__statement_expression__atom(
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
                            parse_python__statement_expression__atom(
                                m.group('indented'),
                                analyze_python_atom(m)
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
