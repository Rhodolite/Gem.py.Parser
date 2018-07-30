#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.Method')
def module():
    require_module('CoreParser.Core')


    #
    #   construct
    #
    if capital_global.crystal_parser:
        @share
        def construct__ab(t, a, b):
            t.a = a
            t.b = b


    if capital_global.crystal_parser:
        @export
        def construct__123(t, k1, k2, k3):
            t.k1 = k1
            t.k2 = k2
            t.k3 = k3


    #
    #   count_newlines
    #
    if capital_global.crystal_parser:
        @share
        def count_newlines__ab(t):
            return t.a.count_newlines() + t.b.count_newlines()


    if capital_global.crystal_parser:
        @export
        def count_newlines__123(t):
            return t.k1.count_newlines() + t.k2.count_newlines() + t.k3.count_newlines()


    #
    #   display_token
    #
    if capital_global.crystal_parser:
        @share
        def display_token__ab(t):
            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


    if capital_global.crystal_parser:
        @export
        def display_token__123(t):
            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.k1.display_token(),
                           t.k2.display_token(),
                           t.k3.display_token())


    #
    #   dump_token
    #
    if capital_global.crystal_parser:
        @share
        def dump_token__12(t, f, newline = true):
            f.partial('<%s ', t.display_name)

            t    .k1.dump_token(f)
            r = t.k2.dump_token(f, false)

            return f.token_result(r, newline)


    if capital_global.crystal_parser:
        @share
        def dump_token__123(t, f, newline = true):
            f.partial('<%s ', t.display_name)

            t    .k1.dump_token(f)
            t    .k2.dump_token(f)
            r = t.k3.dump_token(f, false)

            return f.token_result(r, newline)


    #
    #   find_require_module
    #
    if capital_global.python_parser:
        @export
        def find_require_module__0(t, e):
            pass


    #
    #   is_name
    #
    if capital_global.python_parser:
        @export
        def is_name__0(t, name):
            return false


    #
    #   mutate
    #
    if capital_global.python_parser:
        @export
        def mutate__self(t, vary, priority):
            return t


    if capital_global.python_parser:
        @export
        def produce_mutate__uncommented(name, uncommented):
            @rename('mutate_%s', name)
            def mutate(t, vary, priority):
                if vary.remove_comments:
                    return uncommented

                return t


            return mutate


    #
    #   order
    #
    if capital_global.python_parser:
        @export
        def order__ab(a, b):
            a_order = a.class_order
            b_order = b.class_order

            if a_order is b_order:
                return (a.a.order(b.a)) or (a.b.order(b.b))

            if a_order < b_order:
                return -1

            assert a_order > b_order

            return 1


    if capital_global.python_parser:
        @export
        def order__abc(a, b):
            a_order = a.class_order
            b_order = b.class_order

            if a_order is b_order:
                return (a.a.order(b.a)) or (a.b.order(b.b)) or (a.c.order(b.c))

            if a_order < b_order:
                return -1

            assert a_order > b_order

            return 1


    if capital_global.python_parser:
        @export
        def order__frill_ab(a, b):
            a_order = a.class_order
            b_order = b.class_order

            if a_order is b_order:
                return (a.frill.order(b.frill)) or (a.a.order(b.a)) or (a.b.order(b.b))

            if a_order < b_order:
                return -1

            assert a_order > b_order

            return 1



    if capital_global.python_parser:
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
    #   order__string
    #
    if capital_global.python_parser:
        @share
        def order__string(a, b):
            if a < b:   return -1
            if a > b:   return 1

            return 0


    #
    #   portray
    #
    if capital_global.crystal_parser:
        @export
        def portray__ab(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


    if capital_global.crystal_parser:
        @export
        def portray__123(t):
            return arrange('<%s %s %r %r>', t.__class__.__name__, t.k1, t.k2, t.k3)


    #
    #   scout_default_values
    #
    if capital_global.python_parser:
        @export
        def scout_default_values__0(t, art):
            pass


    #
    #   scout_variables
    #
    if capital_global.python_parser:
        @export
        def scout_variables__0(t, art):
            pass


    #
    #   transform
    #
    if capital_global.python_parser:
        @export
        def produce_transform__ab(name, conjure):
            @rename('transform_%s', name)
            def transform(t, vary):
                a = t.a
                b = t.b

                a__2 = a.transform(vary)
                b__2 = b.transform(vary)

                if (a is a__2) and (b is b__2):
                    return t

                return conjure(a__2, b__2)


            return transform


    if capital_global.python_parser:
        @export
        def produce_transform__abc(name, conjure):
            @rename('transform_%s', name)
            def transform(t, vary):
                a = t.a
                b = t.b
                c = t.c

                a__2 = a.transform(vary)
                b__2 = b.transform(vary)
                c__2 = c.transform(vary)

                if (a is a__2) and (b is b__2) and (c is c__2):
                    return t

                return conjure(a__2, b__2, c__2)


            return transform


    if capital_global.python_parser:
        @export
        def produce_transform__uncommented(name, uncommented):
            @rename('transform_%s', name)
            def transform(t, vary):
                if vary.remove_comments:
                    return uncommented

                return t


            return transform


    if capital_global.python_parser:
        @export
        def transform__remove_comments_0(t, vary):
            if vary.remove_comments:
                return 0

            return t


    if capital_global.python_parser:
        @export
        def transform__self(t, vary):
            return t


    #
    #   write
    #
    if capital_global.crystal_parser:
        @share
        def write__123(t, w):
            t.k1.write(w)
            t.k2.write(w)
            t.k3.write(w)
