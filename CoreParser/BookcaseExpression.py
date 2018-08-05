#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.BookcaseExpression')
def module():
    require_module('CoreParser.DualFrill')


    LEFT_PARENTHESIS__RIGHT_PARENTHESIS = conjure_vw_frill(LEFT_PARENTHESIS, RIGHT_PARENTHESIS)


    export(
        'LEFT_PARENTHESIS__RIGHT_PARENTHESIS',  LEFT_PARENTHESIS__RIGHT_PARENTHESIS,
    )


    @export
    class BookcaseExpression(ParserTrunk):
        __slots__ = ((
            'a',                        #   Expression+
        ))


        class_order = CLASS_ORDER__BOOKCASE_EXPRESSION


        def __init__(t, a):
            t.a = a


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.a)


        def count_newlines(t):
            return t.a.count_newlines() + t.frill.count_newlines()


        def display_token(t):
            return arrange('<%s %s>', t.display_name, t.a.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)

            frill    .v.dump_token(f)
            t        .a.dump_token(f)
            r = frill.w.dump_token(f, false)

            return f.token_result(r, newline)


        order = order__frill_a


        def write(t, w):
            frill = t.frill

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)


    BookcaseExpression.k1 = BookcaseExpression.a


    @export
    def produce_conjure_bookcase_expression(name, Meta):
        cache   = {}
        lookup  = cache.get
        provide = cache.setdefault
        store   = cache.__setitem__


        def conjure_BookcaseExpression_WithFrill(a, frill):
            BookcaseExpression_WithFrill = lookup_adjusted_meta(Meta)

            if BookcaseExpression_WithFrill is none:
                class BookcaseExpression_WithFrill(Meta):
                    __slots__ = ((
                        'frill',                #   DualFrill
                    ))


                    def __init__(t, a, frill):
                        t.a     = a
                        t.frill = frill


                    def __repr__(t):
                        return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.frill)


                    display_token = attribute(Meta, 'display_token__frill', none)

                    if display_token is none:
                        def display_token(t):
                            frill = t.frill

                            return arrange('<%s+frill %s %s %s>',
                                           t.display_name,
                                           frill.v.display_token(),
                                           t.a    .display_token(),
                                           frill.w.display_token())


                write = attribute(Meta, 'write__frill', none)

                if write is not none:
                    BookcaseExpression_WithFrill.write = write


                #BookcaseExpression_WithFrill.k2 = BookcaseExpression_WithFrill.frill


                if python_debug_mode:
                    BookcaseExpression_WithFrill.__name__ = intern_arrange('%s_WithFrill', Meta.__name__)

                store_adjusted_meta(Meta, BookcaseExpression_WithFrill)

            return BookcaseExpression_WithFrill(a, frill)


        conjure_dual__with_frill = produce_conjure_dual__21(
                                       name + '__X2',
                                       conjure_BookcaseExpression_WithFrill,
                                       cache,
                                       lookup,
                                       store,
                                   )

        meta_frill   = Meta.frill
        meta_frill_v = meta_frill.v
        meta_frill_w = meta_frill.w


        @rename('conjure_%s', name)
        def conjure_bookcase_expression(frill_v, a, frill_w):
            if (frill_v is meta_frill_v) and (frill_w is meta_frill_w):
                return (lookup(a)) or (provide(a, Meta(a)))

            return conjure_dual__with_frill(a, conjure_vw_frill(frill_v, frill_w))


        @rename('conjure_%s__with_frill', name)
        def conjure_with_frill(frill, a):
            if frill is meta_frill:
                return (lookup(a)) or (provide(a, Meta(a)))

            return conjure_dual__with_frill(a, frill)


        if python_debug_mode:
            append_cache(name, cache)


        return ((
                   conjure_bookcase_expression,
                   conjure_with_frill,
               ))


    if PYTHON_parser or TREMOLITE_parser:
        @export
        class ParenthesizedExpression(BookcaseExpression):
            __slots__    = (())
            display_name = '()'
            frill        = LEFT_PARENTHESIS__RIGHT_PARENTHESIS

            is_CRYSTAL_atom              = true
            is_CRYSTAL_left_parenthesis  = false
            is_CRYSTAL_right_parenthesis = false

            
            if PYTHON_parser:
                scout_variables = scout_variables__a


        [
            conjure_CRYSTAL_parenthesized_expression, conjure_CRYSTAL_parenthesized_expression__with_frill,
        ] = produce_conjure_bookcase_expression('parenthesized-expression', ParenthesizedExpression)


        export(
            'conjure_CRYSTAL_parenthesized_expression',     conjure_CRYSTAL_parenthesized_expression,

            'conjure_CRYSTAL_parenthesized_expression__with_frill',
                conjure_CRYSTAL_parenthesized_expression__with_frill,
        )
