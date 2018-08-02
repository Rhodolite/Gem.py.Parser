#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Parse1Call')
def module():
    require_module('PythonParser.BookcaseDualExpression')
    require_module('PythonParser.CallStatement')


    @share
    def parse1_call_expression__left__operator(left, left_parenthesis):
        return conjure_call_expression(left, parse1_arguments__left_parenthesis(left_parenthesis))


    @share
    def parse1_argument7__left(left):
        operator = qk()

        if operator is none:
            operator = tokenize_python_operator()
        else:
            wk(none)

        if operator.is_equal_sign:
            if not left.is_CRYSTAL_identifier:
                raise_unknown_line()

            return conjure_keyword_argument(left, operator, parse1_ternary_expression())

        if operator.is_end_of_ternary_expression:
            wk(operator)

            return left

        return parse1_ternary_expression__X__any_expression(left, operator)


    @share
    def parse1_arguments__left_parenthesis(left_parenthesis):
        argument_1 = parse1_atom()

        if argument_1.is_right_parenthesis:
            return conjure_arguments_0(left_parenthesis, argument_1)

        if argument_1.is_CRYSTAL_special_operator:
            raise_unknown_line()

        operator_1 = qk()

        if operator_1 is none:
            operator_1 = tokenize_python_operator()
        else:
            wk(none)

        if operator_1.is_equal_sign:
            if not argument_1.is_CRYSTAL_identifier:
                raise_unknown_line()

            argument_1 = conjure_keyword_argument(argument_1, operator_1, parse1_ternary_expression())

            operator_1 = qk()

            if operator_1 is none:
                operator_1 = tokenize_python_operator()
            else:
                wk(none)
        else:
            if not operator_1.is_end_of_comprehension_expression:
                argument_1 = parse1_comprehension_expression__X__any_expression(argument_1, operator_1)

                operator_1 = qk()

                if operator_1 is none:
                    operator_1 = tokenize_python_operator()
                else:
                    wk(none)

        if operator_1.is__optional_comma__right_parenthesis:
            return conjure_arguments_1(left_parenthesis, argument_1, operator_1)

        if not operator_1.is_comma:
            #my_line('operator_1: %r', operator_1)
            raise_unknown_line()

        argument_2 = parse1_atom()

        if argument_2.is_right_parenthesis:
            return conjure_arguments_1(
                       left_parenthesis,
                       argument_1,
                       conjure_comma__right_parenthesis(operator_1, argument_2),
                   )

        if argument_2.is_CRYSTAL_special_operator:
            raise_unknown_line()

        argument_2 = parse1_argument7__left(argument_2)
        operator_2 = qk()

        wk(none)

        if operator_2.is__optional_comma__right_parenthesis:
            return conjure_arguments_2(left_parenthesis, argument_1, operator_1, argument_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line()

        argument_3 = parse1_atom()

        if argument_3.is_right_parenthesis:
            return conjure_arguments_2(
                       left_parenthesis,
                       argument_1,
                       operator_1,
                       argument_2,
                       conjure_comma__right_parenthesis(operator_2, argument_3),
                   )

        if argument_3.is_CRYSTAL_special_operator:
            raise_unknown_line()

        frill_many = [operator_1, operator_2]
        many       = [argument_1, argument_2]

        while 7 is 7:
            many.append(parse1_argument7__left(argument_3))

            operator_7 = qk()

            wk(none)

            if operator_7.is__optional_comma__right_parenthesis:
                return conjure_arguments_many(left_parenthesis, many, frill_many, operator_7)

            if not operator_7.is_comma:
                raise_unknown_line()

            argument_3 = parse1_atom()

            if argument_3.is_right_parenthesis:
                return conjure_arguments_many(
                           left_parenthesis,
                           many,
                           frill_many,
                           conjure_comma__right_parenthesis(operator_7, argument_3),
                       )

            if argument_3.is_CRYSTAL_special_operator:
                raise_unknown_line()

            frill_many.append(operator_7)
