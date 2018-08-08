#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ParseAtom')
def module():
    def parse_PYTHON__first_list_expression__or__right_square_bracket():
        atom_or_token = parse_PYTHON__atom__or__right_square_bracket()

        if atom_or_token.is_right_square_bracket:
            return atom_or_token

        operator = qk()

        if operator is 0:
            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_comprehension_expression:
                wk(operator)
                return atom_or_token
        else:
            if operator.is_end_of_comprehension_expression:
                return atom_or_token

            wk0()

        return parse_PYTHON__comprehension_expression__X__any_expression(atom_or_token, operator)


    def parse_PYTHON__middle_list_expression__or__right_square_bracket():
        atom_or_token = parse_PYTHON__atom__or__right_square_bracket()

        if atom_or_token.is_right_square_bracket:
            return atom_or_token

        operator = qk()

        if operator is 0:
            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_ternary_expression:
                wk(operator)
                return atom_or_token
        else:
            if operator.is_end_of_ternary_expression:
                return atom_or_token

            wk0()

        return parse_PYTHON__ternary_expression__X__any_expression(atom_or_token, operator)


    def parse_PYTHON__first_parenthesized_expression__or__right_parenthesis():
        atom_or_token = parse_PYTHON__atom__or__right_parenthesis()

        if atom_or_token.is_right_parenthesis:
            return atom_or_token

        operator = qk()

        if operator is 0:
            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_comprehension_expression:
                wk(operator)
                return atom_or_token
        else:
            if operator.is_end_of_comprehension_expression:
                return atom_or_token

            wk0()

        return parse_PYTHON__comprehension_expression__X__any_expression(atom_or_token, operator)


    def parse_PYTHON__middle_parenthesized_expression__or__right_parenthesis():
        atom_or_token = parse_PYTHON__atom__or__right_parenthesis()

        if atom_or_token.is_right_parenthesis:
            return atom_or_token

        operator = qk()

        if operator is 0:
            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_ternary_expression:
                wk(operator)
                return atom_or_token
        else:
            if operator.is_end_of_ternary_expression:
                return atom_or_token

            wk0()

        return parse_PYTHON__ternary_expression__X__any_expression(atom_or_token, operator)


    def parse_PYTHON__first_map_element__or__right_brace():
        map_element__or__token = parse_PYTHON__middle_map_element__or__right_brace()

        if map_element__or__token.is_right_brace:
            return map_element__or__token

        operator = qk()

        if not operator.is_keyword_for:
            return map_element__or__token

        wk0()

        return parse_PYTHON__comprehension_expression__left_operator(map_element__or__token, operator)


    def parse_PYTHON__middle_map_element__or__right_brace():
        assert qk() is 0

        if qn() is not 0:
            raise_unknown_line()

        #
        #<python atom or right brace + operator>
        #
        m = PYTHON_atom_match(qs(), qj())

        if m is none:
            raise_unknown_line()

        atom_or_token = analyze_PYTHON_atom(m)

        if atom_or_token.is_CRYSTAL_simple_atom__or__right_brace:
            if atom_or_token.is_right_brace:
                return atom_or_token

            operator = tokenize_PYTHON_operator()
        else:
            atom_or_token = parse_PYTHON_atom__X__token(atom_or_token)

            operator = qk()

            if operator is 0:
                operator = tokenize_PYTHON_operator()
            else:
                wk0()
        #</>

        if not operator.is_colon:
            atom_or_token = parse_PYTHON__ternary_expression__X__any_expression(atom_or_token, operator)

            operator = qk()

            if operator is 0:
                raise_unknown_line()

            wk0()

        if not operator.is_colon:
            raise_unknown_line()

        return conjure_map_element(atom_or_token, operator, parse_PYTHON__ternary_expression())


    def parse_PYTHON_atom__X__token(token):
        if token.is_left_parenthesis:
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
        assert qk() is 0

        if qn() is not 0:
            raise_unknown_line()

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
        assert qk() is 0

        if qn() is not 0:
            raise_unknown_line()

        m = PYTHON_atom_match(qs(), qj())

        if m is none:
            raise_unknown_line()

        token = analyze_PYTHON_atom(m)

        if token.is_CRYSTAL_simple_atom__or__colon:
            return token

        return parse_PYTHON_atom__X__token(token)


    @share
    def parse_PYTHON__atom__or__right_parenthesis():
        assert qk() is 0

        if qn() is not 0:
            raise_unknown_line()

        m = PYTHON_atom_match(qs(), qj())

        if m is none:
            raise_unknown_line()

        token = analyze_PYTHON_atom(m)

        if token.is_CRYSTAL_simple_atom__or__right_parenthesis:
            return token

        return parse_PYTHON_atom__X__token(token)


    @share
    def parse_PYTHON__atom__or__right_square_bracket():
        assert qk() is 0

        if qn() is not 0:
            raise_unknown_line()

        m = PYTHON_atom_match(qs(), qj())

        if m is none:
            raise_unknown_line()

        token = analyze_PYTHON_atom(m)

        if token.is_CRYSTAL_simple_atom__or__right_square_bracket:
            return token

        return parse_PYTHON_atom__X__token(token)


    #
    #   NOTE:
    #       `conjure_map_expression_1` is *BOTH* `conjure_LANGUAGE_bookcase_expression{,_comma}_1` on purpose.
    #
    parse_PYTHON__map__left_brace = produce_parse_LANGUAGE__bookcase_expression(
            'PYTHON',                                           #   language
            'map',                                              #   name
            'left_brace',                                       #   LEFT_OPERATOR
            conjure_map_expression_1,                           #   conjure_LANGUAGE_bookcase_expression_1
            0,                                                  #   conjure_LANGUAGE_bookcase_expression_2
            conjure_map_expression_1,                           #   conjure_LANGUAGE_bookcase_expression_comma_1
            conjure_map_expression_many,                        #   conjure_LANGUAGE_bookcase_expression_many
            conjure__comma__right_brace,                        #   conjure_LANGUAGE_dual_token
            conjure_empty_map,                                  #   conjure_LANGUAGE_EMPTY_PAIR
            0,                                                  #   name__is_LANGUAGE__comma__RIGHT_OPERATOR
            'is__optional_comma__right_brace',                  #   name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR
            'is_right_brace',                                   #   name__is_LANGUAGE_RIGHT_OPERATOR
            0,                                                  #   parse_LANGUAGE__FIRST_expression

            #
            #   parse_LANGUAGE__FIRST_expression__or__RIGHT_OPERATOR
            #
            parse_PYTHON__first_map_element__or__right_brace,

            #
            #   parse_LANGUAGE__MIDDLE_expression__or__RIGHT_OPERATOR
            #
            parse_PYTHON__middle_map_element__or__right_brace,
        )

    #
    #   NOTE:
    #       `conjure_list_expression_1` is *BOTH* `conjure_LANGUAGE_bookcase_expression{,_comma}_1` on purpose.
    #
    parse_PYTHON__list_expression__left_square_bracket = produce_parse_LANGUAGE__bookcase_expression(
            'PYTHON',                                           #   language
            'list_expression',                                  #   name
            'left_square_bracket',                              #   LEFT_OPERATOR
            conjure_list_expression_1,                          #   conjure_LANGUAGE_bookcase_expression_1
            conjure_list_expression_2,                          #   conjure_LANGUAGE_bookcase_expression_2
            conjure_list_expression_1,                          #   conjure_LANGUAGE_bookcase_expression_comma_1
            conjure_list_expression_many,                       #   conjure_LANGUAGE_bookcase_expression_many
            conjure_comma__right_square_bracket,                #   conjure_LANGUAGE_dual_token
            conjure_empty_list,                                 #   conjure_LANGUAGE_EMPTY_PAIR
            0,                                                  #   name__is_LANGUAGE__comma__RIGHT_OPERATOR
            'is__optional_comma__right_square_bracket',         #   name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR
            'is_right_square_bracket',                          #   name__is_LANGUAGE_RIGHT_OPERATOR
            0,                                                  #   parse_LANGUAGE__FIRST_expression

            #
            #   parse_LANGUAGE__FIRST_expression__or__RIGHT_OPERATOR
            #
            parse_PYTHON__first_list_expression__or__right_square_bracket,

            #
            #   parse_LANGUAGE__MIDDLE_expression__or__RIGHT_OPERATOR
            #
            parse_PYTHON__middle_list_expression__or__right_square_bracket,
        )

    #
    #   NOTE:
    #       `parse_PYTHON__ternary_expression__X__any_expression` is *BOTH*
    #       `parse_LANGUAGE__{FIRST,MIDDLE}_expression__X__any_expression{,_comma}_1` on purpose.
    #
    parse_PYTHON__parenthesized_expression__left_parenthesis = produce_parse_LANGUAGE__bookcase_expression(
            'PYTHON',                                           #   langauge
            'parenthesized_expression',                         #   name
            'left_parenthesis',                                 #   LEFT_OPERATOR
            conjure_CRYSTAL_parenthesized_expression,           #   conjure_LANGUAGE_bookcase_expression_1
            conjure_tuple_expression_2,                         #   conjure_LANGUAGE_bookcase_expression_2
            conjure_parenthesized_tuple_expression_1,           #   conjure_LANGUAGE_bookcase_expression_comma_1
            conjure_tuple_expression_many,                      #   conjure_LANGUAGE_bookcase_expression_many
            conjure_comma__right_parenthesis,                   #   conjure_LANGUAGE_dual_token
            conjure_empty_tuple,                                #   conjure_LANGUAGE_EMPTY_PAIR
            'is_comma__right_parenthesis',                      #   name__is_LANGUAGE__comma__RIGHT_OPERATOR
            'is__optional_comma__right_parenthesis',            #   name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR
            'is_right_parenthesis',                             #   name__is_LANGUAGE_RIGHT_OPERATOR
            0,                                                  #   parse_LANGUAGE__FIRST_expression

            #
            #   parse_LANGUAGE__FIRST_expression__or__RIGHT_OPERATOR
            #
            parse_PYTHON__first_parenthesized_expression__or__right_parenthesis,

            #
            #   parse_LANGUAGE__MIDDLE_expression__or__RIGHT_OPERATOR
            #
            parse_PYTHON__middle_parenthesized_expression__or__right_parenthesis,
        )


    #
    #   export
    #
    export(
        'parse_PYTHON__list_expression__left_square_bracket',   parse_PYTHON__list_expression__left_square_bracket,

        'parse_PYTHON__parenthesized_expression__left_parenthesis',
            parse_PYTHON__parenthesized_expression__left_parenthesis,
    )
