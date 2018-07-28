#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Parse1Atom')
def module():
    show = 7


    @share
    def parse1_map_element():
        if qk() is not none:
            #my_line('qk: %r', qk())
            raise_unknown_line()

        token = parse1_atom()

        if token.is_right_brace:
            return token

        if token.is_special_operator:
            raise_unknown_line()

        operator = qk()

        if operator is none:
            if qn() is not none:
                raise_unknown_line()

            operator = tokenize_operator()
        else:
            wk(none)

        if not operator.is_colon:
            token = parse1_ternary_expression__X__any_expression(token, operator)

            operator = qk()

            if operator is none:
                raise_unknown_line()

            wk(none)

        if not operator.is_colon:
            raise_unknown_line()

        return conjure_map_element(token, operator, parse1_ternary_expression())


    @share
    def parse1_map__left_brace(left_brace):
        #
        #   1
        #
        left = parse1_map_element()

        if left.is_right_brace:
            return conjure_empty_map(left_brace, left)

        operator = qk()

        if operator is none:
            operator = tokenize_operator()
        else:
            wk(none)

        if operator.is_keyword_for:
            left = parse1_comprehension_expression__X__any_expression(left, operator)

            operator = qk()

            if operator is none:
                operator = tokenize_operator()
            else:
                wk(none)

        if operator.is_right_brace:
            return conjure_map_expression_1(left_brace, left, operator)

        if not operator.is_comma:
            raise_unknown_line()

        token = parse1_map_element()

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

            if not operator.is_comma:
                raise_unknown_line()

            token = parse1_map_element()

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
    def parse1__parenthesized_expression__left_parenthesis(left_parenthesis):
        #
        #   1
        #

        #
        #   TODO:
        #       Replace this with 'parse1__parenthesis__first_atom' & handle a right-parenthesis as an empty tuple
        #
        middle_1 = parse1_atom()

        if middle_1.is_right_parenthesis:
            return conjure_empty_tuple(left_parenthesis, middle_1)

        if middle_1.is_special_operator:
            raise_unknown_line()

        operator_1 = qk()

        if operator_1 is none:
            operator_1 = tokenize_operator()
        else:
            wk(none)

        #my_line('operator_1: %r', operator_1)

        if not operator_1.is_end_of_ternary_expression:
            middle_1 = parse1_ternary_expression__X__any_expression(middle_1, operator_1)

            operator_1 = qk()
            wk(none)

        if operator_1.is_right_parenthesis:
            return conjure_parenthesized_expression(left_parenthesis, middle_1, operator_1)

        if operator_1.is_comma__right_parenthesis:
            return conjure_parenthesized_tuple_expression_1(left_parenthesis, middle_1, operator_1)

        if not operator_1.is_comma:
            raise_unknown_line()

        #
        #   2
        #
        middle_2 = parse1_atom()

        if middle_2.is_right_parenthesis:
            return conjure_parenthesized_tuple_expression_1(
                       left_parenthesis,
                       middle_1,
                       conjure_comma__right_parenthesis(operator_1, middle_2),
                   )

        if middle_2.is_special_operator:
            raise_unknown_line()

        operator_2 = tokenize_operator()

        if not operator_2.is_end_of_ternary_expression:
            middle_2 = parse1_ternary_expression__X__any_expression(middle_2, operator_2)

            operator_2 = qk()
            wk(none)

        if operator_2.is__optional_comma__right_parenthesis:
            return conjure_tuple_expression_2(left_parenthesis, middle_1, operator_1, middle_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line()

        #
        #   3
        #
        middle_3 = parse1_atom()

        if middle_3.is_right_parenthesis:
            return conjure_tuple_expression_2(
                       left_parenthesis,
                       middle_1,
                       operator_1,
                       middle_2,
                       conjure_comma__right_parenthesis(operator_2, middle_3),
                   )

        if middle_3.is_special_operator:
            raise_unknown_line()

        many       = [middle_1, middle_2]
        many_frill = [operator_1, operator_2]

        while 7 is 7:
            operator_7 = tokenize_operator()

            if not operator_7.is_end_of_ternary_expression:
                middle_3 = parse1_ternary_expression__X__any_expression(middle_3, operator_7)

                operator_7 = qk()
                wk(none)

            many.append(middle_3)

            if operator_7.is__optional_comma__right_parenthesis:
                return conjure_tuple_expression_many(left_parenthesis, many, many_frill, operator_7)

            if not operator_7.is_comma:
                raise_unknown_line()

            middle_3 = parse1_atom()

            if middle_3.is_right_parenthesis:
                return conjure_tuple_expression_many(
                           left_parenthesis,
                           many,
                           many_frill,
                           conjure_comma__right_parenthesis(operator_7, middle_3),
                       )

            if middle_3.is_special_operator:
                raise_unknown_line()

            many_frill.append(operator_7)


    @share
    def parse1__list_expression__left_square_bracket(left_square_bracket):
        #
        #   1
        #
        middle_1 = parse1_atom()

        if middle_1.is_right_square_bracket:
            return conjure_empty_list(left_square_bracket, middle_1)

        if middle_1.is_special_operator:
            raise_unknown_line()

        operator_1 = tokenize_operator()

        if not operator_1.is_end_of_comprehension_expression:
            middle_1 = parse1_comprehension_expression__X__any_expression(middle_1, operator_1)

            operator_1 = qk()
            wk(none)

        if operator_1.is__optional_comma__right_square_bracket:
            return conjure_list_expression_1(left_square_bracket, middle_1, operator_1)

        if not operator_1.is_comma:
            #my_line('line: %d; middle_1: %r; operator_1: %r', ql(), middle_1, operator_1)
            raise_unknown_line()

        #
        #   2
        #
        middle_2 = parse1_atom()

        if middle_2.is_right_square_bracket:
            return conjure_list_expression_1(
                       left_square_bracket,
                       middle_1,
                       conjure_comma__right_square_bracket(operator_1, middle_2),
                   )

        if middle_2.is_special_operator:
            raise_unknown_line()

        operator_2 = tokenize_operator()

        if not operator_2.is_end_of_ternary_expression:
            middle_2 = parse1_ternary_expression__X__any_expression(middle_2, operator_2)

            operator_2 = qk()
            wk(none)

        if operator_2.is__optional_comma__right_square_bracket:
            return conjure_list_expression_2(left_square_bracket, middle_1, operator_1, middle_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line()

        #
        #   3
        #
        middle_3 = parse1_atom()

        if middle_3.is_right_square_bracket:
            return conjure_list_expression_2(
                       left_square_bracket,
                       middle_1,
                       operator_1,
                       middle_2,
                       conjure_comma__right_square_bracket(operator_2, middle_3),
                   )

        if middle_3.is_special_operator:
            raise_unknown_line()

        many       = [middle_1, middle_2]
        many_frill = [operator_1, operator_2]

        while 7 is 7:
            operator_7 = tokenize_operator()

            if not operator_7.is_end_of_ternary_expression:
                middle_3 = parse1_ternary_expression__X__any_expression(middle_3, operator_7)

                operator_7 = qk()
                wk(none)

            many.append(middle_3)

            if operator_7.is__optional_comma__right_square_bracket:
                return conjure_list_expression_many(left_square_bracket, many, many_frill, operator_7)

            if not operator_7.is_comma:
                raise_unknown_line()

            middle_3 = parse1_atom()

            if middle_3.is_right_square_bracket:
                return conjure_list_expression_many(
                           left_square_bracket,
                           many,
                           many_frill,
                           conjure_comma__right_square_bracket(operator_7, middle_3),
                       )

            if middle_3.is_special_operator:
                raise_unknown_line()

            many_frill.append(operator_7)


    @share
    def parse1_atom():
        assert qk() is none
        assert qn() is none

        m = atom_match(qs(), qj())

        if m is none:
            #my_line('full: %r; s: %r', portray_string(qs()), portray_string(qs()[qj() :]))
            raise_unknown_line()

        token = analyze_atom(m)

        if token.is__atom__or__special_operator:
            return token

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

        my_line('token: %r', token)
        assert 0
        raise_unknown_line()
