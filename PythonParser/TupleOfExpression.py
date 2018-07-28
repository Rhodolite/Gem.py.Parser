#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.TupleOfExpression')
def module():
    require_module('PythonParser.Cache')
    require_module('PythonParser.TokenTuple')


    tuple_of_expression_cache = {}


    class TupleOfExpression(TokenTuple):
        __slots__    = (())
        display_name = 'expression-*'


        def morph(t, vary, first_priority, middle_priority, last_priority):
            iterator = iterate(t)

            element_priority = first_priority
            maximum_i_m1     = length(t) - 1

            v    = next_method(iterator)()
            v__2 = v.mutate(vary, first_priority)

            if v is not v__2:
                element_priority = middle_priority
                i                = 0
                many__2          = [v__2]

                append = many__2.append
            else:
                element_priority = middle_priority
                i                = 1

                for v in iterator:
                    v__2 = v.mutate(vary, (last_priority   if i is maximum_i_m1 else   middle_priority))

                    if v is not v__2:
                        break

                    i += 1
                else:
                     return t

                if i is 1:
                    many__2 = [t[0], v__2]
                    append  = many__2.append
                else:
                    many__2 = List(t[:i])
                    append  = many__2.append

                    append(v__2)

            for v in iterator:
                i += 1

                append(v.mutate(vary, (last_priority   if i is maximum_i_m1 else   middle_priority)))

            assert i == maximum_i_m1

            return conjure_tuple_of_many_expression(many__2)


    conjure_tuple_of_many_expression = produce_conjure_tuple(
                                           'many-expression',
                                           TupleOfExpression,
                                           tuple_of_expression_cache,
                                       )


    append_cache('tuple-of-expression', tuple_of_expression_cache)


    share(
        'conjure_tuple_of_many_expression',     conjure_tuple_of_many_expression,
    )
