#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.ManyExpression')
def module():
    require_module('CoreParser.ClassOrder')
    require_module('CoreParser.ManyFrill')
    require_module('CoreParser.Method')
    require_module('CoreParser.ParserTrunk')
    require_module('CoreParser.TupleOfExpression')


    @export
    class ManyExpression(ParserTrunk):
        __slots__ = ((
            'frill',                    #   BookcaseManyFrill
            'many',                     #   TupleOfExpression+
        ))


        class_order = CLASS_ORDER__MANY_EXPRESSION


        def __init__(t, frill, many):
            t.frill = frill
            t.many  = many


        def __repr__(t):
            return arrange('<%s %s %r>', t.__class__.__name__, t.frill, ' '.join(portray(v)   for v in t.many))


        def count_newlines(t):
            return t.many.count_newlines() + t.frill.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           t.frill.display_token(),
                           ' '.join(v.display_token()   for v in t.many))


        def dump_token(t, f, newline = true):
            frill = t.frill
            many  = t.many

            frill_estimate = frill.frill_estimate

            f.partial('<%s ', t.display_name)

            if frill_estimate is 1:
                assert length(many) is 2

                many    [0].dump_token(f)
                frill      .dump_token(f)
                r = many[1].dump_token(f, false)

            elif frill_estimate is 2:
                assert length(many) is 3

                many    [0].dump_token(f)
                frill   .v .dump_token(f)
                many    [1].dump_token(f)
                frill   .w .dump_token(f)
                r = many[2].dump_token(f, false)

            elif frill_estimate is 3:
                assert length(many) is 4

                many    [0].dump_token(f)
                frill   .v .dump_token(f)
                many    [1].dump_token(f)
                frill   .w .dump_token(f)
                many    [2].dump_token(f)
                frill   .x .dump_token(f)
                r = many[3].dump_token(f, false)

            elif frill_estimate is 4:
                assert length(many) is 5

                many    [0].dump_token(f)
                frill   .v .dump_token(f)
                many    [1].dump_token(f)
                frill   .w .dump_token(f)
                many    [2].dump_token(f)
                frill   .x .dump_token(f)
                many    [3].dump_token(f)
                frill   .y .dump_token(f)
                r = many[4].dump_token(f, false)

            else:
                iterator   = iterate(many)
                next_frill = next_method(iterate(frill))

                many[0].dump_token(f)

                for v in many[1:-1]:
                    next_frill().dump_token(f)
                    v           .dump_token(f)

                next_frill().dump_token(f)
                r = many[-1].dump_token(f, false)

            return f.token_result(r, newline)


        order = order__frill_many


        def write(t, w):
            many  = t.many
            frill = t.frill

            frill_estimate = frill.frill_estimate

            if frill_estimate is 1:
                assert length(many) is 2

                many[0].write(w)
                w(frill.s)
                many[1].write(w)
                return

            if frill_estimate is 2:
                assert length(many) is 3

                many[0].write(w)
                w(frill.v.s)
                many[1].write(w)
                w(frill.w.s)
                many[2].write(w)
                return

            if frill_estimate is 3:
                assert length(many) is 4

                many[0].write(w)
                w(frill.v.s)
                many[1].write(w)
                w(frill.w.s)
                many[2].write(w)
                w(frill.x.s)
                many[3].write(w)
                return

            if frill_estimate is 4:
                assert length(many) is 5

                many[0].write(w)
                w(frill.v.s)
                many[1].write(w)
                w(frill.w.s)
                many[2].write(w)
                w(frill.x.s)
                many[3].write(w)
                w(frill.y.s)
                many[4].write(w)
                return

            iterator    = iterate(many)
            write_frill = next_method(frill.iterate_write(w))

            next_method(iterator)().write(w)

            for v in iterator:
                write_frill()
                v.write(w)


   #ManyExpression.k1 = ManyExpression.frill
    ManyExpression.k2 = ManyExpression.many


    @export
    class ArithmeticExpression_Many(ManyExpression):
        __slots__    = (())
        display_name = 'arithmetic-many'

        if capital_global.python_parser:
            scout_variables = scout_variables__many


    @export
    def produce_conjure_many_expression(name, Meta):
        cache  = {}
        lookup = cache.get
        store  = cache.__setitem__

        conjure_dual = produce_conjure_dual(
                (arrange('conjure_%s__with_frill', name)   if python_debug_mode else   name),
                Meta,
                cache,
            )


        @rename('conjure_%s', name)
        def conjure_many_expression(list, frill_list):
            return conjure_dual(conjure_many_frill(frill_list), conjure_tuple_of_many_expression(list))


        if python_debug_mode:
            append_cache(name, cache)


        return ((
                   conjure_many_expression,
                   conjure_dual,
               ))


    [
        conjure_arithmetic_expression_many, conjure_arithmetic_expression_many__with_frill,
    ] = produce_conjure_many_expression('arithmetic-many', ArithmeticExpression_Many)


    export(
        'conjure_arithmetic_expression_many',               conjure_arithmetic_expression_many,
        'conjure_arithmetic_expression_many__with_frill',   conjure_arithmetic_expression_many__with_frill,
    )
