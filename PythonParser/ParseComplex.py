#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ParseComplex')
def module():
    require_module('PythonParser.PrefixedDualStatement')


    def parse_python__condition_statement__X__m(m, conjure_indented_keyword, evoke_header, conjure_body_statement):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_else_if(m.end('indented'), j)

        wi(j)
        wj(j)

        condition = parse_python__ternary_expression()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            operator = tokenize_python_operator()

        if qn() is not none:
            raise_unknown_line()

        if operator.is_colon__line_marker:
            return evoke_header(indented_keyword, condition, operator)

        if not operator.is_colon:
            raise_unknown_line()

        header = evoke_header(indented_keyword, condition, operator)

        assert qk() is none
        assert qn() is none

        m = simple_statement_match(qs(), qj())

        if m is none:
            #my_line('full: %r; s: %r', portray_string(qs()), portray_string(qs()[qj() :]))
            raise_unknown_line()

        token = analyze_python_atom(m)

        if token.is_keyword_return:
            if qn() is not none:
                raise_unknown_line()

            right = parse_python__ternary_expression_list()

            if qk() is not none:
                raise_unknown_line()

            newline = qn()

            if newline is none:
                raise_unknown_line()

            return conjure_body_statement(
                       header,
                       conjure_return_statement(
                           conjure_indented_token(empty_indentation, token),
                           right,
                           newline
                       ),
                   )

        if token.is_CRYSTAL_atom:
            pass
        elif token.is_CRYSTAL_left_parenthesis:
            token = parse_python__parenthesized_expression__left_parenthesis(token)
        elif token.is_left_square_bracket:
            token = parse_python__list_expression__left_square_bracket(token)
        elif token.is_left_brace:
            token = parse_python__map__left_brace(token)
        elif token.is_keyword_not:
            token = parse_python__not_expression__operator(token)
        elif token.is_minus_sign:
            token = parse_python__negative_expression__operator(token)
        elif token.is_tilde_sign:
            token =  parse_python__twos_complement_expression__operator(token)
        elif token.is_star_sign:
            token = conjure_star_argument(token, parse_python__ternary_expression())
        else:
            #my_line('token: %r', token)
            raise_unknown_line()

        return conjure_body_statement(
                   header,
                   parse_python__statement_expression__atom('', token),
               )


    @share
    def parse_python__statement_else_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__else__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        j = m.end()

        keyword = evoke_indented_else_colon(m.end('indented'), m.start('colon'), j)

        wi(j)
        wj(j)

        left = parse_python_atom__normal()

        return conjure_else_fragment(keyword, parse_python__statement_expression__atom('', left))


    @share
    def parse_python__statement_else_if(m):
        return parse_python__condition_statement__X__m(
                   m,
                   conjure_keyword_else_if,
                   conjure_else_if_header,
                   conjure_else_if_fragment,
               )


    @share
    def parse_python__statement_except(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_except(m.end('indented'), j)

        wi(j)
        wj(j)

        left = parse_python__ternary_expression()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            operator = tokenize_python_operator()

        if operator.is_colon__line_marker:
            return conjure_except_header_1(indented_keyword, left, operator)

        if not operator.is_keyword_as:
            raise_unknown_line()

        right = parse_python__ternary_expression()

        operator_2 = qk()

        if operator_2 is not none:
            wk(none)
        else:
            operator_2 = tokenize_python_operator()

        if operator_2.is_colon__line_marker:
            return conjure_except_header_2(indented_keyword, left, operator, right, operator_2)

        raise_unknown_line()


    @share
    def parse_python__statement_except_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__except__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        raise_unknown_line()


    @share
    def parse_python__statement_finally_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__finally__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        raise_unknown_line()


    @share
    def parse_python__statement_for(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_for(m.end('indented'), j)

        wi(j)
        wj(j)

        left = parse_python__normal_expression_list()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            if qn() is not none:
                raise_unknown_line()

            operator = tokenize_python_operator()

            if qn() is not none:
                raise_unknown_line()

        if not operator.is_keyword_in:
            raise_unknown_line()

        right = parse_python__ternary_expression_list()

        operator_2 = qk()

        if operator_2 is not none:
            wk(none)
        else:
            if qn() is not none:
                raise_unknown_line()

            operator_2 = tokenize_python_operator()

            if qn() is not none:
                raise_unknown_line()

        if not operator_2.is_colon__line_marker:
            raise_unknown_line()

        return conjure_for_header(indented_keyword, left, operator, right, operator_2)


    @share
    def parse_python__statement_if(m):
        return parse_python__condition_statement__X__m(m, evoke_indented_if, conjure_if_header, conjure_if_statement)


    @share
    def parse_python__statement_try_colon(m):
        if m.end('newline') is not -1:
            return evoke_indented__try__colon__line_marker(m.end('indented'), m.start('colon'), m.end('colon'))

        raise_unknown_line()


    @share
    def parse_python__statement_while(m):
        return parse_python__condition_statement__X__m(m, evoke_indented_while, conjure_while_header, conjure_while_statement)


    @share
    def parse_python__statement_with(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_with(m.end('indented'), j)

        wi(j)
        wj(j)

        left = parse_python__ternary_expression()

        operator = qk()

        if operator is not none:
            wk(none)
        else:
            operator = tokenize_python_operator()

        if operator.is_colon__line_marker:
            return conjure_with_header_1(indented_keyword, left, operator)

        if not operator.is_keyword_as:
            raise_unknown_line()

        right = parse_python__normal_expression()

        operator_2 = qk()

        if operator_2 is not none:
            wk(none)
        else:
            operator_2 = tokenize_python_operator()

        if operator_2.is_colon__line_marker:
            return conjure_with_header_2(indented_keyword, left, operator, right, operator_2)

        raise_unknown_line()
