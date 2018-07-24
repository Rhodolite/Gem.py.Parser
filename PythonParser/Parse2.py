#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.Parse2')
def gem():
    show = 0


    require_gem('PythonParser.Core')

    require_gem('PythonParser.BinaryExpression')
    require_gem('PythonParser.BookcaseDualExpression')
    require_gem('PythonParser.BookcaseExpression')
    require_gem('PythonParser.DualToken')
    require_gem('PythonParser.Match')
    require_gem('PythonParser.Parse1Atom')
    require_gem('PythonParser.Parse1Call')
    require_gem('PythonParser.Parse1Complex')
    require_gem('PythonParser.Parse1Expression')
    require_gem('PythonParser.Parse1ExpressionStatement')
    require_gem('PythonParser.Parse1From')
    require_gem('PythonParser.Parse1Function')
    require_gem('PythonParser.Parse1Import')
    require_gem('PythonParser.Parse1Simple')
    require_gem('PythonParser.PostfixExpression')
    require_gem('PythonParser.Tokenize1Atom')
    require_gem('PythonParser.Tokenize1Header')
    require_gem('PythonParser.Tokenize1Name')
    require_gem('PythonParser.Tokenize1Operator')
    require_gem('PythonParser.UnaryExpression')


    find_conjure_keyword_colon = {
                                     'else'    : conjure_indented_else_colon,
                                     'except'  : conjure_except_colon,
                                     'finally' : conjure_finally_colon,
                                     'try'     : conjure_try_colon,
                                 }.__getitem__


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
                             'continue' : parse1_statement_continue,
                             'class'    : parse1_statement_class_header,
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
    def parse2_python_from_path(path):
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

                        if m.start('comment_newline') is not -1:
                            append(
                                conjure_statement_expression(
                                    conjure_indented(m.group('indented')),
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
                    else:
                        keyword = m.group('keyword')

                        if keyword is not none:
                            if m.end('newline') is not -1:
                                append(find_conjure_keyword_colon(keyword)(qs()))

                                assert qd() is 0
                                continue

                            #append(find_parse1_colon_line(keyword)(m))
                            #assert qd() is 0
                            #continue
                        elif m.start('something') is not -1:
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
                        else:
                            comment_end = m.end('comment')

                            if comment_end is not -1:
                                append(conjure_any_comment_line(m.end('indented'), comment_end))
                                continue

                            if m.end('newline') is -1:
                                raise_unknown_line()

                            append(conjure_empty_line(m.group()))
                            continue

                    j = m.end()

                    wi(j)
                    wj(j)

                    while 7 is 7:
                        m = atom_match(qs(), qj())

                        if m is none:
                            #my_line('full: %r; s: %r', portray_string(qs()), portray_string(qs()[qj() :]))
                            raise_unknown_line()

                        token = analyze_atom(m)

                        if token.has_newline:
                            raise_unknown_line()

                        la(token)

                        #my_line('qs: %r', portray_string(qs()))
                        #my_line('token: %r', token)

                        raise_unknown_line()


                    if token.is_atom:
                        pass

                    if token.is_left_parenthesis:
                        return parse1__parenthesized_expression__left_parenthesis(token)

                    if token.is_left_square_bracket:
                        return parse1__list_expression__left_square_bracket(token)

                    if token.is_left_brace:
                        return parse1_map__left_brace(token)

                    if token.is_keyword_not:
                        return parse1_not_expression__operator(token)

                    if token.is_minus_sign:
                        return parse1_negative_expression__operator(token)

                    if token.is_tilde_sign:
                        return parse1_twos_complement_expression__operator(token)

                    if token.is_star_sign:
                        return conjure_star_argument(token, parse1_ternary_expression())

                    #my_line('token: %r', token)
                    raise_unknown_line()

        if show:
            for v in many:
                line('%s', v.display_token())

        with create_StringOutput() as f:
            w = f.write

            for v in many:
                v.write(w)

        if data != f.result:
            with create_DelayedFileOutput('oops.txt') as oops:
                oops.write(f.result)

            raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')

        line('Passed#2: identical dump from parse tree.  Total: %d line%s',
             length(many), (''   if length(many) is 0 else   's'))
