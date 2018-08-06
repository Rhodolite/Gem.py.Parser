#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.ParseAtom')
def module():
    #
    #   conjure_LANGUAGE_EMPTY_PAIR                 #   0 = NOT done
    #   parse_LANGUAGE__atom__normal                #   0 = NOT done; must have conjure_LANGUAGE_EMPTY_PAIR instead
    #   conjure_LANGUAGE_bookcase_expression_comma_1#   0 = same as conjure_LANGUAGE_bookcase_expression_1
    #   name__is_LANGUAGE__comma__RIGHT_OPERATOR    #   0 = not used; conjure_LANGUAGE_bookcase_expression_comma_1 is 0
    #
    @export
    def produce_parse_LANGUAGE__bookcase_expression__LEFT_OPERATOR(
            name,
            conjure_LANGUAGE_bookcase_expression_1,
            conjure_LANGUAGE_bookcase_expression_2,
            conjure_LANGUAGE_bookcase_expression_comma_1,
            conjure_LANGUAGE_bookcase_expression_many,
            conjure_LANGUAGE_dual_token,
            conjure_LANGUAGE_EMPTY_PAIR,
            name__is_end_of_LANGUAGE_MIDDLE_expression,
            name__is_LANGUAGE__comma__RIGHT_OPERATOR,
            name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR,
            name__is_LANGUAGE_RIGHT_OPERATOR,
            parse_LANGUAGE__atom__normal,
            parse_LANGUAGE__atom__or__RIGHT_OPERATOR,
            parse_LANGUAGE__FIRST_expression__X__any_expression,
            parse_LANGUAGE__MIDDLE_expression__X__any_expression,
            tokenize_LANGUAGE_operator,
    ):
        assert type(name)                                         is String
        assert type(conjure_LANGUAGE_bookcase_expression_1)       is Function
        assert type(conjure_LANGUAGE_bookcase_expression_2)       is Function
        assert type(conjure_LANGUAGE_bookcase_expression_comma_1) is Function

        if conjure_LANGUAGE_bookcase_expression_1 is conjure_LANGUAGE_bookcase_expression_comma_1:
            assert name__is_LANGUAGE__comma__RIGHT_OPERATOR is 0
        else:
            assert name__is_LANGUAGE__comma__RIGHT_OPERATOR is not 0

        assert type(conjure_LANGUAGE_bookcase_expression_many) is Function
        assert type(conjure_LANGUAGE_dual_token)               is Function

        if conjure_LANGUAGE_EMPTY_PAIR is 0:
            assert parse_LANGUAGE__atom__normal is not 0
        else:
            assert type(conjure_LANGUAGE_EMPTY_PAIR) is Function
            assert parse_LANGUAGE__atom__normal is 0

        assert type(name__is_end_of_LANGUAGE_MIDDLE_expression) is String

        if name__is_LANGUAGE__comma__RIGHT_OPERATOR is 0:
            assert conjure_LANGUAGE_bookcase_expression_1 is conjure_LANGUAGE_bookcase_expression_comma_1
        else:
            assert type(name__is_LANGUAGE__comma__RIGHT_OPERATOR)   is String
            assert conjure_LANGUAGE_bookcase_expression_1 is not conjure_LANGUAGE_bookcase_expression_comma_1

        assert type(name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR) is String
        assert type(name__is_LANGUAGE_RIGHT_OPERATOR)                  is String

        if parse_LANGUAGE__atom__normal is 0:
            assert conjure_LANGUAGE_EMPTY_PAIR is not 0
        else:
            assert type(parse_LANGUAGE__atom__normal) is Function
            assert conjure_LANGUAGE_EMPTY_PAIR is 0

        assert type(parse_LANGUAGE__atom__or__RIGHT_OPERATOR)             is Function
        assert type(parse_LANGUAGE__FIRST_expression__X__any_expression)  is Function
        assert type(parse_LANGUAGE__MIDDLE_expression__X__any_expression) is Function
        assert type(tokenize_LANGUAGE_operator)                           is Function


        @rename(name)
        def parse_LANGUAGE__bookcase_expression__LEFT_OPERATOR(left_operator):
            #my_line('left_operator: %r', left_operator)

            #
            #   1
            #
            if conjure_LANGUAGE_EMPTY_PAIR is 0:
                middle_1 = parse_LANGUAGE__atom__normal()
            else:
                assert parse_LANGUAGE__atom__normal is 0

                middle_1 = parse_LANGUAGE__atom__or__RIGHT_OPERATOR()

                if attribute(middle_1, name__is_LANGUAGE_RIGHT_OPERATOR):
                    return conjure_LANGUAGE_EMPTY_PAIR(left_operator, middle_1)

            operator_1 = qk()

            if operator_1 is none:
                operator_1 = tokenize_LANGUAGE_operator()
            else:
                wk(none)

            if not attribute(operator_1, name__is_end_of_LANGUAGE_MIDDLE_expression):
                middle_1 = parse_LANGUAGE__FIRST_expression__X__any_expression(middle_1, operator_1)

                operator_1 = qk()
                wk(none)

            if conjure_LANGUAGE_bookcase_expression_1 is conjure_LANGUAGE_bookcase_expression_comma_1:
                if attribute(operator_1, name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_1(left_operator, middle_1, operator_1)
            else:
                if attribute(operator_1, name__is_LANGUAGE_RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_1(left_operator, middle_1, operator_1)

                if attribute(operator_1, name__is_LANGUAGE__comma__RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_comma_1(left_operator, middle_1, operator_1)

            if not operator_1.is_CRYSTAL_comma:
                raise_unknown_line()

            #
            #   2
            #
            middle_2 = parse_LANGUAGE__atom__or__RIGHT_OPERATOR()

            if attribute(middle_2, name__is_LANGUAGE_RIGHT_OPERATOR):
                return conjure_LANGUAGE_bookcase_expression_comma_1(
                           left_operator,
                           middle_1,
                           conjure_LANGUAGE_dual_token(operator_1, middle_2),
                       )

            operator_2 = tokenize_LANGUAGE_operator()

            if not attribute(operator_2, name__is_end_of_LANGUAGE_MIDDLE_expression):
                middle_2 = parse_LANGUAGE__MIDDLE_expression__X__any_expression(middle_2, operator_2)

                operator_2 = qk()
                wk(none)

            if attribute(operator_2, name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR):
                return conjure_LANGUAGE_bookcase_expression_2(left_operator, middle_1, operator_1, middle_2, operator_2)

            if not operator_2.is_CRYSTAL_comma:
                raise_unknown_line()

            #
            #   3
            #
            middle_3 = parse_LANGUAGE__atom__or__RIGHT_OPERATOR()

            if attribute(middle_3, name__is_LANGUAGE_RIGHT_OPERATOR):
                return conjure_LANGUAGE_bookcase_expression_2(
                           left_operator,
                           middle_1,
                           operator_1,
                           middle_2,
                           conjure_LANGUAGE_dual_token(operator_2, middle_3),
                       )

            many       = [middle_1, middle_2]
            many_frill = [operator_1, operator_2]

            while 7 is 7:
                operator_7 = tokenize_LANGUAGE_operator()

                if not attribute(operator_7, name__is_end_of_LANGUAGE_MIDDLE_expression):
                    middle_3 = parse_LANGUAGE__MIDDLE_expression__X__any_expression(middle_3, operator_7)

                    operator_7 = qk()
                    wk(none)

                many.append(middle_3)

                if attribute(operator_7, name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_many(left_operator, many, many_frill, operator_7)

                if not operator_7.is_CRYSTAL_comma:
                    raise_unknown_line()

                middle_3 = parse_LANGUAGE__atom__or__RIGHT_OPERATOR()

                if attribute(middle_3, name__is_LANGUAGE_RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_many(
                               left_operator,
                               many,
                               many_frill,
                               conjure_LANGUAGE_dual_token(operator_7, middle_3),
                           )

                many_frill.append(operator_7)


        return parse_LANGUAGE__bookcase_expression__LEFT_OPERATOR


    @export
    def produce_parse_LANGUAGE__bookcase_expression__LEFT_OPERATOR__2(
            name,
            conjure_LANGUAGE_bookcase_expression_1,
            conjure_LANGUAGE_bookcase_expression_2,                     #   May be 0
            conjure_LANGUAGE_bookcase_expression_comma_1,
            conjure_LANGUAGE_bookcase_expression_many,
            conjure_LANGUAGE_dual_token,
            conjure_LANGUAGE_EMPTY_PAIR,                                #   May be 0
            name__is_LANGUAGE__comma__RIGHT_OPERATOR,                   #   May be 0
            name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR,
            name__is_LANGUAGE_RIGHT_OPERATOR,
            parse_LANGUAGE__FIRST_expression,                           #   May be 0
            parse_LANGUAGE__FIRST_expression__or__RIGHT_OPERATOR,       #   May be 0
            parse_LANGUAGE__MIDDLE_expression__or__RIGHT_OPERATOR,
    ):
        assert type(name)                                         is String
        assert type(conjure_LANGUAGE_bookcase_expression_1)       is Function

        if conjure_LANGUAGE_bookcase_expression_2 is not 0:
            assert type(conjure_LANGUAGE_bookcase_expression_2)   is Function

        assert type(conjure_LANGUAGE_bookcase_expression_comma_1) is Function

        if conjure_LANGUAGE_bookcase_expression_1 is conjure_LANGUAGE_bookcase_expression_comma_1:
            assert name__is_LANGUAGE__comma__RIGHT_OPERATOR is 0
        else:
            assert name__is_LANGUAGE__comma__RIGHT_OPERATOR is not 0

        assert type(conjure_LANGUAGE_bookcase_expression_many) is Function
        assert type(conjure_LANGUAGE_dual_token)               is Function

        if conjure_LANGUAGE_EMPTY_PAIR is 0:
            assert parse_LANGUAGE__FIRST_expression                     is not 0
            assert parse_LANGUAGE__FIRST_expression__or__RIGHT_OPERATOR is 0
        else:
            assert type(conjure_LANGUAGE_EMPTY_PAIR)                    is Function
            assert parse_LANGUAGE__FIRST_expression                     is 0
            assert parse_LANGUAGE__FIRST_expression__or__RIGHT_OPERATOR is not 0

        if name__is_LANGUAGE__comma__RIGHT_OPERATOR is 0:
            assert conjure_LANGUAGE_bookcase_expression_1 is conjure_LANGUAGE_bookcase_expression_comma_1
        else:
            assert type(name__is_LANGUAGE__comma__RIGHT_OPERATOR)   is String
            assert conjure_LANGUAGE_bookcase_expression_1 is not conjure_LANGUAGE_bookcase_expression_comma_1

        assert type(name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR) is String
        assert type(name__is_LANGUAGE_RIGHT_OPERATOR)                  is String

        if parse_LANGUAGE__FIRST_expression is 0:
            assert conjure_LANGUAGE_EMPTY_PAIR is not 0
        else:
            assert type(parse_LANGUAGE__FIRST_expression) is Function
            assert conjure_LANGUAGE_EMPTY_PAIR is 0
        
        if parse_LANGUAGE__FIRST_expression__or__RIGHT_OPERATOR is 0:
            assert conjure_LANGUAGE_EMPTY_PAIR is 0
        else:
            assert type(parse_LANGUAGE__FIRST_expression__or__RIGHT_OPERATOR) is Function
            assert conjure_LANGUAGE_EMPTY_PAIR is not 0

        assert type(parse_LANGUAGE__MIDDLE_expression__or__RIGHT_OPERATOR) is Function


        @rename(name)
        def parse_LANGUAGE__bookcase_expression__LEFT_OPERATOR(left_operator):
            #my_line('left_operator: %r', left_operator)

            #
            #   1
            #
            if conjure_LANGUAGE_EMPTY_PAIR is 0:
                middle_1 = parse_LANGUAGE__FIRST_expression()
            else:
                middle_1 = parse_LANGUAGE__FIRST_expression__or__RIGHT_OPERATOR()

                if attribute(middle_1, name__is_LANGUAGE_RIGHT_OPERATOR):
                    return conjure_LANGUAGE_EMPTY_PAIR(left_operator, middle_1)

            operator_1 = qk()

            wk(none)

            #
            #   TODO:   If `middle_1` is a comprehension expression, THEN: it ust be followed by a RIGHT_OPERATOR
            #

            if conjure_LANGUAGE_bookcase_expression_1 is conjure_LANGUAGE_bookcase_expression_comma_1:
                if attribute(operator_1, name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_1(left_operator, middle_1, operator_1)
            else:
                if attribute(operator_1, name__is_LANGUAGE_RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_1(left_operator, middle_1, operator_1)

                if attribute(operator_1, name__is_LANGUAGE__comma__RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_comma_1(left_operator, middle_1, operator_1)

            if not operator_1.is_CRYSTAL_comma:
                #my_line('operator_1: %r', operator_1)
                raise_unknown_line()

            #
            #   2
            #
            middle_2 = parse_LANGUAGE__MIDDLE_expression__or__RIGHT_OPERATOR()

            if attribute(middle_2, name__is_LANGUAGE_RIGHT_OPERATOR):
                return conjure_LANGUAGE_bookcase_expression_comma_1(
                           left_operator,
                           middle_1,
                           conjure_LANGUAGE_dual_token(operator_1, middle_2),
                       )


            if conjure_LANGUAGE_bookcase_expression_2 is 0:
                many       = [middle_1, middle_2]
                many_frill = [operator_1]
            else:
                operator_2 = qk()

                assert operator_2 is not none

                if attribute(operator_2, name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_2(left_operator, middle_1, operator_1, middle_2, operator_2)

                if not operator_2.is_CRYSTAL_comma:
                    raise_unknown_line()

                #
                #   3
                #
                middle_3 = parse_LANGUAGE__MIDDLE_expression__or__RIGHT_OPERATOR()

                if attribute(middle_3, name__is_LANGUAGE_RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_2(
                               left_operator,
                               middle_1,
                               operator_1,
                               middle_2,
                               conjure_LANGUAGE_dual_token(operator_2, middle_3),
                           )

                many       = [middle_1, middle_2, middle_3]
                many_frill = [operator_1, operator_2]

            while 7 is 7:
                operator_7 = qk()

                wk(none)

                if attribute(operator_7, name__is_LANGUAGE__optional_comma__RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_many(left_operator, many, many_frill, operator_7)

                if not operator_7.is_CRYSTAL_comma:
                    raise_unknown_line()

                middle_7 = parse_LANGUAGE__MIDDLE_expression__or__RIGHT_OPERATOR()

                if attribute(middle_7, name__is_LANGUAGE_RIGHT_OPERATOR):
                    return conjure_LANGUAGE_bookcase_expression_many(
                               left_operator,
                               many,
                               many_frill,
                               conjure_LANGUAGE_dual_token(operator_7, middle_7),
                           )

                many_frill.append(operator_7)
                many.append      (middle_7)


        return parse_LANGUAGE__bookcase_expression__LEFT_OPERATOR
