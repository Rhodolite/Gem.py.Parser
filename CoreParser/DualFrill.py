#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.DualFrill')
def module():
    require_module('CoreParser.DualTwig')


    dual_frill_cache  = {}
    lookup_dual_frill = dual_frill_cache.get
    store_dual_frill  = dual_frill_cache.__setitem__


    if PYTHON_parser:
        class Commented_V_Frill(DualTwig):
            __slots__ = (())
            comment   = DualTwig.a
            v         = DualTwig.b

            class_order  = CLASS_ORDER__FRILL_2
            display_name = '#v-frill'


            if PYTHON_parser:
                def transform(t, vary):
                    comment = t.comment
                    v       = t.v

                    comment__2 = comment.transform(vary)
                    v__2       = v      .transform(vary)

                    if (comment is comment__2) and (v is v__2):
                        return t

                    if comment__2 is 0:
                        return v__2

                    return conjure_commented_v_frill(comment__2, v__2)


    class VW_Frill(DualTwig):
        __slots__ = (())
        k1        = DualTwig.a
        k2        = DualTwig.b
        v         = DualTwig.a
        w         = DualTwig.b

        class_order    = CLASS_ORDER__FRILL_2
        comment        = 0
        display_name   = 'vw-frill'
        is_vw_frill    = true
        frill_estimate = 2

        __init__       = construct__ab
        __repr__       = portray__ab
        count_newlines = count_newlines__ab
        display_token  = display_token__ab
        dump_token     = dump_token__12


        if PYTHON_parser:
            #
            #   NOTE:
            #       This is deliberatly called .morph, as its not appropriate to do .mutate on a general
            #       wrapper like VW_frill -- even when it is called with 'a_priority' and 'b_priority'
            #       with the same value.
            #
            #       Thus the specific method .morph here is to indicate [for code clarity of the reader] that
            #       something special is going on -- even though [for the computer] it really looks like
            #       a .mutate method with redundant parameters.
            #
            def morph(t, vary, a_priority, b_priority):
                a = t.a
                b = t.b

                a__2 = (a.transform(vary)   if a_priority is 0 else   a.mutate(vary, a_priority))
                b__2 = (b.transform(vary)   if b_priority is 0 else   b.mutate(vary, b_priority))

                if (a is a__2) and (b is b__2):
                    return t

                return conjure_vw_frill(a__2, b__2)


        order = order__ab



    if PYTHON_parser:
        conjure_commented_v_frill = produce_conjure_dual(
                                        '#v-frill',
                                        Commented_V_Frill,
                                        dual_frill_cache,
                                        lookup_dual_frill,
                                        store_dual_frill
                                    )

    conjure_vw_frill = produce_conjure_dual(
                           'vw-frill',
                           VW_Frill,
                           dual_frill_cache,
                           lookup_dual_frill,
                           store_dual_frill
                       )


    #
    #   .transform
    #
    if PYTHON_parser:
        VW_Frill.transform = produce_transform__ab('vw_frill', conjure_vw_frill)


    append_cache('dual-frill', dual_frill_cache)


    if PYTHON_parser:
        export(
            'conjure_commented_v_frill',    conjure_commented_v_frill,
        )


    export(
        'conjure_vw_frill',             conjure_vw_frill,
    )
