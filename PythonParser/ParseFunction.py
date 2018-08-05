#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ParseFunction')
def module():
    require_module('PythonParser.DefinitionHeader')
    require_module('PythonParser.DualExpressionStatement')


    @share
    def parse_PYTHON__statement_class_header(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_class(m.end('indented'), j)

        wi(j)
        wj(j)

        name = tokenize_name()

        if qn() is not none:
            raise_unknown_line()

        operator = tokenize_PYTHON_operator()

        if not operator.is__arguments_0__or__left_parenthesis:
            raise_unknown_line()

        if operator.is_CRYSTAL_left_parenthesis:
            assert qd() > 0
            assert qn() is none

            operator = parse_PYTHON__arguments__left_parenthesis(operator)

        return conjure_class_header(
                   indented_keyword,
                   name,
                   operator,
                   tokenize_parameter_colon_newline(),
               )


    @share
    def parse_PYTHON__statement_function_header(m):
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

        if not operator_1.is_CRYSTAL_left_parenthesis:
            raise_unknown_line()

        #
        #<parameter_1>
        #
        token_1 = tokenize_parameter_atom()

        if qn() is not none:
            raise_unknown_line()
        #</parameter_1>

        if token_1.is_CRYSTAL_right_parenthesis:
            return conjure_function_header(
                       indented_keyword,
                       name,
                       conjure_parameters_0(operator_1, token_1),
                       tokenize_parameter_colon_newline(),
                   )

        assert token_1.is_PYTHON__identifier__or__star_parameter

        operator_2 = tokenize_parameter_operator()

        if operator_2.is_equal_sign:
            value = parse_PYTHON__ternary_expression()

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

        if not operator_2.is_CRYSTAL_comma:
            #my_line('operator_2: %r', operator_2)
            raise_unknown_line()

        token_7 = tokenize_parameter_atom()

        if qn() is not none:
            raise_unknown_line()

        if token_7.is_CRYSTAL_right_parenthesis:
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

        assert token_7.is_PYTHON__identifier__or__star_parameter

        many       = [token_1]
        many_frill = [operator_2]

        while 7 is 7:
            operator_7 = tokenize_parameter_operator()

            if operator_7.is_equal_sign:
                value = parse_PYTHON__ternary_expression()

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

            if not operator_7.is_CRYSTAL_comma:
                #my_line('operator_7: %s; full_line: %r', operator_7, portray_string(qs()))
                raise_unknown_line()

            token_7 = tokenize_parameter_atom()

            if qn() is not none:
                raise_unknown_line()

            if token_7.is_CRYSTAL_right_parenthesis:
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

            assert token_7.is_PYTHON__identifier__or__star_parameter

            many_frill.append(operator_7)
