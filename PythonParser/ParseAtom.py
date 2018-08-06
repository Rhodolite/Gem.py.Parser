#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ParseAtom')
def module():
    @share
    def parse_PYTHON__map_element():
        if qk() is not none:
            #my_line('qk: %r', qk())
            raise_unknown_line()

        token = parse_PYTHON__atom__or__right_brace()

        if token.is_right_brace:
            return token

        operator = qk()

        if operator is none:
            if qn() is not none:
                raise_unknown_line()

            operator = tokenize_PYTHON_operator()
        else:
            wk(none)

        if not operator.is_colon:
            token = parse_PYTHON__ternary_expression__X__any_expression(token, operator)

            operator = qk()

            if operator is none:
                raise_unknown_line()

            wk(none)

        if not operator.is_colon:
            raise_unknown_line()

        return conjure_map_element(token, operator, parse_PYTHON__ternary_expression())


    @share
    def parse_PYTHON__map__left_brace(left_brace):
        #
        #   1
        #
        left = parse_PYTHON__map_element()

        if left.is_right_brace:
            return conjure_empty_map(left_brace, left)

        operator = qk()

        if operator is none:
            operator = tokenize_PYTHON_operator()
        else:
            wk(none)

        if operator.is_keyword_for:
            left = parse_PYTHON__comprehension_expression__X__any_expression(left, operator)

            operator = qk()

            if operator is none:
                operator = tokenize_PYTHON_operator()
            else:
                wk(none)

        if operator.is_right_brace:
            return conjure_map_expression_1(left_brace, left, operator)

        if not operator.is_CRYSTAL_comma:
            raise_unknown_line()

        token = parse_PYTHON__map_element()

        if token.is_right_brace:
            return conjure_map_expression_1(left_brace, left, conjure__comma__right_brace(operator, token))

        many       = [left, token]
        many_frill = [operator]

        while 7 is 7:
            operator = qk()

            if operator is none:
                raise_unknown_line()

            wk(none)

            if operator.is_right_brace:
                return conjure_map_expression_many(left_brace, many, many_frill, operator)

            if not operator.is_CRYSTAL_comma:
                raise_unknown_line()

            token = parse_PYTHON__map_element()

            if token.is_right_brace:
                return conjure_map_expression_many(
                           left_brace,
                           many,
                           many_frill,
                           conjure__comma__right_brace(operator, token),
                       )

            many_frill.append(operator)
            many.append(token)


    @share
    def parse_PYTHON__list_expression__left_square_bracket(left_square_bracket):
        #
        #   1
        #
        middle_1 = parse_PYTHON__atom__or__right_square_bracket()

        if middle_1.is_right_square_bracket:
            return conjure_empty_list(left_square_bracket, middle_1)

        operator_1 = tokenize_PYTHON_operator()

        if not operator_1.is_end_of_comprehension_expression:
            middle_1 = parse_PYTHON__comprehension_expression__X__any_expression(middle_1, operator_1)

            operator_1 = qk()
            wk(none)

        if operator_1.is__optional_comma__right_square_bracket:
            return conjure_list_expression_1(left_square_bracket, middle_1, operator_1)

        if not operator_1.is_CRYSTAL_comma:
            #my_line('line: %d; middle_1: %r; operator_1: %r', ql(), middle_1, operator_1)
            raise_unknown_line()

        #
        #   2
        #
        middle_2 = parse_PYTHON__atom__or__right_square_bracket()

        if middle_2.is_right_square_bracket:
            return conjure_list_expression_1(
                       left_square_bracket,
                       middle_1,
                       conjure_comma__right_square_bracket(operator_1, middle_2),
                   )

        operator_2 = tokenize_PYTHON_operator()

        if not operator_2.is_end_of_ternary_expression:
            middle_2 = parse_PYTHON__ternary_expression__X__any_expression(middle_2, operator_2)

            operator_2 = qk()
            wk(none)

        if operator_2.is__optional_comma__right_square_bracket:
            return conjure_list_expression_2(left_square_bracket, middle_1, operator_1, middle_2, operator_2)

        if not operator_2.is_CRYSTAL_comma:
            raise_unknown_line()

        #
        #   3
        #
        middle_3 = parse_PYTHON__atom__or__right_square_bracket()

        if middle_3.is_right_square_bracket:
            return conjure_list_expression_2(
                       left_square_bracket,
                       middle_1,
                       operator_1,
                       middle_2,
                       conjure_comma__right_square_bracket(operator_2, middle_3),
                   )

        many       = [middle_1, middle_2]
        many_frill = [operator_1, operator_2]

        while 7 is 7:
            operator_7 = tokenize_PYTHON_operator()

            if not operator_7.is_end_of_ternary_expression:
                middle_3 = parse_PYTHON__ternary_expression__X__any_expression(middle_3, operator_7)

                operator_7 = qk()
                wk(none)

            many.append(middle_3)

            if operator_7.is__optional_comma__right_square_bracket:
                return conjure_list_expression_many(left_square_bracket, many, many_frill, operator_7)

            if not operator_7.is_CRYSTAL_comma:
                raise_unknown_line()

            middle_3 = parse_PYTHON__atom__or__right_square_bracket()

            if middle_3.is_right_square_bracket:
                return conjure_list_expression_many(
                           left_square_bracket,
                           many,
                           many_frill,
                           conjure_comma__right_square_bracket(operator_7, middle_3),
                       )

            many_frill.append(operator_7)


    def parse_PYTHON_atom__X__token(token):
        if token.is_CRYSTAL_left_parenthesis:
            return parse_PYTHON__parenthesized_expression__left_parenthesis(token)

        if token.is_left_square_bracket:
            return parse_PYTHON__list_expression__left_square_bracket(token)

        if token.is_left_brace:
            return parse_PYTHON__map__left_brace(token)

        if token.is_keyword_not:
            return parse_PYTHON__not_expression__operator(token)

        if token.is_minus_sign:
            return parse_PYTHON__negative_expression__operator(token)

        if token.is_tilde_sign:
            return parse_PYTHON__twos_complement_expression__operator(token)

        if token.is_star_sign:
            return conjure_star_argument(token, parse_PYTHON__ternary_expression())

        #my_line('token: %r', token)
        raise_unknown_line()


    @share
    def parse_PYTHON_atom__normal():
        assert qk() is none
        assert qn() is none

        m = PYTHON_atom_match(qs(), qj())

        if m is none:
            #my_line('full: %r; s: %r', portray_string(qs()), portray_string(qs()[qj() :]))
            raise_unknown_line()

        token = analyze_PYTHON_atom(m)

        if token.is_CRYSTAL_atom:
            return token

        return parse_PYTHON_atom__X__token(token)


    @share
    def parse_PYTHON__atom__or__colon():
        assert qk() is none
        assert qn() is none

        m = PYTHON_atom_match(qs(), qj())

        if m is none:
            raise_unknown_line()

        token = analyze_PYTHON_atom(m)

        if token.is_CRYSTAL_simple_atom__or__colon:
            return token

        return parse_PYTHON_atom__X__token(token)


    def parse_PYTHON__atom__or__right_brace():
        assert qk() is none
        assert qn() is none

        m = PYTHON_atom_match(qs(), qj())

        if m is none:
            raise_unknown_line()

        token = analyze_PYTHON_atom(m)

        if token.is_CRYSTAL_simple_atom__or__right_brace:
            return token

        return parse_PYTHON_atom__X__token(token)


    @share
    def parse_PYTHON__atom__or__right_parenthesis():
        assert qk() is none
        assert qn() is none

        m = PYTHON_atom_match(qs(), qj())

        if m is none:
            raise_unknown_line()

        token = analyze_PYTHON_atom(m)

        if token.is_CRYSTAL_simple_atom__or__right_parenthesis:
            return token

        return parse_PYTHON_atom__X__token(token)


    @share
    def parse_PYTHON__atom__or__right_square_bracket():
        assert qk() is none
        assert qn() is none

        m = PYTHON_atom_match(qs(), qj())

        if m is none:
            raise_unknown_line()

        token = analyze_PYTHON_atom(m)

        if token.is_CRYSTAL_simple_atom__or__right_square_bracket:
            return token

        return parse_PYTHON_atom__X__token(token)


    parse_PYTHON__parenthesized_expression__left_parenthesis = produce_parse_LANGUAGE__bookcase_expression__LEFT_OPERATOR(
            'parse_PYTHON__parenthesized_expression__left_parenthesis', #   name
            conjure_CRYSTAL_parenthesized_expression,                   #   conjure_LANGUAGE_bookcase_expression_1
            conjure_tuple_expression_2,                                 #   conjure_LANGUAGE_bookcase_expression_2
            conjure_parenthesized_tuple_expression_1,                   #   conjure_LANGUAGE_bookcase_expression_comma_1
            conjure_tuple_expression_many,                              #   conjure_LANGUAGE_bookcase_expression_many
            conjure_comma__right_parenthesis,                           #   conjure_LANGUAGE_dual_token
            conjure_empty_tuple,                                        #   conjure_LANGUAGE_EMPTY_PAIR
            'is_end_of_ternary_expression',                             #   name__is_end_of_LANGUAGE_MIDDLE_expression
            'is_comma__right_parenthesis',                              #   name__is_LANGUAGE__comma__RIGHT_OPERATOR
            'is__optional_comma__right_parenthesis',                    #   name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR
            'is_CRYSTAL_right_parenthesis',                             #   name__is_LANGUAGE_RIGHT_OPERATOR
            0,                                                          #   parse_LANGUAGE__atom__normal
            parse_PYTHON__atom__or__right_parenthesis,                  #   parse_LANGUAGE__atom__or__RIGHT_OPERATOR
            parse_PYTHON__ternary_expression__X__any_expression,        #   parse_LANGUAGE__MIDDLE_expression__X__any_expression
            tokenize_PYTHON_operator,                                   #   tokenize_LANGUAGE_operator
        )
