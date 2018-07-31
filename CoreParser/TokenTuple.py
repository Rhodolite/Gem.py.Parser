#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.TokenTuple')
def module():
    require_module('CoreParser.ClassOrder')
    require_module('CoreParser.Nub')


    @export
    class TokenTuple(Tuple):
        __slots__   = (())
        class_order = CLASS_ORDER__TUPLE


        def __repr__(t):
            return arrange('<%s %s>', t.__class__.__name__, ' '.join(portray(v)   for v in t))


        def count_newlines(t):
            return sum(v.count_newlines()   for v in t)


        def display_token(t):
            return arrange('<%s %s>', t.display_name, ' '.join(v.display_token()   for v in t))


        nub = static_conjure_nub


        def order(a, b):
            if a is b:  return 0

            r = a.class_order - b.class_order

            if r < 0:   return -1
            if r > 0:   return 1

            a_total = length(a)
            b_total = length(b)
            total   = minimum(a_total, b_total)

            a_next = next_method(iterate(a))
            b_next = next_method(iterate(b))

            while total:
                r = a_next().order(b_next())

                if r < 0:   return -1
                if r > 0:   return 1

                total -= 1

            if a_total < b_total:   return -1
            if a_total > b_total:   return 1

            my_line('a_total: %d', a_total)
            my_line('b_total: %d', b_total)

            a_next = next_method(iterate(a))
            b_next = next_method(iterate(b))
            total  = minimum(a_total, b_total)

            while total:
                a = a_next()
                b = b_next()

                my_line('a: %r', a)
                my_line('b: %r', b)
                my_line('is: %s', a is b)
                total -= 1

                if a is not b:
                    line('a.a: %r', a.a)
                    line('b.a: %r', b.a)
                    my_line('is: %s', a.a is b.a)

                    line('a.b: %r', a.b)
                    line('b.b: %r', b.b)
                    my_line('is: %s', a.b is b.b)

                    line('a.frill: %r', a.frill)
                    line('b.frill: %r', b.frill)
                    my_line('is: %s', a.frill is b.frill)

            raise_runtime_error('a<%r> == b<%r>: but not identical', a, b)


        def write(t, w):
            for v in t:
                v.write(w)
