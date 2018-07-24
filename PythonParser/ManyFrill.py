#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.ManyFrill')
def gem():
    require_gem('PythonParser.QuadrupleFrill')
    require_gem('PythonParser.TokenTuple')


    many_frill_cache   = {}
    provide_many_frill = many_frill_cache.setdefault


    class ManyFrill(TokenTuple):
        __slots__    = (())
        class_order  = CLASS_ORDER__FRILL_MANY
        display_name = 'frill-*'


        frill_estimate = 7


        def iterate_write(t, w):
            for v in t:
                w(v.s)
                yield


    @share
    def conjure_many_frill(many):
        if type(many) is not List:
            assert many.frill_estimate

            return many

        total = length(many)

        if total <= 4:
            if total is 1:
                assert many[0].frill_estimate is 1

                return many[0]

            if total is 2:
                return conjure_vw_frill(many[0], many[1])

            if total is 3:
                return conjure_vwx_frill(many[0], many[1], many[2])

            assert total is 4

            return conjure_vwxy_frill(many[0], many[1], many[2], many[3])

        r = ManyFrill(many)

        return provide_many_frill(r, r)


    #
    #   .transform
    #
    ManyFrill.transform = produce_transform_many('many-frill', conjure_many_frill)


    append_cache('many-frill', many_frill_cache)
