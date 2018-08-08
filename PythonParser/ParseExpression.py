#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ParseExpression')
def module():
    require_module('PythonParser.ManyExpression')
    require_module('PythonParser.TernaryExpression')
    require_module('PythonParser.UnaryExpression')


    #
    #   3.  Postfix-Expression (Python 2.7.14rc1 grammer calls this 'trailer')
    #
    #       postfix-expression
    #           : atom
    #           | dot-expression
    #           | call-expression
    #           | method-call-expression
    #           | index-expression
    #
    #       dot-expression
    #           : postfix-expression '.' name
    #
    #       call-expression
    #           : postfix-expression '(' ] ')'
    #           : postfix-expression '(' argument-list ')'
    #
    #       method-call-expression
    #           : postfix-expression '.' name '(' ')'
    #           | postfix-expression '.' name '(' argument-list ')'
    #
    #       index-expression
    #           : postfix-expression '[' ']'
    #           | postfix-expression '[' subscript-list ']'
    #
    #       subscript-list
    #           : subscript
    #           | subscript-list ',' subscript
    #
    #       subscript
    #           : '.' '.' '.'
    #           | ternary-expression
    #           | ternary-expression ':'
    #           | ':' ternary-expression
    #           | [ternary-expression] ':' [ternary-expression] ':' [ternary-expression]
    #
    @share
    def parse_PYTHON__postfix_expression__left_operator(left, operator, indentation = 0):
        assert operator.is_postfix_operator

        while 7 is 7:
            assert qk() is 0

            if operator.is_dot:
                name = tokenize_name()

                if qn() is not 0:
                    return conjure_member_expression(left, conjure_dot_name(operator, name))

                operator_2 = tokenize_PYTHON_operator()

                if operator_2.is_dot:
                    if qn() is not 0:
                        raise_unknown_line()

                    name_2 = tokenize_name()

                    if qn() is not 0:
                        return conjure_member_expression(
                                   left,
                                   conjure_dot_name_pair(
                                       conjure_dot_name(operator,   name),
                                       conjure_dot_name(operator_2, name_2),
                                   ),
                               )

                    operator_3 = tokenize_PYTHON_operator()

                    if operator_3.is_dot:
                        if qn() is not 0:
                            raise_unknown_line()

                        name_3 = tokenize_name()

                        if qn() is not 0:
                            return conjure_member_expression(
                                       left,
                                       conjure_dot_name_triplet__with_newlines(
                                           conjure_dot_name(operator,   name),
                                           conjure_dot_name(operator_2, name_2),
                                           conjure_dot_name(operator_3, name_3),
                                       ),
                                   )

                        operator_4 = tokenize_PYTHON_operator()

                        if operator_4.is_dot:
                            if qn() is not 0:
                                raise_unknown_line()

                            name_4 = tokenize_name()

                            left = conjure_member_expression(
                                       left,
                                       conjure_dot_name_quadruplet(
                                           conjure_dot_name(operator,   name),
                                           conjure_dot_name(operator_2, name_2),
                                           conjure_dot_name(operator_3, name_3),
                                           conjure_dot_name(operator_4, name_4),
                                       ),
                                   )

                            if qn() is not 0:
                                return left

                            operator_5 = tokenize_PYTHON_operator()

                            if not operator_5.is_postfix_operator:
                                wk(operator_5)

                                return left

                            operator = operator_5
                        else:
                            left = conjure_member_expression(
                                       left,
                                       conjure_dot_name_triplet__with_newlines(
                                           conjure_dot_name(operator,   name),
                                           conjure_dot_name(operator_2, name_2),
                                           conjure_dot_name(operator_3, name_3),
                                       ),
                                   )

                            if not operator_4.is_postfix_operator:
                                wk(operator_4)

                                return left

                            operator = operator_4

                    else:
                        left = conjure_member_expression(
                                   left,
                                   conjure_dot_name_pair(
                                       conjure_dot_name(operator,   name),
                                       conjure_dot_name(operator_2, name_2),
                                   ),
                               )

                        if not operator_3.is_postfix_operator:
                            wk(operator_3)

                            return left

                        operator = operator_3

                else:
                    left = conjure_member_expression(left, conjure_dot_name(operator, name))

                    if not operator_2.is_postfix_operator:
                        wk(operator_2)

                        return left

                    operator = operator_2

            if operator.is__arguments_0__or__left_parenthesis:
                if operator.is_left_parenthesis:
                    assert qd() > 0
                    assert qn() is 0

                    operator = parse_PYTHON__arguments__left_parenthesis(operator)

                newline = qn()

                if (indentation is not 0) and (newline is not 0) and (qk() is 0):
                    wn0()

                    return left.call_statement(conjure_vw_frill(indentation, newline), left, operator)

                left = left.call_expression(left, operator)

                operator = qk()

                if operator is not 0:
                    if not operator.is_postfix_operator:
                        return left

                    wk0()
                else:
                    if newline is not 0:
                        return left

                    operator = tokenize_PYTHON_operator()

                    if not operator.is_postfix_operator:
                        wk(operator)

                        return left

            if operator.is_left_square_bracket:
                if qn() is not 0:
                    raise_unknown_line()

                middle = parse_PYTHON__atom__or__colon()

                if middle.is_colon:
                    operator = conjure__left_square_bracket__colon(operator, middle)
                else:
                    operator_2 = qk()

                    if operator_2 is 0:
                        if qn() is not 0:
                            raise_unknown_line()

                        operator_2 = tokenize_PYTHON_operator()
                    else:
                        wk0()

                    if not operator_2.is_end_of_ternary_expression:
                        middle = parse_PYTHON__ternary_expression__X__any_expression(middle, operator_2)

                        operator_2 = qk()

                        if operator_2 is 0:
                            raise_unknown_line()

                        wk0()

                    if operator_2.is_right_square_bracket:
                        left = conjure_index_expression(left, conjure_normal_index(operator, middle, operator_2))
                    elif operator_2.is_colon:
                        if qn() is not 0:
                            raise_unknown_line()

                        middle_2 = parse_PYTHON__atom__or__right_square_bracket()

                        if middle_2.is_right_square_bracket:
                            left = conjure_index_expression(
                                       left,
                                       conjure_head_index(
                                           operator,
                                           middle,
                                           conjure__colon__right_square_bracket(operator_2, middle_2),
                                       ),
                                   )
                        else:
                            operator_3 = qk()

                            if operator_3 is 0:
                                if qn() is not 0:
                                    raise_unknown_line()

                                operator_3 = tokenize_PYTHON_operator()
                            else:
                                wk0()

                            if not operator_3.is_end_of_ternary_expression:
                                middle_2 = parse_PYTHON__ternary_expression__X__any_expression(middle_2, operator_3)

                                operator_3 = qk()

                                if operator_3 is 0:
                                    raise_unknown_line()

                                wk0()

                            if not operator_3.is_right_square_bracket:
                                raise_unknown_line()

                            left = conjure_index_expression(
                                       left,
                                       conjure_range_index(operator, middle, operator_2, middle_2, operator_3),
                                   )
                    elif operator_2.is_colon__right_square_bracket:
                        left = conjure_index_expression(left, conjure_head_index(operator, middle, operator_2))
                    else:
                        my_line('operator_2: %r', operator_2)
                        raise_unknown_line()

                    if qn() is not 0:
                        return left

                    operator = qk()

                    if operator is not 0:
                        if not operator.is_postfix_operator:
                            return left

                        wk0()
                    else:
                        if qn() is not 0:
                            return left

                        operator = tokenize_PYTHON_operator()

                        if not operator.is_postfix_operator:
                            wk(operator)

                            return left

            if operator.is_tail_index:
                middle_2 = parse_PYTHON__atom__or__right_square_bracket()

                if middle_2.is_right_square_bracket:
                    operator = conjure_all_index__with_newlines(operator.a, operator.b, middle_2)
                else:
                    operator_2 = qk()

                    if operator_2 is 0:
                        if qn() is not 0:
                            raise_unknown_line()

                        operator_2 = tokenize_PYTHON_operator()
                    else:
                        wk0()

                    if not operator_2.is_right_square_bracket:
                        middle_2 = parse_PYTHON__ternary_expression__X__any_expression(middle_2, operator_2)

                        operator_2 = qk()

                        if not operator_2.is_right_square_bracket:
                            raise_unknown_line()

                        wk0()

                    left = conjure_index_expression(left, conjure_tail_index(operator, middle_2, operator_2))

                    if qn() is not 0:
                        return left

                    operator = qk()

                    if operator is not 0:
                        if not operator.is_postfix_operator:
                            return left

                        wk0()
                    else:
                        if qn() is not 0:
                            return left

                        operator = tokenize_PYTHON_operator()

                        if not operator.is_postfix_operator:
                            wk(operator)

                            return left

            if operator.is_all_index:
                left = conjure_index_expression(left, operator)

                if qn() is not 0:
                    return left

                operator = qk()

                if operator is not 0:
                    if not operator.is_postfix_operator:
                        return left

                    wk0()
                else:
                    if qn() is not 0:
                        return left

                    operator = tokenize_PYTHON_operator()

                    if not operator.is_postfix_operator:
                        wk(operator)

                        return left

            assert operator.is_postfix_operator

        raise_unknown_line()



    #
    #   4.  Power-Expression (Python 2.7.14rc1 grammer calls this 'power')
    #
    #       power-expression
    #           :   postfix-expression
    #           |   postfix-expression '**' unary-expression
    #
    def parse_PYTHON__power_expression__left_operator(left, power_operator):
        return conjure_power_expression(left, power_operator, parse_PYTHON__unary_expression())


    #
    #   5.  Unary-Expression (Python 2.7.14rc1 grammer calls this 'factor')
    #
    @share
    def parse_PYTHON__twos_complement_expression__operator(operator):
        return conjure_twos_complement(operator, parse_PYTHON__unary_expression())


    @share
    def parse_PYTHON__negative_expression__operator(operator):
        return conjure_negative_expression(operator, parse_PYTHON__unary_expression())


    def parse_PYTHON__unary_expression():
        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is 0:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if qk() is not 0:
                raise_unknown_line()

            if operator.is_end_of_unary_expression:
                wk(operator)
                return left
        else:
            if operator.is_end_of_unary_expression:
                return left

            wk0()

        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_unary_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_unary_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_unary_expression:
                return left

            wk0()

        raise_unknown_line()


    #
    #   6.  Multiply-Expression (Python 2.7.14rc1 grammer calls this 'term')
    #
    #       multiply-expression
    #           : unary-expression
    #           | multiply-expression mutiply-operator unary-expression
    #
    #       multiply-operator
    #           : '*'
    #           | '/'
    #           | '%'
    #           | '//'
    #
    def parse_PYTHON__multiply_expression__left_operator(left, multiply_operator):
        right = parse_PYTHON__unary_expression()

        operator = qk()

        if operator is 0:
            if qn() is not 0:
                return multiply_operator.expression_meta(left, multiply_operator, right)

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_multiply_expression:
                wk(operator)

                return multiply_operator.expression_meta(left, multiply_operator, right)
        else:
            if operator.is_end_of_multiply_expression:
                return multiply_operator.expression_meta(left, multiply_operator, right)

            wk0()

        if not operator.is_multiply_operator:
            raise_unknown_line()

        many       = [left, right]
        many_frill = [multiply_operator, operator]

        while 7 is 7:
            many.append(parse_PYTHON__unary_expression())

            operator = qk()

            if operator is 0:
                if qn() is not 0:
                    break

                operator = tokenize_PYTHON_operator()

                if operator.is_end_of_multiply_expression:
                    wk(operator)
                    break
            else:
                if operator.is_end_of_multiply_expression:
                    break

                wk0()

            if not operator.is_multiply_operator:
                raise_unknown_line()

            many.append(operator)

        return conjure_multiply_expression_many(many, many_frill)


    def parse_PYTHON__multiply_expression():
        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is not 0:
            if operator.is_end_of_multiply_expression:
                return left

            wk0()
        else:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_multiply_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_multiply_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_multiply_expression:
                return left

            wk0()

        if operator.is_multiply_operator:
            return parse_PYTHON__multiply_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()


    #
    #   7.  Arithmetic-Expression (Python 2.7.14rc1 grammer calls this 'arith_expr')
    #
    def parse_PYTHON__arithmetic_expression__left_operator(left, add_operator):
        assert add_operator.is_PYTHON_arithmetic_operator

        right = parse_PYTHON__multiply_expression()

        operator = qk()

        if operator is 0:
            if qn() is not 0:
                return add_operator.expression_meta(left, add_operator, right)

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_PYTHON_arithmetic_expression:
                wk(operator)

                return add_operator.expression_meta(left, add_operator, right)
        else:
            if operator.is_end_of_PYTHON_arithmetic_expression:
                return add_operator.expression_meta(left, add_operator, right)

            wk0()

        if not operator.is_PYTHON_arithmetic_operator:
            raise_unknown_line()

        many       = [left, right]
        many_frill = [add_operator, operator]

        while 7 is 7:
            many.append(parse_PYTHON__multiply_expression())

            operator = qk()

            if operator is 0:
                if qn() is not 0:
                    break

                operator = tokenize_PYTHON_operator()

                if operator.is_end_of_PYTHON_arithmetic_expression:
                    wk(operator)
                    break
            else:
                if operator.is_end_of_PYTHON_arithmetic_expression:
                    break

                wk0()

            if not operator.is_PYTHON_arithmetic_operator:
                raise_unknown_line()

            many_frill.append(operator)

        return conjure_arithmetic_expression_many(many, many_frill)


    def parse_PYTHON__arithmetic_expression():
        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is not 0:
            if operator.is_end_of_PYTHON_arithmetic_expression:
                return left

            wk0()
        else:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_PYTHON_arithmetic_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_PYTHON_arithmetic_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_PYTHON_arithmetic_expression:
                return left

            wk0()

        if operator.is_multiply_operator:
            left = parse_PYTHON__multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_PYTHON_arithmetic_expression:
                return left

            wk0()

        if operator.is_PYTHON_arithmetic_operator:
            return parse_PYTHON__arithmetic_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()


    #
    #   j.  Shift-Expression (Python 2.7.14rc1 grammer calls this 'shift_expr')
    #

    #
    #   9.  Logical-And-Expression (Python 2.7.14rc1 grammer calls this 'and_expr')
    #
    def parse_PYTHON__logical_and_expression__left_operator(left, logical_and_operator):
        assert logical_and_operator.is_logical_and_operator

        right = parse_PYTHON__arithmetic_expression()

        operator = qk()

        if operator is 0:
            if qn() is not 0:
                return conjure_logical_and_expression(left, logical_and_operator, right)

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_logical_and_expression:
                wk(operator)

                return conjure_logical_and_expression(left, logical_and_operator, right)
        else:
            if operator.is_end_of_logical_and_expression:
                return conjure_logical_and_expression(left, logical_and_operator, right)

            wk0()

        if not operator.is_logical_and_operator:
            raise_unknown_line()

        many = [left, logical_and_operator, right, operator]

        while 7 is 7:
            many.append(parse_PYTHON__arithmetic_expression())

            operator = qk()

            if operator is 0:
                if qn() is not 0:
                    return LogicalAndExpression_Many(Tuple(many))

                operator = tokenize_PYTHON_operator()

                if operator.is_end_of_logical_and_expression:
                    wk(operator)

                    return LogicalAndExpression_Many(Tuple(many))
            else:
                if operator.is_end_of_logical_and_expression:
                    return LogicalAndExpression_Many(Tuple(many))

                wk0()

            if not operator.is_logical_and_operator:
                raise_unknown_line()

            many.append(operator)


    @share
    def parse_PYTHON__logical_and_expression():
        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is not 0:
            if operator.is_end_of_logical_and_expression:
                return left

            wk0()
        else:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_logical_and_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_and_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_and_expression:
                return left

            wk0()

        if operator.is_multiply_operator:
            left = parse_PYTHON__multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_and_expression:
                return left

            wk0()

        if operator.is_PYTHON_arithmetic_operator:
            left = parse_PYTHON__arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_and_expression:
                return left

            wk0()

        if operator.is_logical_and_operator:
            return parse_PYTHON__logical_and_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()


    #
    #   10. Logical-Exclusive-Or-Expression (Python 2.7.14rc1 grammer calls this 'xor_expr')
    #

    #
    #   11. Normal-Expression (Logical-Or) (Python 2.7.14rc1 grammer calls this 'expr')
    #
    def parse_PYTHON__normal_expression__left_operator(left, logical_or_operator):
        assert logical_or_operator.is_logical_or_operator

        right = parse_PYTHON__logical_and_expression()

        operator = qk()

        if operator is 0:
            if qn() is not 0:
                return conjure_logical_or_expression(left, logical_or_operator, right)

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_logical_or_expression:
                wk(operator)

                return conjure_logical_or_expression(left, logical_or_operator, right)
        else:
            if operator.is_end_of_logical_or_expression:
                return conjure_logical_or_expression(left, logical_or_operator, right)

            wk0()

        if not operator.is_logical_or_operator:
            raise_unknown_line()

        many       = [left, right]
        many_frill = [logical_or_operator, operator]

        while 7 is 7:
            many.append(parse_PYTHON__logical_and_expression())

            operator = qk()

            if operator is 0:
                if qn() is not 0:
                    break

                operator = tokenize_PYTHON_operator()

                if operator.is_end_of_logical_or_expression:
                    wk(operator)
                    break
            else:
                if operator.is_end_of_logical_or_expression:
                    break

                wk0()

            if not operator.is_logical_or_operator:
                raise_unknown_line()

            many_frill.append(operator)

        return conjure_logical_or_expression_many(many, many_frill)


    @share
    def parse_PYTHON__normal_expression():
        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is not 0:
            if operator.is_end_of_logical_or_expression:
                return left

            wk0()
        else:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_logical_or_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk0()

        if operator.is_multiply_operator:
            left = parse_PYTHON__multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk0()

        if operator.is_PYTHON_arithmetic_operator:
            left = parse_PYTHON__arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk0()

        if operator.is_logical_and_operator:
            left = parse_PYTHON__logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_logical_or_expression:
                return left

            wk0()

        if operator.is_logical_or_operator:
            return parse_PYTHON__normal_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()

    #
    #   12. Normal-Expression-List (Python 2.7.14rc1 grammer calls this 'exprlist')
    #
    @share
    def parse_PYTHON__normal_expression_list():
        return parse_PYTHON__arithmetic_expression()       #   Temporary until , is implemented


    #
    #   13. Compare-Expression (Python 2.7.14rc1 grammer calls this 'comparasion')
    #
    @share
    def parse_PYTHON__compare_expression__left_operator(left, compare_operator):
        assert compare_operator.is_compare_operator

        if compare_operator.is_keyword_not:
            #my_line('full: %s', portray_string(qs()))
            raise_unknown_line()

        right = parse_PYTHON__normal_expression()

        operator = qk()

        if operator is 0:
            if qn() is not 0:
                return compare_operator.expression_meta(left, compare_operator, right)

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_compare_expression:
                wk(operator)

                return compare_operator.expression_meta(left, compare_operator, right)
        else:
            if operator.is_end_of_compare_expression:
                return compare_operator.expression_meta(left, compare_operator, right)

            wk0()

        many       = [left, right]
        many_frill = [compare_operator, operator]

        while 7 is 7:
            many.append(parse_PYTHON__normal_expression())

            operator = qk()

            if operator is 0:
                if qn() is not 0:
                    break

                operator = tokenize_PYTHON_operator()

                if operator.is_end_of_compare_expression:
                    wk(operator)
                    break
            else:
                if operator.is_end_of_compare_expression:
                    break

                wk0()

            many_frill.append(operator)

        return conjure_compare_expression_many(many, many_frill)


    def parse_PYTHON__compare_expression():
        assert qk() is 0

        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is not 0:
            if operator.is_end_of_compare_expression:
                return left

            wk0()
        else:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_compare_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk0()

        if operator.is_multiply_operator:
            left = parse_PYTHON__multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk0()

        if operator.is_PYTHON_arithmetic_operator:
            left = parse_PYTHON__arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk0()

        if operator.is_logical_and_operator:
            left = parse_PYTHON__logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk0()

        if operator.is_logical_or_operator:
            left = parse_PYTHON__normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_compare_expression:
                return left

            wk0()

        if operator.is_compare_operator:
            return parse_PYTHON__compare_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()


    #
    #   14. Not-Expression (Python 2.7.14rc1 grammer calls this 'not_test')
    #
    #       not-expression
    #           : compare-expression
    #           | 'not' not-test
    #
    #   NOTE [FIX IN FUTURE -- When really parsing not expressions properly]:
    #       Uses .is_end_of_compare_expression on purpose (there is no .is_end_of_not_expression, as it would be
    #       identicial to .is_end_of_compare_expression)
    #
    @share
    def parse_PYTHON__not_expression__operator(not_operator):
        assert not_operator.is_keyword_not

        return conjure_not_expression(not_operator, parse_PYTHON__compare_expression()) #   Temporary until handle 'not' atom itself


    #
    #   15. Boolean-And-Expression (Python 2.7.14rc1 grammer calls this 'and_test')
    #
    def parse_PYTHON__boolean_and_expression__left_operator(left, operator):
        assert operator.is_keyword_and

        right = parse_PYTHON__compare_expression()

        operator_2 = qk()

        if operator_2 is 0:
            if qn() is not 0:
                return conjure_and_expression_1(left, operator, right)

            operator_2 = tokenize_PYTHON_operator()

            if operator_2.is_end_of_boolean_and_expression:
                wk(operator_2)

                return conjure_and_expression_1(left, operator, right)
        else:
            if operator_2.is_end_of_boolean_and_expression:
                return conjure_and_expression_1(left, operator, right)

            wk0()

        many       = [left, right]
        many_frill = [operator, operator_2]

        while 7 is 7:
            many.append(parse_PYTHON__compare_expression())

            operator_7 = qk()

            if operator_7 is 0:
                if qn() is not 0:
                    return conjure_and_expression_many(many, many_frill)

                operator_7 = tokenize_PYTHON_operator()

                if operator_7.is_end_of_boolean_and_expression:
                    wk(operator_7)

                    return conjure_and_expression_many(many, many_frill)
            else:
                if operator_7.is_end_of_boolean_and_expression:
                    return conjure_and_expression_many(many, many_frill)

                wk0()

            if not operator_7.is_keyword_and:
                raise_unknown_line()

            many_frill.append(operator_7)


    def parse_PYTHON__boolean_and_expression():
        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is not 0:
            if operator.is_end_of_boolean_and_expression:
                return left

            wk0()
        else:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_boolean_and_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk0()

        if operator.is_multiply_operator:
            left = parse_PYTHON__multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk0()

        if operator.is_PYTHON_arithmetic_operator:
            left = parse_PYTHON__arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk0()

        if operator.is_logical_and_operator:
            left = parse_PYTHON__logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk0()

        if operator.is_logical_or_operator:
            left = parse_PYTHON__normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk0()

        if operator.is_compare_operator:
            left = parse_PYTHON__compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk0()

        if operator.is_keyword_and:
            return parse_PYTHON__boolean_and_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()



    #
    #   16. Boolean-Or-Expression (Python 2.7.14rc1 grammer calls this 'or_test')
    #
    def parse_PYTHON__boolean_or_expression__left_operator(left, operator):
        assert operator.is_keyword_or

        right = parse_PYTHON__boolean_and_expression()

        operator_2 = qk()

        if operator_2 is 0:
            if qn() is not 0:
                return conjure_or_expression_1(left, operator, right)

            operator_2 = tokenize_PYTHON_operator()

            if operator_2.is_end_of_boolean_or_expression:
                wk(operator_2)

                return conjure_or_expression_1(left, operator, right)
        else:
            if operator_2.is_end_of_boolean_or_expression:
                return conjure_or_expression_1(left, operator, right)

            wk0()

        many       = [left, right]
        many_frill = [operator, operator_2]

        while 7 is 7:
            many.append(parse_PYTHON__boolean_and_expression())

            operator_7 = qk()

            if operator_7 is 0:
                if qn() is not 0:
                    break

                operator_7 = tokenize_PYTHON_operator()

                if operator_7.is_end_of_boolean_or_expression:
                    wk(operator_7)
                    break
            else:
                if operator_7.is_end_of_boolean_or_expression:
                    break

                wk0()

            if not operator_7.is_keyword_or:
                raise_unknown_line()

            many_frill.append(operator_7)

        return conjure_or_expression_many(many, many_frill)


    def parse_PYTHON__boolean_or_expression():
        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is not 0:
            if operator.is_end_of_boolean_or_expression:
                return left

            wk0()
        else:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_boolean_or_expression:
                wk(operator)

                return left

        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk0()

        if operator.is_multiply_operator:
            left = parse_PYTHON__multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk0()

        if operator.is_PYTHON_arithmetic_operator:
            left = parse_PYTHON__arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk0()

        if operator.is_compare_operator:
            left = parse_PYTHON__compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk0()

        if operator.is_logical_and_operator:
            left = parse_PYTHON__logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_and_expression:
                return left

            wk0()

        if operator.is_logical_or_operator:
            left = parse_PYTHON__normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk0()

        if operator.is_keyword_and:
            left = parse_PYTHON__boolean_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_boolean_or_expression:
                return left

            wk0()

        if operator.is_keyword_or:
            return parse_PYTHON__boolean_or_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()


    #
    #   17. Lambda-Expression (Python 2.7.14rc1 grammer calls this 'lambdef')
    #


    #
    #   18. Ternary-Expression (Python 2.7.14rc1 grammer calls this 'test')
    #
    #           ternary-expression
    #               : boolean-or-expression
    #               | boolean-or-expression 'if' boolean-or-expression 'else' ternary-expression
    #               | lambda-expression
    #
    #           lambda-Expression
    #               : 'lambda' [variable-argument-list] ':' ternary-expression
    #
    def parse_PYTHON__ternary_expression__left_operator(left, operator):
        assert operator.is_keyword_if

        middle = parse_PYTHON__boolean_or_expression()

        operator_2 = qk()

        wk0()

        if not operator_2.is_keyword_else:
            #my_line('left: %r; operator: %r; middle: %r; operator_2: %r; s: %s',
            #        left, operator, middle, operator_2, portray_string(qs()[qj():]))

            raise_unknown_line()

        return conjure_ternary_expression(left, operator, middle, operator_2, parse_PYTHON__ternary_expression())


    @share
    def parse_PYTHON__ternary_expression__X__any_expression(left, operator):
        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk0()

        if operator.is_multiply_operator:
            left = parse_PYTHON__multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk0()

        if operator.is_PYTHON_arithmetic_operator:
            left = parse_PYTHON__arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk0()

        if operator.is_compare_operator:
            left = parse_PYTHON__compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk0()

        if operator.is_logical_and_operator:
            left = parse_PYTHON__logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk0()

        if operator.is_logical_or_operator:
            left = parse_PYTHON__normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk0()

        if operator.is_keyword_and:
            left = parse_PYTHON__boolean_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk0()


        if operator.is_keyword_or:
            left = parse_PYTHON__boolean_or_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression:
                return left

            wk0()

        if operator.is_keyword_if:
            return parse_PYTHON__ternary_expression__left_operator(left, operator)

        #my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()


    @share
    def parse_PYTHON__ternary_expression():
        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is not 0:
            if operator.is_end_of_ternary_expression:
                return left

            wk0()
        else:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_ternary_expression:
                wk(operator)

                return left

        return parse_PYTHON__ternary_expression__X__any_expression(left, operator)


    #
    #   19. Ternary-Expression-List (Python 2.7.14rc1 grammer calls this 'testlist')
    #
    @share
    def parse_PYTHON__ternary_expression_list__X_any_expression(left, operator):
        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        if operator.is_multiply_operator:
            left = parse_PYTHON__multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        if operator.is_PYTHON_arithmetic_operator:
            left = parse_PYTHON__arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        if operator.is_logical_and_operator:
            left = parse_PYTHON__logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        if operator.is_logical_or_operator:
            left = parse_PYTHON__normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        if operator.is_compare_operator:
            left = parse_PYTHON__compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        if operator.is_keyword_and:
            left = parse_PYTHON__boolean_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        if operator.is_keyword_or:
            left = parse_PYTHON__boolean_or_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        if operator.is_keyword_if:
            left = parse_PYTHON__ternary_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()

        #my_line('line: %d; left: %r; operator: %r', ql(), left, operator)
        raise_unknown_line()


    @share
    def parse_PYTHON__ternary_expression_list():
        left = parse_PYTHON_atom__normal()

        operator = qk()

        if operator is not 0:
            if operator.is_end_of_ternary_expression_list:
                return left

            wk0()
        else:
            if qn() is not 0:
                return left

            operator = tokenize_PYTHON_operator()

            if operator.is_end_of_ternary_expression_list:
                wk(operator)

                return left

        return parse_PYTHON__ternary_expression_list__X_any_expression(left, operator)


    #
    #   20. Subscript-Expression
    #

    #
    #   21. Subscript-Expression-List
    #

    #
    #   22. Map-Element
    #   23. Map-Element
    #

    #
    #   24. Yield-Expression
    #

    #
    #   25. Comprehension-Expression-List (Python 2.7.14rc1 grammer calls this 'testlist_comp')
    #
    @export
    def parse_PYTHON__comprehension_expression__left_operator(left, operator):
        assert operator.is_keyword_for

        while 7 is 7:
            if operator.is_keyword_for:
                middle = parse_PYTHON__normal_expression_list()

                in_operator = qk()

                wk0()

                if not in_operator.is_keyword_in:
                    #my_line('left: %r; operator: %r; middle: %r; in_operator: %r; s: %s',
                    #        left, operator, middle, in_operator, portray_string(qs()[qj():]))

                    raise_unknown_line()

                left = conjure_comprehension_for(left, operator, middle, in_operator, parse_PYTHON__boolean_or_expression())

                operator = qk()

                #
                #   TODO: Operator is 0 seems to be a mistake!
                #
                if (operator is 0) or (operator.is_end_of_comprehension_expression_list):
                    return left

                wk0()

            if operator.is_keyword_if:
                left = conjure_comprehension_if(left, operator, parse_PYTHON__boolean_or_expression())

                operator = qk()

                #
                #   TODO: Operator is 0 seems to be a mistake!
                #
                if (operator is 0) or (operator.is_end_of_comprehension_expression_list):
                    return left

                wk0()

            assert (operator.is_keyword_for) or (operator.is_keyword_if)


    @share
    def parse_PYTHON__comprehension_expression__X__any_expression(left, operator):
        if operator.is_postfix_operator:
            left = parse_PYTHON__postfix_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()

        if operator.is_power_operator:
            left = parse_PYTHON__power_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()

        if operator.is_multiply_operator:
            left = parse_PYTHON__multiply_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()

        if operator.is_PYTHON_arithmetic_operator:
            left = parse_PYTHON__arithmetic_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()

        if operator.is_compare_operator:
            left = parse_PYTHON__compare_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()

        if operator.is_logical_and_operator:
            left = parse_PYTHON__logical_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()

        if operator.is_logical_or_operator:
            left = parse_PYTHON__normal_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()

        if operator.is_keyword_and:
            left = parse_PYTHON__boolean_and_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()


        if operator.is_keyword_or:
            left = parse_PYTHON__boolean_or_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()

        if operator.is_keyword_if:
            left = parse_PYTHON__ternary_expression__left_operator(left, operator)

            operator = qk()

            if operator is 0:
                if qn() is 0:
                    raise_unknown_line()

                return left

            if operator.is_end_of_comprehension_expression:
                return left

            wk0()

        if operator.is_keyword_for:
            return parse_PYTHON__comprehension_expression__left_operator(left, operator)

        my_line('left: %r; operator: %r; s: %s', left, operator, portray_string(qs()[qj():]))
        raise_unknown_line()
