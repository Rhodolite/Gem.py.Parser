#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ParseCall')
def module():
    require_module('PythonParser.BookcaseDualExpression')
    require_module('PythonParser.CallStatement')


    @share
    def parse_python__call_expression__left__operator(left, left_parenthesis):
        return conjure_call_expression(left, parse_python__arguments__left_parenthesis(left_parenthesis))


    @share
    def parse_python__argument7__left(left):
        operator = qk()

        if operator is none:
            operator = tokenize_python_operator()
        else:
            wk(none)

        if operator.is_equal_sign:
            if not left.is_CRYSTAL_identifier:
                raise_unknown_line()

            return conjure_keyword_argument(left, operator, parse_python__ternary_expression())

        if operator.is_end_of_ternary_expression:
            wk(operator)

            return left

        return parse_python__ternary_expression__X__any_expression(left, operator)


    @share
    def parse_python__arguments__left_parenthesis(left_parenthesis):
        argument_1 = parse_python__atom__or__right_parenthesis()

        if argument_1.is_CRYSTAL_right_parenthesis:
            return conjure_arguments_0(left_parenthesis, argument_1)

        operator_1 = qk()

        if operator_1 is none:
            operator_1 = tokenize_python_operator()
        else:
            wk(none)

        if operator_1.is_equal_sign:
            if not argument_1.is_CRYSTAL_identifier:
                raise_unknown_line()

            argument_1 = conjure_keyword_argument(argument_1, operator_1, parse_python__ternary_expression())

            operator_1 = qk()

            if operator_1 is none:
                operator_1 = tokenize_python_operator()
            else:
                wk(none)
        else:
            if not operator_1.is_end_of_comprehension_expression:
                argument_1 = parse_python__comprehension_expression__X__any_expression(argument_1, operator_1)

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

        argument_2 = parse_python__atom__or__right_parenthesis()

        if argument_2.is_CRYSTAL_right_parenthesis:
            return conjure_arguments_1(
                       left_parenthesis,
                       argument_1,
                       conjure_comma__right_parenthesis(operator_1, argument_2),
                   )

        argument_2 = parse_python__argument7__left(argument_2)
        operator_2 = qk()

        wk(none)

        if operator_2.is__optional_comma__right_parenthesis:
            return conjure_arguments_2(left_parenthesis, argument_1, operator_1, argument_2, operator_2)

        if not operator_2.is_comma:
            raise_unknown_line()

        argument_3 = parse_python__atom__or__right_parenthesis()

        if argument_3.is_CRYSTAL_right_parenthesis:
            return conjure_arguments_2(
                       left_parenthesis,
                       argument_1,
                       operator_1,
                       argument_2,
                       conjure_comma__right_parenthesis(operator_2, argument_3),
                   )

        frill_many = [operator_1, operator_2]
        many       = [argument_1, argument_2]

        while 7 is 7:
            many.append(parse_python__argument7__left(argument_3))

            operator_7 = qk()

            wk(none)

            if operator_7.is__optional_comma__right_parenthesis:
                return conjure_arguments_many(left_parenthesis, many, frill_many, operator_7)

            if not operator_7.is_comma:
                raise_unknown_line()

            argument_3 = parse_python__atom__or__right_parenthesis()

            if argument_3.is_CRYSTAL_right_parenthesis:
                return conjure_arguments_many(
                           left_parenthesis,
                           many,
                           frill_many,
                           conjure_comma__right_parenthesis(operator_7, argument_3),
                       )

            frill_many.append(operator_7)
