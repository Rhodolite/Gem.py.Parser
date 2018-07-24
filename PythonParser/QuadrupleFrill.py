#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.QuadrupleFrill')
def gem():
    require_gem('PythonParser.QuadrupleTwig')


    quadruple_frill_cache  = create_cache('quadruple_frill')
    lookup_quadruple_frill = quadruple_frill_cache.get
    store_quadruple_frill  = quadruple_frill_cache.__setitem__


    class VWXY_Frill(QuadrupleTwig):
        __slots__      = (())
        v              = QuadrupleTwig.a
        w              = QuadrupleTwig.b
        x              = QuadrupleTwig.c
        y              = QuadrupleTwig.d

        class_order    = CLASS_ORDER__QUADRUPLE_TWIG
        display_name   = 'vwxy-frill'
        frill_estimate = 4


        order = order__abcd


    class Commented_VWX_Frill(QuadrupleTwig):
        __slots__    = (())
        comment      = QuadrupleTwig.a
        v            = QuadrupleTwig.b
        w            = QuadrupleTwig.c
        x            = QuadrupleTwig.d

        class_order  = CLASS_ORDER__QUADRUPLE_TWIG
        display_name = '#vwx-frill'


        order = order__abcd


        def transform(t, vary):
            comment = t.comment
            v       = t.v
            w       = t.w
            x       = t.x

            comment__2 = comment.transform(vary)
            v__2       = v      .transform(vary)
            w__2       = w      .transform(vary)
            x__2       = x      .transform(vary)

            if (comment is comment__2) and (v is v__2) and (w is w__2) and (x is x__2):
                return t

            if comment__2 is 0:
                return conjure_vwx_frill(v__2, w__2, x__2)

            return conjure_commented_vwx_frill(comment__2, v__2, w__2, x__2)


    conjure_vwxy_frill = produce_conjure_quadruple__4123(
                             'vwxy-frill',
                             VWXY_Frill,
                             quadruple_frill_cache,
                             lookup_quadruple_frill,
                             store_quadruple_frill,
                         )

    conjure_commented_vwx_frill = produce_conjure_quadruple__4123(
                                      '#vwx-frill',
                                      Commented_VWX_Frill,
                                      quadruple_frill_cache,
                                      lookup_quadruple_frill,
                                      store_quadruple_frill,
                                  )

    VWXY_Frill.transform = produce_transform__abcd('vwxy_frill', conjure_vwxy_frill)

    append_cache('quadruple-frill', quadruple_frill_cache)


    share(
        'conjure_vwxy_frill',           conjure_vwxy_frill,
        'conjure_commented_vwx_frill',  conjure_commented_vwx_frill,
    )
