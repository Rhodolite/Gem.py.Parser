#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.DualToken')
def module():
    def construct_dual_token__with_newlines(t, s, a, b, ends_in_newline, newlines):
        assert t.line_marker is false
        assert s == a.s + b.s
        assert ends_in_newline is (b.s[-1] == '\n')
        assert newlines >= 1

        t.s               = s
        t.a               = a
        t.b               = b
        t.ends_in_newline = ends_in_newline
        t.newlines        = newlines


    def create_dual_token__with_newlines(Meta, s, a, b):
        assert s == a.s + b.s

        newlines = s.count('\n')

        return (
                   Meta(s, a, b)
                       if newlines is 0 else
                           conjure_ActionWord_WithNewlines(
                                Meta, construct_dual_token__with_newlines,
                           )(s, a, b, s[-1] == '\n', newlines)
               )


    #
    #<create_dual_token>
    #   produce_create_dual_token__line_marker
    #   produce_create_dual_token__normal
    #       Two slightly different versions ...
    #
    def produce_conjure_dual_token__X__helper(name, Meta, create_dual_token, lookup, provide):
        @rename('conjure_%s', name)
        def conjure_dual_token(a, b):
            s = a.s + b.s

            r = lookup(s)

            if r is not none:
                assert (r.a is a) and (r.b is b)

                return r

            s = intern_string(s)

            return provide(s, create_dual_token(Meta, s, a, b))


        return conjure_dual_token


    def create_dual_token__line_marker(Meta, s, a, b):
        assert (s == a.s + b.s) and (s[-1] == '\n')

        newlines = s.count('\n')

        return (
                   Meta(s, a, b)
                       if newlines is 1 else
                           conjure_ActionWord_LineMarker_Many(
                                Meta, construct_dual_token__line_marker__many
                           )(s, a, b, newlines)
               )


    @export
    def produce_conjure_dual_token__normal(
            name, Meta,

            lookup      = lookup_normal_token,
            provide     = provide_normal_token,
    ):
        return produce_conjure_dual_token__X__helper(name, Meta, create_dual_token__with_newlines, lookup, provide)


    @export
    def produce_conjure_dual_token__line_marker(name, Meta):
        return produce_conjure_dual_token__X__helper(
                name, Meta, create_dual_token__line_marker, lookup_line_marker, provide_line_marker,
            )
    #</produce_conjure_dual_token>


    #
    #<produce_evoke_dual_token>
    #   produce_evoke_dual_token__ends_in_newline
    #   produce_evoke_dual_token__indentation
    #   produce_evoke_dual_token__line_marker
    #       Three slightly different versions ...
    #
    def produce_evoke_dual_token__X__indentation_or_whitespace(
            name, Meta, conjure_first, conjure_second, lookup, provide,
    ):
        @rename('evoke_%s', name)
        def evoke_dual_token__X__indentation_or_whitespace(middle, end):
            #
            #   Indentation tokens may have 0 length, hence 'qi() <= middle'
            #
            assert qi() <= middle < end

            full = qs()[qi() : end]

            r = lookup(full)

            if r is not none:
                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            full = intern_string(full)
            s    = qs()

            return provide(
                       full,
                       create_dual_token__with_newlines(
                           Meta,
                           full,
                           conjure_first (s[qi()   : middle]),
                           conjure_second(s[middle : end   ]),
                       ),
                   )


        return evoke_dual_token__X__indentation_or_whitespace


    @export
    def produce_evoke_dual_token__ends_in_newline(
            name, Meta, conjure_first, conjure_second, conjure_second__ends_in_newline,

            lookup  = lookup_normal_token,
            provide = provide_normal_token,
    ):
        @rename('evoke_%s', name)
        def evoke_dual_token__ends_in_newline(middle, end):
            if end is none:
                assert qi() < middle
            else:
                assert qi() < middle < end

            full = qs()[qi() : end]

            r = lookup(full)

            if r is not none:
                #if not ( (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta)) ):
                #    my_line('r: %r', r)
                #    my_line('Meta: %r', Meta)
                #    my_line('adjusted: %r', lookup_adjusted_meta(Meta))

                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            full = intern_string(full)
            s    = qs()

            return provide(
                       full,
                       create_dual_token__with_newlines(
                           Meta,
                           full,
                           conjure_first(s[qi() : middle]),
                           (conjure_second__ends_in_newline   if end is none else   conjure_second)(s[middle : end]),
                       ),
                   )


        return evoke_dual_token__ends_in_newline

    
    @export
    def produce_evoke_dual_token__indentation(name, Meta, conjure_first, conjure_second):
        return produce_evoke_dual_token__X__indentation_or_whitespace(
                name, Meta, conjure_first, conjure_second, lookup_indentation, provide_indentation,
            )


    @export
    def produce_evoke_dual_token__line_marker(name, Meta, conjure_first):
        @rename('evoke_%s', name)
        def evoke_dual_token__line_marker(a_end):
            assert qi() < a_end

            full_s = qs()[qi() : ]

            r = lookup_line_marker(full_s)

            if r is not none:
                assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                return r

            s      = qs()
            full_s = intern_string(full_s)

            return provide_line_marker(
                       full_s,
                       create_dual_token__line_marker(
                           Meta,
                           full_s,
                           conjure_first      (s[qi()  : a_end]),
                           conjure_line_marker(s[a_end :      ]),
                       ),
                   )


        return evoke_dual_token__line_marker


    @export
    def produce_evoke_dual_token__whitespace(name, Meta, conjure_first, conjure_second):
        return produce_evoke_dual_token__X__indentation_or_whitespace(
                name, Meta, conjure_first, conjure_second, lookup_normal_token, provide_normal_token,
            )
    #</produce_evoke_dual_token>


    @export
    class DualToken(KeywordAndOperatorBase):
        __slots__ = ((
            'a',                        #   Operator+
            'b',                        #   Operator+
        ))


        def __init__(t, s, a, b):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert '\n' not in s
            assert s == a.s + b.s

            t.s = s
            t.a = a
            t.b = b


        __repr__ = portray__ab


        if 0:                                                           #   Not currently used
            def display_full_token(t):
                display_name = t.display_name
                a_s          = t.a.s
                b_s          = t.b.s

                return arrange('<%s <%s> <%s>>',
                               display_name,
                               portray_string(a_s)   if '\n' in a_s else   a_s,
                               portray_string(b_s)   if '\n' in b_s else   b_s)


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return arrange('<%s>', display_name)

            a_s = t.a.s
            b_s = t.b.s

            return arrange('<%s <%s> <%s>>',
                           display_name,
                           portray_string(a_s)   if '\n' in a_s else   a_s,
                           portray_string(b_s)   if '\n' in b_s else   b_s)


        order = order__s
