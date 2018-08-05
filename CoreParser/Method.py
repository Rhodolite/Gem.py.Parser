#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.Method')
def module():
    #
    #   add_parameters
    #
    if PYTHON_parser:
        @share
        def add_parameters__b(t, art):
            t.b.add_parameters(art)


    #
    #   construct
    #
    if CRYSTAL_parser:
        @share
        def construct__ab(t, a, b):
            t.a = a
            t.b = b


    if CRYSTAL_parser:
        @export
        def construct__123(t, k1, k2, k3):
            t.k1 = k1
            t.k2 = k2
            t.k3 = k3


    #
    #   count_newlines
    #
    if CRYSTAL_parser:
        @share
        def count_newlines__ab(t):
            return t.a.count_newlines() + t.b.count_newlines()


    if CRYSTAL_parser:
        @export
        def count_newlines__123(t):
            return t.k1.count_newlines() + t.k2.count_newlines() + t.k3.count_newlines()


    #
    #   display_token
    #
    if CRYSTAL_parser:
        @share
        def display_token__ab(t):
            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


    if CRYSTAL_parser:
        @export
        def display_token__123(t):
            return arrange('<%s %s %s %s>',
                           t.display_name,
                           t.k1.display_token(),
                           t.k2.display_token(),
                           t.k3.display_token())


    if CRYSTAL_parser:
        @export
        def display_token__ab__with_braces(t):
            return arrange('{%s %s %s}', t.display_name, t.a.display_token(), t.b.display_token())


    if CRYSTAL_parser:
        @export
        def display_token__with_angle_signs(t):
            return arrange('<%s>', t.s)


    #
    #   dump_token
    #
    def produce_dump_token(suffix, left, right):
        left__percent_s__right = left + '%s' + right
        percent_s__right       = '%s' + right


        @rename('dump_token__with_%s', suffix)
        def dump_token__with_SUFFIX(t, f, newline = true):
            if t.ends_in_newline:
                if t.newlines is 1:
                    f.partial(left__percent_s__right, portray_string(t.s)[1:-1])
                else:
                    many = t.s.splitlines(true)

                    f.partial(left)

                    for s in many[:-1]:
                        f.line(portray_string(s)[1:-1])

                    f.partial(percent_s__right, portray_string(many[-1])[1:-1])

                if newline:
                    f.line()
                    return false

                return true

            if t.newlines is 0:
                f.partial(left__percent_s__right, portray_string(t.s)[1:-1])
                return

            many = t.s.splitlines(true)

            f.partial(left)

            for s in many[:-1]:
                f.line(portray_string(s)[1:-1])

            f.partial(percent_s__right, portray_string(many[-1])[1:-1])


        return dump_token__with_SUFFIX


    dump_token__with_angle_signs = produce_dump_token('angles', '<', '>')
    dump_token__with_braces      = produce_dump_token('braces', '{', '}')


    export(
        'dump_token__with_angle_signs',     dump_token__with_angle_signs,
    )


    share(
        'dump_token__with_braces',  dump_token__with_braces,
    )


    if CRYSTAL_parser:
        @share
        def dump_token__12(t, f, newline = true):
            f.partial('<%s ', t.display_name)

            t    .k1.dump_token(f)
            r = t.k2.dump_token(f, false)

            return f.token_result(r, newline)


    if CRYSTAL_parser:
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
    if PYTHON_parser:
        @export
        def find_require_module__0(t, e):
            pass


    #
    #   is_name
    #
    if PYTHON_parser:
        @export
        def is_name__0(t, name):
            return false


    #
    #   mutate
    #
    if PYTHON_parser:
        @export
        def mutate__self(t, vary, priority):
            return t


    if PYTHON_parser:
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


    @share
    def order__abcd(a, b):
        a_order = a.class_order
        b_order = b.class_order

        if a_order is b_order:
            return (a.a.order(b.a)) or (a.b.order(b.b)) or (a.c.order(b.c)) or (a.d.order(b.d))

        if a_order < b_order:
            return -1

        assert a_order > b_order

        return 1


    @export
    def order__frill_a(a, b):
        a_order = a.class_order
        b_order = b.class_order

        if a_order is b_order:
            return (a.frill.order(b.frill)) or (a.a.order(b.a))

        if a_order < b_order:
            return -1

        assert a_order > b_order

        return 1


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


    @export
    def order__frill_many(a, b):
        a_order = a.class_order
        b_order = b.class_order

        if a_order is b_order:
            return (a.frill.order(b.frill)) or (a.many.order(b.many))

        if a_order < b_order:
            return -1

        assert a_order > b_order

        return 1


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


    @share
    def order__string(a, b):
        if a < b:   return -1
        if a > b:   return 1

        return 0


    #
    #   portray
    #
    if CRYSTAL_parser:
        @export
        def portray__ab(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.a, t.b)


    if CRYSTAL_parser:
        @export
        def portray__123(t):
            return arrange('<%s %s %r %r>', t.__class__.__name__, t.k1, t.k2, t.k3)


    if CRYSTAL_parser:
        @export
        def portray_with_braces(t):
            return arrange('{%s %r %r}', t.__class__.__name__, t.a, t.b)


    #
    #   scout_default_values
    #
    if PYTHON_parser:
        @export
        def scout_default_values__0(t, art):
            pass


    if PYTHON_parser:
        @share
        def scout_default_values__b(t, art):
            t.b.scout_default_values(art)



    #
    #   scout_variables
    #
    if PYTHON_parser:
        @export
        def scout_variables__0(t, art):
            pass


    if PYTHON_parser:
        @export
        def scout_variables__a(t, art):
            t.a.scout_variables(art)


    if PYTHON_parser:
        @export
        def scout_variables__ab(t, art):
            t.a.scout_variables(art)
            t.b.scout_variables(art)


    if PYTHON_parser:
        @export
        def scout_variables__b(t, art):
            t.b.scout_variables(art)


    if PYTHON_parser:
        @export
        def scout_variables__many(t, art):
            for v in t.many:
                v.scout_variables(art)


    #
    #   transform
    #
    if PYTHON_parser:
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


    if PYTHON_parser:
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


    if PYTHON_parser:
        @export
        def produce_transform__abcd(name, conjure):
            @rename('transform_%s', name)
            def transform(t, vary):
                a = t.a
                b = t.b
                c = t.c
                d = t.d

                a__2 = a.transform(vary)
                b__2 = b.transform(vary)
                c__2 = c.transform(vary)
                d__2 = d.transform(vary)

                if (a is a__2) and (b is b__2) and (c is c__2) and (d is d__2):
                    return t

                return conjure(a__2, b__2, c__2, d__2)


            return transform


    if PYTHON_parser:
        @export
        def produce_transform_many(name, conjure):
            @rename('transform_%s', name)
            def transform(t, vary):
                iterator = iterate(t)

                i = 0

                for v in iterator:
                    v__2 = v.transform(vary)

                    if v is not v__2:
                        break

                    i += 1
                else:
                    return t

                many__2 = (
                              []       if i is 0 else
                              [t[0]]   if i is 1 else
                              List(t[:i])
                          )

                append = many__2.append

                append(v__2)

                for v in iterator:
                    append(v.transform(vary))

                return conjure(many__2)


            return transform


    if PYTHON_parser:
        @export
        def produce_transform__uncommented(name, uncommented):
            @rename('transform_%s', name)
            def transform(t, vary):
                if vary.remove_comments:
                    return uncommented

                return t


            return transform


    if PYTHON_parser:
        @export
        def transform__remove_comments_0(t, vary):
            if vary.remove_comments:
                return 0

            return t


    if PYTHON_parser:
        @export
        def transform__self(t, vary):
            return t


    #
    #   write
    #
    if CRYSTAL_parser:
        @share
        def write__123(t, w):
            t.k1.write(w)
            t.k2.write(w)
            t.k3.write(w)


    #
    #   write_variables
    #
    if PYTHON_parser:
        @share
        def write_variables__b(t, art):
            t.b.write_variables(art)


    if PYTHON_parser:
        @export
        def write_variables__a(t, art):
            t.a.write_variables(art)
