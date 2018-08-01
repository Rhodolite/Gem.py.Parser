#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Method')
def module():
    #
    #   add_parameters
    #
    @share
    def add_parameters__0(t, art):
        pass


    @share
    def add_parameters__a(t, art):
        t.a.add_parameters(art)


    #
    #   adorn
    #
    if 0:
        @share
        def produce_adorn__ab(name, conjure):
            @rename('adorn_%s', name)
            def adorn(t, art):
                a = t.a
                b = t.b

                a__2 = a.adorn(art)
                b__2 = b.adorn(art)

                if (a is a__2) and (b is b__2):
                    return t

                return conjure(a__2, b__2)


            return adorn


    #
    #   find_require_module
    #
    @share
    def find_require_module__b(t, e):
        t.b.find_require_module(e)


    #
    #   mutate
    #
    @share
    def produce_mutate__ab(name, conjure):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            a = t.a
            b = t.b

            a__2 = a.mutate(vary, priority)
            b__2 = b.mutate(vary, priority)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)


        return mutate


    @share
    def produce__mutate__ab__priority(name, conjure, a_priority, b_priority):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            a = t.a
            b = t.b

            a__2 = a.mutate(vary, a_priority)
            b__2 = b.mutate(vary, b_priority)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)


        return mutate


    @share
    def produce_mutate__abc(name, conjure):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            a = t.a
            b = t.b
            c = t.c

            a__2 = a.mutate(vary, priority)
            b__2 = b.mutate(vary, priority)
            c__2 = c.mutate(vary, priority)

            if (a is a__2) and (b is b__2) and (c is c__2):
                return t

            return conjure(a__2, b__2, c__2)


        return mutate


    @share
    def produce_mutate__abcd(name, conjure):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            a = t.a
            b = t.b
            c = t.c
            d = t.d

            a__2 = a.mutate(vary, priority)
            b__2 = b.mutate(vary, priority)
            c__2 = c.mutate(vary, priority)
            d__2 = d.mutate(vary, priority)

            if (a is a__2) and (b is b__2) and (c is c__2) and (d is d__2):
                return t

            return conjure(a__2, b__2, c__2, d__2)


        return mutate


    #
    #   NOTE:
    #       Very similiar to `produce_mutate__frill__ab_with_priority`, but uses a `conjure` instead of `conjure_with_frill`
    #       for the last parameter
    #
    #       See also notes in `produce_transform__binary_expression` for a further explanation.
    #
    @share
    def produce_mutate__binary_expression(name, a_priority, b_priority, conjure):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, a_priority)
            b__2     = b    .mutate   (vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, frill__2, b__2)


        return mutate


    @share
    def produce_mutate__frill__a__priority(name, priority):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a

            frill__2 = frill.mutate(vary, priority)
            a__2     = a    .mutate(vary, priority)

            if (frill is frill__2) and (a is a__2):
                return t

            return t.conjure_with_frill(frill__2, a__2)


        return mutate


    @share
    def produce_mutate__frill__a_with_priority(name, a_priority, conjure_with_frill):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, a_priority)

            if (frill is frill__2) and (a is a__2):
                return t

            return conjure_with_frill(frill__2, a__2)


        return mutate


    #
    #   NOTE:
    #       Very similiar to `produce_mutate__binary_expression`, but calls `frill.mutate` (instead of `.transform`)
    #
    @share
    def produce_mutate__map_element(name, frill_priority, a_priority, b_priority, conjure):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.mutate(vary, frill_priority)
            a__2     = a    .mutate(vary, a_priority)
            b__2     = b    .mutate(vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, frill__2, b__2)


        return mutate


    @share
    def produce_mutate__frill__ab_with_priority(name, a_priority, b_priority, conjure_with_frill):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, a_priority)
            b__2     = b    .mutate   (vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure_with_frill(frill__2, a__2, b__2)


        return mutate


    @share
    def produce_mutate__frill__many(name, first_priority, middle_priority, last_priority, conjure_with_frill):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            frill = t.frill
            many  = t.many

            frill__2 = frill .transform(vary)
            many__2  = t.many.morph    (vary, first_priority, middle_priority, last_priority)

            if (frill is frill__2) and (many is many__2):
                return t

            return conjure_with_frill(frill__2, many__2)


        return mutate


    #
    #   order
    #
    @share
    def order__frill_a(a, b):
        a_order = a.class_order
        b_order = b.class_order

        if a_order is b_order:
            return (a.frill.order(b.frill)) or (a.a.order(b.a))

        if a_order < b_order:
            return -1

        assert a_order > b_order

        return 1


    @share
    def order__frill_abc(a, b):
        a_order = a.class_order
        b_order = b.class_order

        if a_order is b_order:
            return (a.frill.order(b.frill)) or (a.a.order(b.a)) or (a.b.order(b.b)) or (a.c.order(b.c))

        if a_order < b_order:
            return -1

        assert a_order > b_order

        return 1


    #
    #   parameters_1_named
    #
    @share
    def parameters_1_named__false(t, name):
        return false


    #
    #   scout_default_values
    #
    @share
    def scout_default_values__a(t, art):
        t.a.scout_default_values(art)


    #
    #   scout_variables
    #
    @share
    def scout_variables__a(t, art):
        t.a.scout_variables(art)


    @share
    def scout_variables__a__b_with_write(t, art):
        t.a.scout_variables(art)
        t.b.write_variables(art)


    @share
    def scout_variables__a_with_write__b(t, art):
        t.a.write_variables(art)
        t.b.scout_variables(art)


    @share
    def scout_variables__abc(t, art):
        t.a.scout_variables(art)
        t.b.scout_variables(art)
        t.c.scout_variables(art)


    @share
    def scout_variables__abcd(t, art):
        t.a.scout_variables(art)
        t.b.scout_variables(art)
        t.c.scout_variables(art)
        t.d.scout_variables(art)


    @share
    def scout_variables__tuple(t, art):
        for v in t:
            v.scout_variables(art)


    #
    #   transform
    #
    @share
    def produce_transform__a__b_with_indentation(name, conjure):
        @rename('transform_%s', name)
        def transform(t, vary):
            a = t.a
            b = t.b

            a__2 = a.transform(vary)

            if 'clique':
                previous = vary.push_indentation()

                b__2 = b.transform(vary)

                vary.pop_indentation(previous)

            if (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, b__2)


        return transform


    #
    #   produce_transform__binary_expression
    #
    #       NOTE:
    #           This is very similiar to `produce_transform__frill__ab_with_priority`, but with
    #           a slight optimization:
    #
    #               1.  The fourth parameter is `conjure` instead of `conjure_with_frill`
    #
    #               2.  The final call (since it is a binary expression) is with `frill__2` as
    #                   the middle parameter (instead of the first parameter).
    #
    #           Thus this version *only* works for `frill` that does not need to be a first
    #           parameter (i.e.: a binary expression -- which only has one middle frill).
    #
    #       (Also `produce_transform__binary_expression` does not take a `frill_morph_priority`
    #       optional parameter).
    #
    @share
    def produce_transform__binary_expression(name, a_priority, b_priority, conjure):
        @rename('transform_%s', name)
        def transform(t, vary):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, a_priority)
            b__2     = b    .mutate   (vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure(a__2, frill__2, b__2)


        return transform


    @share
    def produce_transform__frill_a(name, conjure_with_frill):
        @rename('transform_%s', name)
        def transform(t, vary):
            frill = t.frill
            a     = t.a

            frill__2 = frill.transform(vary)
            a__2     = a    .transform(vary)

            if (frill is frill__2) and (a is a__2):
                return t

            return conjure_with_frill(frill__2, a__2)


        return transform


    @share
    def produce_transform__frill_ab(name, conjure_with_frill):
        @rename('transform_%s', name)
        def transform(t, vary):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .transform(vary)
            b__2     = b    .transform(vary)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure_with_frill(frill__2, a__2, b__2)


        return transform


    @share
    def produce_transform__frill__a_with_priority(name, priority, conjure_with_frill):
        @rename('transform_%s', name)
        def transform(t, vary):
            frill = t.frill
            a     = t.a

            frill__2 = frill.transform(vary)
            a__2     = a    .mutate   (vary, priority)

            if (frill is frill__2) and (a is a__2):
                return t

            return conjure_with_frill(frill__2, a__2)


        return transform


    @share
    def produce_transform__frill__a__b_with_priority(name, b_priority, conjure_with_frill):
        @rename('transform_%s', name)
        def transform(t, vary):
            frill = t.frill
            a     = t.a
            b     = t.b

            frill__2 = frill.transform(vary)
            a__2     = a    .transform(vary)
            b__2     = b    .mutate(vary, b_priority)

            if (frill is frill__2) and (a is a__2) and (b is b__2):
                return t

            return conjure_with_frill(frill__2, a__2, b__2)


        return transform


    @share
    def produce_transform__frill__ab_with_priority(
            name, a_priority, b_priority, conjure_with_frill,

            frill_morph_priority = none,
    ):
        if frill_morph_priority is none:
            @rename('transform_%s', name)
            def transform(t, vary):
                frill = t.frill
                a     = t.a
                b     = t.b

                frill__2 = frill.transform(vary)
                a__2     = a    .mutate   (vary, a_priority)
                b__2     = b    .mutate   (vary, b_priority)

                if (frill is frill__2) and (a is a__2) and (b is b__2):
                    return t

                return conjure_with_frill(frill__2, a__2, b__2)
        else:
            #
            #   This version is used by `FromImportStatement` since `.morph` has to be called on `frill_2`
            #   to indicate that the `AS` keyword is used in a statement context instead of an expression context.
            #
            @rename('transform_%s', name)
            def transform(t, vary):
                frill = t.frill
                a     = t.a
                b     = t.b

                frill__2 = frill.morph (vary, 0, frill_morph_priority, 0)
                a__2     = a    .mutate(vary, a_priority)
                b__2     = b    .mutate(vary, b_priority)

                if (frill is frill__2) and (a is a__2) and (b is b__2):
                    return t

                return conjure_with_frill(frill__2, a__2, b__2)

        return transform


    @share
    def produce_transform__frill__many(name, many_priority, conjure_with_frill):
        @rename('transform_%s', name)
        def transform(t, vary):
            frill    = t.frill
            many     = t.many
            iterator = iterate(many)

            frill_2 = frill.transform(vary)

            i = 0

            for v in iterator:
                v__2 = v.transform(vary)

                if v is not v__2:
                    break

                i += 1
            else:
                if frill is frill_2:
                    return t

                return conjure_with_frill(frill__2, many)

            many__2 = (
                          []          if i is 0 else
                          [many[0]]   if i is 1 else
                          List(many[:i])
                      )

            append = many__2.append

            append(v__2)

            for v in iterator:
                append(v.transform(vary))

            return conjure_with_frill(frill_2, conjure_tuple_of_many_expression(many__2))


        return transform


    #
    #   write_variables
    #
    @share
    def write_variables__a(t, art):
        t.a.write_variables(art)


    @share
    def write_variables__ab(t, art):
        t.a.write_variables(art)
        t.b.write_variables(art)


    @share
    def write_variables__many(t, art):
        for v in t.many:
            v.write_variables(art)
