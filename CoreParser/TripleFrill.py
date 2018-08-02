#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.TripleFrill')
def module():
    require_module('CoreParser.TripleTwig')


    triple_frill_cache  = {}
    lookup_triple_frill = triple_frill_cache.get
    store_triple_frill  = triple_frill_cache.__setitem__


    if PYTHON_parser:
        class Commented_VW_Frill(TripleTwig):
            __slots__ = (())
            comment   = TripleTwig.a
            v         = TripleTwig.b
            w         = TripleTwig.c

            class_order  = CLASS_ORDER__FRILL_3
            display_name = '#vw-frill'


            order = order__abc


            if PYTHON_parser:
                def transform(t, vary):
                    comment = t.comment
                    v       = t.v
                    w       = t.w

                    comment__2 = comment.transform(vary)
                    v__2       = v.transform(vary)
                    w__2       = w.transform(vary)

                    if (comment is comment__2) and (v is v__2) and (w is w__2):
                        return t

                    if comment__2 is 0:
                        return conjure_vw_frill(v__2, w__2)

                    return conjure_commented_vw_frill(comment__2, v__2, w__2)


    class VWX_Frill(TripleTwig):
        __slots__ = (())
        comment   = 0
        v         = TripleTwig.a
        w         = TripleTwig.b
        x         = TripleTwig.c

        class_order    = CLASS_ORDER__FRILL_3
        display_name   = 'xyz-frill'
        frill_estimate = 3


        if PYTHON_parser:
            def morph(t, vary, v_priority, w_priority, x_priority):
                assert v_priority is x_priority is 0

                v = t.v
                w = t.w
                x = t.x

                v__2 = v.transform(vary)
                w__2 = w.mutate   (vary, w_priority)
                x__2 = x.transform(vary)

                if (v is v__2) and (w is w__2) and (x is x__2):
                    return t

                return conjure_vwx_frill(v__2, w__2, x__2)


        order = order__abc


    if PYTHON_parser:
        conjure_commented_vw_frill = produce_conjure_triple(
                                         '#vw-frill',
                                         Commented_VW_Frill,
                                         triple_frill_cache,
                                         lookup_triple_frill,
                                         store_triple_frill,
                                     )


    conjure_vwx_frill = produce_conjure_triple(
                            'vwx-frill',
                            VWX_Frill,
                            triple_frill_cache,
                            lookup_triple_frill,
                            store_triple_frill,
                        )


    if PYTHON_parser:
        VWX_Frill.transform = produce_transform__abc('vwx-frill', conjure_vwx_frill)


    append_cache('triple-frill', triple_frill_cache)


    if PYTHON_parser:
        export(
            'conjure_commented_vw_frill',   conjure_commented_vw_frill,
        )


    export(
        'conjure_vwx_frill',    conjure_vwx_frill,
    )
