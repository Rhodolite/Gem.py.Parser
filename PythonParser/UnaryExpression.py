#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.UnaryExpression')
def module():
    @share
    class UnaryExpression(ParserTrunk):
        __slots__ = ((
            'a',                        #   Expression
        ))


        class_order = CLASS_ORDER__UNARY_EXPRESSION
        is_colon    = false


        def __init__(t, a):
            t.a = a


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.a)


        def count_newlines(t):
            return t.a.count_newlines()


        def display_token(t):
            return arrange('<%s %s>', t.display_name, t.a.display_token())


        def dump_token(t, f, newline = true):
            f.partial('<%s ', t.display_name)

            t    .frill.dump_token(f)
            r = t.a    .dump_token(f, false)

            return f.token_result(r, newline)


        order = order__frill_a


        def write(t, w):
            w(t.frill.s)
            t.a.write(w)


    UnaryExpression.k1 = UnaryExpression.a


    @share
    def produce_conjure_unary_expression(name, Meta):
        cache   = create_cache(name, conjure_nub)
        lookup  = cache.lookup
        provide = cache.provide
        store   = cache.store


        def conjure_UnaryExpression_WithFrill(a, frill):
            UnaryExpression_WithFrill = lookup_adjusted_meta(Meta)

            if UnaryExpression_WithFrill is none:
                class UnaryExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   Operator*
                    ))


                    def __init__(t, a, frill):
                        t.a     = a
                        t.frill = frill


                    def __repr__(t):
                        return arrange('<%s %r %r>', t.__class__.__name__, t.frill, t.a)


                    def count_newlines(t):
                        return t.a.count_newlines() + t.frill.count_newlines()


                    display_token = attribute(Meta, 'display_token__frill', none)

                    if display_token is none:
                        def display_token(t):
                            return arrange('<%s+frill %s %s>', t.display_name, t.frill.display_token(), t.a.display_token())


                UnaryExpression_WithFrill.k2 = UnaryExpression_WithFrill.frill


                if python_debug_mode:
                    UnaryExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, UnaryExpression_WithFrill)

            return UnaryExpression_WithFrill(a, frill)



        conjure_dual__21 = produce_conjure_unique_dual__21(
                               name,
                               conjure_UnaryExpression_WithFrill,
                               cache,
                               lookup,
                               store,
                           )

        meta_frill = Meta.frill


        @rename('conjure_%s', name)
        def conjure_unary_expression(frill, a):
            if frill is meta_frill:
                return (lookup(a)) or (provide(a, Meta(a)))

            return conjure_dual__21(a, frill)


        return conjure_unary_expression


    class NegativeExpression(UnaryExpression):
        __slots__    = (())
        display_name = '-'
        frill        = conjure_action_word('-', '-')


        scout_variables = scout_variables__a


    class NotExpression(UnaryExpression):
        __slots__    = (())
        display_name = 'not'
        frill        = NOT__W


        mutate          = produce_mutate__frill__a__priority('not-expression', PRIORITY_UNARY)
        scout_variables = scout_variables__a


    class StarArgument(UnaryExpression):
        __slots__    = (())
        display_name = '*-argument'
        frill        = conjure_star_sign('*')


        scout_variables = scout_variables__a



    class StarParameter(UnaryExpression):
        __slots__    = (())
        display_name = '*-parameter'
        frill        = conjure_star_sign('*')
        
        is_CRYSTAL_atom = true

        is_PYTHON__identifier__or__star_parameter = true


        add_parameters       = add_parameters__a
        scout_default_values = scout_default_values__a


    class TwosComplementExpression(UnaryExpression):
        __slots__    = (())
        display_name = '~'
        frill        = conjure_action_word('~', '~')


        scout_variables = scout_variables__a


    conjure_negative_expression = produce_conjure_unary_expression('negative',        NegativeExpression)
    conjure_not_expression      = produce_conjure_unary_expression('not',             NotExpression)
    conjure_star_argument       = produce_conjure_unary_expression('*-argument',      StarArgument)
    conjure_star_parameter      = produce_conjure_unary_expression('*-parameter',     StarParameter)
    conjure_twos_complement     = produce_conjure_unary_expression('twos-complement', TwosComplementExpression)


    NotExpression           .conjure_with_frill = static_method(conjure_not_expression)
    StarArgument            .conjure_with_frill = static_method(conjure_star_argument)
    StarParameter           .conjure_with_frill = static_method(conjure_star_parameter)
    TwosComplementExpression.conjure_with_frill = static_method(conjure_twos_complement)


    #
    #   .mutate
    #
    NegativeExpression.mutate = produce_mutate__frill__a_with_priority(
                                    'negative_expression',
                                    PRIORITY_UNARY,
                                    conjure_negative_expression,
                                )

    StarArgument.mutate = produce_mutate__frill__a_with_priority(
                              'star_argument',
                              PRIORITY_TERNARY,
                              conjure_star_argument,
                          )

    TwosComplementExpression.mutate = produce_mutate__frill__a_with_priority(
                                          'twos_complement_expression',
                                          PRIORITY_TERNARY,
                                          conjure_twos_complement,
                                      )


    #
    #   .transform
    #
    StarParameter.transform = produce_transform__frill_a('star_paramater', conjure_star_parameter)


    share(
        'conjure_negative_expression',  conjure_negative_expression,
        'conjure_not_expression',       conjure_not_expression,
        'conjure_star_argument',        conjure_star_argument,
        'conjure_star_parameter',       conjure_star_parameter,
        'conjure_twos_complement',      conjure_twos_complement,
    )
