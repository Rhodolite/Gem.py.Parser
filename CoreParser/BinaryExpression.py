#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.BinaryExpression')
def module():
    require_module('CoreParser.DualTwig')
    require_module('CoreParser.Elemental')


    binary_frill_cache  = create_cache('binary_frill_cache', conjure_nub)
    lookup_binary_frill = binary_frill_cache.get
    store_binary_frill  = binary_frill_cache.__setitem__


    def display_token__frill(t):
        return arrange('<%s+frill %s %s %s>',
                       t.display_name,
                       t.a    .display_token(),
                       t.frill.display_token(),
                       t.b    .display_token())


    def display_token__frill_with_braces(t):
        return arrange('{%s+frill %s %s %s}',
                       t.display_name,
                       t.a    .display_token(),
                       t.frill.display_token(),
                       t.b    .display_token())


    def portray_frill(t):
        return arrange('<%s %r %r %r>', t.__class__.__name__, t.a, t.frill, t.b)


    def portray_frill_with_braces(t):
        return arrange('{%s+frill %r %r %r}', t.__class__.__name__, t.a, t.frill, t.b)


    @export
    class BinaryExpression(DualTwig):
        __slots__ = (())


        class_order = CLASS_ORDER__BINARY_EXPRESSION


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            t    .a.dump_token(f)
            frill  .dump_token(f)
            r = t.b.dump_token(f)

            return f.token_result(r, newline)


        order = order__frill_ab


        if PYTHON_parser:
            scout_variables = scout_variables__ab


        def write(t, w):
            t.a.write(w)
            w(t.frill.s)
            t.b.write(w)


    @export
    class AddExpression(BinaryExpression):
        __slots__    = (())
        display_name = 'add'
        frill        = conjure_action_word('+', ' + ')


    @export
    def produce_conjure_binary_expression(name, Meta):
        cache  = create_cache(name, conjure_nub)
        lookup = cache.lookup
        store  = cache.store


        def conjure_BinaryExpression_WithFrill(a, b, frill):
            BinaryExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BinaryExpression_WithFrill is none:
                class BinaryExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   Operator*
                    ))


                    def __init__(t, a, frill, b):
                        t.a     = a
                        t.frill = frill
                        t.b     = b


                    __repr__ = (
                                   portray_frill_with_braces
                                       if method_is_function(Meta.__repr__, portray_with_braces) else
                                           portray_frill
                               )


                    def count_newlines(t):
                        return t.a.count_newlines() + t.frill.count_newlines() + t.b.count_newlines()


                    display_token = (
                            display_token__frill_with_braces
                                if method_is_function(Meta.display_token, display_token__ab__with_braces) else
                                    display_token__frill
                        )


                BinaryExpression_WithFrill.k3 = BinaryExpression_WithFrill.frill


                if python_debug_mode:
                    BinaryExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BinaryExpression_WithFrill)

            return BinaryExpression_WithFrill(a, frill, b)


        conjure_dual = produce_conjure_unique_dual(name, Meta, cache, lookup, store)

        conjure_triple = produce_conjure_unique_triple__312(
                             name,
                             conjure_BinaryExpression_WithFrill,
                             binary_frill_cache,
                             lookup_binary_frill,
                             store_binary_frill,
                         )

        meta_frill = Meta.frill


        @rename('conjure_%s', name)
        def conjure_binary_expression(a, frill, b):
            if frill is meta_frill:
                return conjure_dual(a, b)

            return conjure_triple(a, b, frill)


        return conjure_binary_expression


    conjure_add_expression = produce_conjure_binary_expression('add', AddExpression)


    #
    #   .expression_meta
    #
    OperatorPlusSign.expression_meta = static_method(conjure_add_expression)


    #
    #   export
    #
    export(
        'conjure_add_expression',   conjure_add_expression,
    )
