#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.Parse1Function')
def gem():
    require_gem('PythonParser.BookcaseDualStatement')
    require_gem('PythonParser.DefinitionHeader')


    @share
    def parse1_statement_class_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_class(m.end('indented'), j)

        wi(j)
        wj(j)

        name = tokenize_name()

        if qn() is not none:
            raise_unknown_line()

        operator = tokenize_operator()

        if not operator.is__arguments_0__or__left_parenthesis:
            raise_unknown_line()

        if operator.is_left_parenthesis:
            assert qd() > 0
            assert qn() is none

            operator = parse1_arguments__left_parenthesis(operator)

        return conjure_class_header(
                   indented_keyword,
                   name,
                   operator,
                   tokenize_parameter_colon_newline(),
               )


    @share
    def parse1_statement_function_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_function(m.end('indented'), j)

        wi(j)
        wj(j)

        #
        #<name>
        #
        name = tokenize_name()

        if qn() is not none:
            raise_unknown_line()
        #</name>

        operator_1 = tokenize_header_parenthesis_atom()

        if operator_1.is_parameters_0:
            return conjure_function_header(indented_keyword, name, operator_1, tokenize_parameter_colon_newline())

        if not operator_1.is_left_parenthesis:
            raise_unknown_line()

        #
        #<parameter_1>
        #
        token_1 = tokenize_parameter_atom()

        if qn() is not none:
            raise_unknown_line()
        #</parameter_1>

        if token_1.is_right_parenthesis:
            return conjure_function_header(
                       indented_keyword,
                       name,
                       conjure_parameters_0(operator_1, token_1),
                       tokenize_parameter_colon_newline(),
                   )

        if token_1.is_special_operator:
            raise_unknown_line()

        operator_2 = tokenize_parameter_operator()

        if operator_2.is_equal_sign:
            value = parse1_ternary_expression()

            token_1 = conjure_keyword_parameter(token_1, operator_2, value)

            operator_2 = qk()
            wk(none)

            if operator_2 is none:
                raise_unknown_line()

        if operator_2.is__optional_comma__right_parenthesis:
            return conjure_function_header(
                       indented_keyword,
                       name,
                       conjure_parameters_1(operator_1, token_1, operator_2),
                       tokenize_parameter_colon_newline(),
                   )

        if not operator_2.is_comma:
            #my_line('operator_2: %r', operator_2)
            raise_unknown_line()

        token_7 = tokenize_parameter_atom()

        if qn() is not none:
            raise_unknown_line()

        if token_7.is_right_parenthesis:
            return conjure_function_header(
                       indented_keyword,
                       name,
                       conjure_parameters_1(
                           operator_1,
                           token_1,
                           conjure_comma__right_parenthesis(operator_2, token_7),
                       ),
                       tokenize_parameter_colon_newline(),
                   )

        if token_7.is_special_operator:
            raise_unknown_line()

        many       = [token_1]
        many_frill = [operator_2]

        while 7 is 7:
            operator_7 = tokenize_parameter_operator()

            if operator_7.is_equal_sign:
                value = parse1_ternary_expression()

                token_7 = conjure_keyword_parameter(token_7, operator_7, value)

                operator_7 = qk()
                wk(none)

                if operator_7 is none:
                    raise_unknown_line()

            many.append(token_7)

            if operator_7.is__optional_comma__right_parenthesis:
                return conjure_function_header(
                           indented_keyword,
                           name,
                           conjure_parameters_many(operator_1, many, many_frill, operator_7),
                           tokenize_parameter_colon_newline(),
                       )

            if not operator_7.is_comma:
                #my_line('operator_7: %s; full_line: %r', operator_7, portray_string(qs()))
                raise_unknown_line()

            token_7 = tokenize_parameter_atom()

            if qn() is not none:
                raise_unknown_line()

            if token_7.is_right_parenthesis:
                return conjure_function_header(
                           indented_keyword,
                           name,
                           conjure_parameters_many(
                               operator_1,
                               many,
                               many_frill,
                               conjure_comma__right_parenthesis(operator_7, token_7),
                           ),
                           tokenize_parameter_colon_newline(),
                       )

            if token_7.is_special_operator:
                raise_unknown_line()

            many_frill.append(operator_7)
