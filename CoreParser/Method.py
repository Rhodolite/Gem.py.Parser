#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CoreParser.Method')
def gem():
    #
    #   is_name
    #
    @export
    def is_name__0(t, name):
        return false


    #
    #   mutate
    #
    @export
    def mutate__self(t, vary, priority):
        return t


    #
    #   order__s
    #
    @export
    def order__s(a, b):
        a_order = a.class_order
        b_order = b.class_order

        if a_order is b_order:
            if a.s < b.s:   return -1
            if a.s > b.s:   return 1

            return 0

        if a_order < b_order: return -1

        assert a_order > b_order

        return 1


    #
    #   scout_default_values
    #
    @share
    def scout_default_values__0(t, art):
        pass


    #
    #   transform
    #
    @export
    def transform__self(t, vary):
        return t
