#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.CreateMeta')
def module():
    require_module('PythonParser.Core')


    @share
    def conjure_ActionWord_LineMarker_Many(Meta, constructor):
        assert Meta.__name__.endswith('_1')

        Actionword_LineMarker_Many = lookup_adjusted_meta(Meta)

        if Actionword_LineMarker_Many is none:
            class Actionword_LineMarker_Many(Meta):
                __slots__ = ((
                    'newlines',                                 #   Integer > 1
                ))

                __init__ = constructor



            if python_debug_mode:
                Actionword_LineMarker_Many.__name__ = intern_arrange('%s_Many', Meta.__name__[:-2])

            store_adjusted_meta(Meta, Actionword_LineMarker_Many)

        return Actionword_LineMarker_Many
