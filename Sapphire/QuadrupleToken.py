#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.QuadrupleToken')
def gem():
    require_gem('Sapphire.CreateMeta')


    def construct_quadruple_token(t, s, a, b, c, d):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert s == a.s + b.s + c.s + d.s
        assert '\n' not in s

        t.s = s
        t.a = a
        t.b = b
        t.c = c
        t.d = d


    if 0:
        def construct_quadruple_token__with_newlines(t, s, a, b, c, d, ends_in_newline, newlines):
            assert t.line_marker is false
            assert s == a.s + b.s + c.s + d.s
            assert ends_in_newline is (d.s[-1] == '\n')
            assert newlines >= 1

            t.s               = s
            t.a               = a
            t.b               = b
            t.c               = c
            t.d               = d
            t.ends_in_newline = ends_in_newline
            t.newlines        = newlines


    def construct_quadruple_operator__line_marker_1(t, s, a, b, c, d):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s == a.s + b.s + c.s + d.s
        assert s.count('\n') is 1
        assert d.s[-1] == '\n'

        t.s = s
        t.a = a
        t.b = b
        t.c = c
        t.d = d


    def construct_quadruple_token__line_marker__many(t, s, a, b, c, d, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines > 1)
        assert s == a.s + b.s + c.s + d.s
        assert s.count('\n') == newlines
        assert d.s[-1] == '\n'

        t.s        = s
        t.a        = a
        t.b        = b
        t.c        = c
        t.d        = d
        t.newlines = newlines


    def dump_token__indented__keyword__colon__line_marker(t, f, newline = true):
        f.partial('<%s +%d ', t.display_name, t.a.total)

        t    .b.dump_token(f)
        t    .c.dump_token(f)
        r = t.d.dump_token(f, false)

        return f.token_result(r, newline)


    def display_token__indented__keyword__colon__line_marker(t):
        return arrange('<%s +%d %s %s %s>',
                       t.display_name,
                       t.a.total,
                       t.b.display_token(),
                       t.c.display_token(),
                       t.d.display_token())


    def produce_transform__indented__keyword__colon__line_marker(name, conjure, keyword):
        @rename('transform_%s', name)
        def transform(t, vary):
            a = t.a
            b = t.b
            c = t.c
            d = t.d

            a__2 = (vary.indentation   if vary.remove_indentation else   a)

            if vary.remove_comments:
                b__2 = keyword
                c__2 = COLON
                d__2 = LINE_MARKER

                if (a is a__2) and (b is b__2) and (c is c__2) and (d is d__2):
                    return t

                return conjure(a__2, b__2, c__2, d__2)

            if a is a__2:
                return t

            return conjure(a__2, b, c, d)


        return transform


    class BaseQuadrupleOperator(KeywordAndOperatorBase):
        __slots__ = ((
            'a',                        #   Operator+
            'b',                        #   Operator+
            'c',                        #   Operator+
            'd',                        #   Operator+
        ))


        __init__ = construct_quadruple_token


        def __repr__(t):
            return arrange('<%s %r %r %r %r>', t.__class__.__name__, t.a, t.b, t.c, t.d)


        def display_full_token(t):
            display_name = t.display_name
            a_s          = t.a.s
            b_s          = t.b.s
            c_s          = t.c.s
            d_s          = t.d.s

            return arrange('<%s <%s> <%s> <%s> <%s>>',
                           display_name,
                           (portray_string(a_s)   if '\n' in a_s else   a_s),
                           (portray_string(b_s)   if '\n' in b_s else   b_s),
                           (portray_string(c_s)   if '\n' in b_s else   c_s),
                           (portray_string(d_s)   if '\n' in d_s else   d_s))


        def display_token(t):
            display_name = t.display_name

            if display_name == t.s:
                return display_name

            a_s = t.a.s
            b_s = t.b.s
            c_s = t.c.s
            d_s = t.d.s

            return arrange('<%s <%s> <%s> <%s> <%s>>',
                           display_name,
                           (portray_string(a_s)   if '\n' in a_s else   a_s),
                           (portray_string(b_s)   if '\n' in b_s else   b_s),
                           (portray_string(c_s)   if '\n' in c_s else   c_s),
                           (portray_string(d_s)   if '\n' in d_s else   d_s))


    def create_quadruple_token__with_newlines(Meta, s, a, b, c, d):
        assert s == a.s + b.s + c.s + d.s

        newlines = s.count('\n')

        return (
                   Meta(s, a, b, c, d)
                       if newlines is 0 else
                           conjure_ActionWord_WithNewlines(
                               Meta, construct_quadruple_token__with_newlines,
                           )(s, a, b, c, d, s[-1] == '\n', newlines)
               )


    def create_quadruple_token__line_marker(Meta, s, a, b, c, d):
        assert (s == a.s + b.s + c.s + d.s) and (s[-1] == '\n')

        newlines = s.count('\n')

        return (
                   Meta(s, a, b, c, d)
                       if newlines is 1 else
                           conjure_ActionWord_LineMarker_Many(
                               Meta, construct_quadruple_token__line_marker__many,
                           )(s, a, b, c, d, newlines)
               )


    def produce_conjure_quadruple_token(
            name, Meta,

            lookup      = lookup_normal_token,
            provide     = provide_normal_token,
            line_marker = false
    ):
        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)

            create_quadruple_token = create_quadruple_token__line_marker
            lookup                 = lookup_line_marker
            provide                = provide_line_marker
        else:
            create_quadruple_token = create_quadruple_token__with_newlines


        @rename('conjure_%s', name)
        def conjure_quadruple_token(a, b, c, d):
            s = a.s + b.s + c.s + d.s

            r = lookup(s)

            if r is not none:
                assert (r.a is a) and (r.b is b) and (r.c is c) and (r.d is d)

                return r

            s = intern_string(s)

            return provide(s, create_quadruple_token(Meta, s, a, b, c, d))


        return conjure_quadruple_token


    def produce_evoke_quadruple_token(
            name, Meta, conjure_a, conjure_b, conjure_c,

            conjure_d                  = absent,
            conjure_d__ends_in_newline = absent,
            lookup                     = lookup_normal_token,
            provide                    = provide_normal_token,
            line_marker                = false,
    ):
        assert type(line_marker) is Boolean


        if line_marker:
            assert (lookup is lookup_normal_token) and (provide is provide_normal_token)
            assert (conjure_d is conjure_d__ends_in_newline is absent)


            @rename('evoke_%s', name)
            def evoke_quadruple_token(a_end, b_end, c_end):
                #
                #   Note: 'qi() <= a_end', since for indented token there might be no indentation
                #
                assert qi() <= a_end < b_end < c_end

                full = qs()[qi() : ]

                r = lookup_line_marker(full)

                if r is not none:
                    assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                    return r

                full = intern_string(full)
                s    = qs()

                return provide_line_marker(
                           full,
                           create_quadruple_token__line_marker(
                               Meta,
                               full,
                               conjure_a          (s[qi()  : a_end]),
                               conjure_b          (s[a_end : b_end]),
                               conjure_c          (s[b_end : c_end]),
                               conjure_line_marker(s[c_end :      ]),
                           ),
                       )
        else:
            @rename('evoke_%s', name)
            def evoke_quadruple_token(a_end, b_end, c_end, d_end):
                assert qi() < a_end < b_end < c_end < d_end

                full = qs()[qi() : d_end]

                r = lookup(full)

                if r is not none:
                    assert (type(r) is Meta) or (type(r) is lookup_adjusted_meta(Meta))

                    return r

                full = intern_string(full)
                s    = qs()

                return provide(
                           full,
                           create_quadruple_token__with_newlines(
                               Meta,
                               full,
                               conjure_a(s[qi()  : a_end]),
                               conjure_b(s[a_end : b_end]),
                               conjure_c(s[b_end : c_end]),
                               (conjure_d__ends_in_newline   if d_end is none else   conjure_d)(s[c_end : d_end]),
                           ),
                       )


        return evoke_quadruple_token


    class DotNameQuadruplet(BaseQuadrupleOperator):
        __slots__           = (())
        class_order         = CLASS_ORDER__NORMAL_TOKEN
        #   [
        display_name        = '.name-quadruplet'
        is_postfix_operator = true


    @share
    class Indented_Else_Colon_LineMarker(BaseQuadrupleOperator):
        __slots__                  = (())
        class_order                = CLASS_ORDER__LINE_MARKER
        display_name               = 'else'
        ends_in_newline            = true
        is_any_else                = true
        is_any_except_or_finally   = false
        is_else_header_or_fragment = true
        is_statement               = false
        is_statement_header        = true
        keyword                    = 'else'
        line_marker                = true
        newlines                   = 1
        split_comment              = 0

        __init__       = construct_quadruple_operator__line_marker_1
        add_comment    = 0
        count_newlines = count_newlines__line_marker
        display_token  = display_token__indented__keyword__colon__line_marker
        dump_token     = dump_token__indented__keyword__colon__line_marker
        indentation    = BaseQuadrupleOperator.a
        scout_variables = scout_variables__0


    @share
    class Indented_Except_Colon_LineMarker(BaseQuadrupleOperator):
        __slots__                = (())
        class_order              = CLASS_ORDER__LINE_MARKER
        display_name             = 'except'
        ends_in_newline          = true
        is_any_else              = false
        is_any_except_or_finally = true
        is_statement             = false
        is_statement_header      = true
        keyword                  = 'except'
        line_marker              = true
        newlines                 = 1
        split_comment            = 0

        __init__       = construct_quadruple_operator__line_marker_1
        add_comment    = 0
        count_newlines = count_newlines__line_marker
        display_token  = display_token__indented__keyword__colon__line_marker
        dump_token     = dump_token__indented__keyword__colon__line_marker
        indentation    = BaseQuadrupleOperator.a
        scout_variables = scout_variables__0


    @share
    class Indented_Finally_Colon_LineMarker(BaseQuadrupleOperator):
        __slots__                = (())
        class_order              = CLASS_ORDER__LINE_MARKER
        display_name             = 'finally'
        ends_in_newline          = true
        is_any_except_or_finally = true
        is_statement             = false
        is_statement_header      = true
        keyword                  = 'finally'
        line_marker              = true
        newlines                 = 1
        split_comment            = 0

        __init__       = construct_quadruple_operator__line_marker_1
        add_comment    = 0
        count_newlines = count_newlines__line_marker
        display_token  = display_token__indented__keyword__colon__line_marker
        dump_token     = dump_token__indented__keyword__colon__line_marker
        indentation    = BaseQuadrupleOperator.a
        scout_variables = scout_variables__0


    @share
    class Indented_Try_Colon_LineMarker(BaseQuadrupleOperator):
        __slots__           = (())
        class_order         = CLASS_ORDER__LINE_MARKER
        display_name        = 'try'
        ends_in_newline     = true
        is_any_else         = false
        is_statement        = false
        is_statement_header = true
        keyword             = 'try'
        line_marker         = true
        newlines            = 1
        split_comment       = 1

        __init__        = construct_quadruple_operator__line_marker_1
        add_comment     = 0
        count_newlines  = count_newlines__line_marker
        display_token   = display_token__indented__keyword__colon__line_marker
        dump_token      = dump_token__indented__keyword__colon__line_marker
        indentation     = BaseQuadrupleOperator.a
        scout_variables = scout_variables__0


    conjure_dot_name_quadruplet = produce_conjure_quadruple_token('.name-quadruplet', DotNameQuadruplet)

    conjure_indented__else__colon__line_marker = produce_conjure_quadruple_token(
                                                     'indented__else__colon__line_marker',
                                                     Indented_Else_Colon_LineMarker,

                                                     line_marker = true,
                                                 )

    conjure_indented__except__colon__line_marker = produce_conjure_quadruple_token(
                                                       'indented__except__colon__line_marker',
                                                       Indented_Except_Colon_LineMarker,

                                                       line_marker = true,
                                                   )

    conjure_indented__finally__colon__line_marker = produce_conjure_quadruple_token(
                                                       'indented__finally__colon__line_marker',
                                                       Indented_Finally_Colon_LineMarker,

                                                       line_marker = true,
                                                   )

    conjure_indented__try__colon__line_marker = produce_conjure_quadruple_token(
                                                    'indented__try__colon__line_marker',
                                                    Indented_Try_Colon_LineMarker,

                                                    line_marker = true,
                                                )

    evoke_indented__else__colon__line_marker = produce_evoke_quadruple_token(
            'indented__else__colon__line_marker',
            Indented_Else_Colon_LineMarker,
            conjure_indentation,
            conjure_keyword_else,
            conjure_colon,

            line_marker = true,
        )

    evoke_indented__except__colon__line_marker = produce_evoke_quadruple_token(
            'indented__except__colon__line_marker',
            Indented_Except_Colon_LineMarker,
            conjure_indentation,
            conjure_keyword_except,
            conjure_colon,

            line_marker = true,
        )

    evoke_indented__finally__colon__line_marker = produce_evoke_quadruple_token(
            'indented__finally__colon__line_marker',
            Indented_Finally_Colon_LineMarker,
            conjure_indentation,
            conjure_keyword_finally,
            conjure_colon,

            line_marker = true,
        )

    evoke_indented__try__colon__line_marker = produce_evoke_quadruple_token(
            'indented__try__colon__line_marker',
            Indented_Try_Colon_LineMarker,
            conjure_indentation,
            conjure_keyword_try,
            conjure_colon,

            line_marker = true,
        )


    #
    #   .mutate
    #
    DotNameQuadruplet.mutate = produce_mutate__abcd('dot_name_quadruplet', conjure_dot_name_quadruplet)


    #
    #   .transform
    #
    Indented_Else_Colon_LineMarker.transform = produce_transform__indented__keyword__colon__line_marker(
                                                   'indented_else_colon__line_marker',
                                                   conjure_indented__else__colon__line_marker,
                                                   ELSE,
                                               )

    Indented_Except_Colon_LineMarker.transform = produce_transform__indented__keyword__colon__line_marker(
                                                     'indented_except_colon__line_marker',
                                                     conjure_indented__except__colon__line_marker,
                                                     EXCEPT,
                                                 )

    Indented_Finally_Colon_LineMarker.transform = produce_transform__indented__keyword__colon__line_marker(
                                                      'indented_finally__line_marker',
                                                      conjure_indented__finally__colon__line_marker,
                                                      FINALLY,
                                                  )

    Indented_Try_Colon_LineMarker.transform = produce_transform__indented__keyword__colon__line_marker(
                                                  'indented_try_colon__line_marker',
                                                  conjure_indented__try__colon__line_marker,
                                                  TRY,
                                              )


    share(
        'conjure_dot_name_quadruplet',                          conjure_dot_name_quadruplet,
        'evoke_indented__else__colon__line_marker',             evoke_indented__else__colon__line_marker,
        'evoke_indented__except__colon__line_marker',           evoke_indented__except__colon__line_marker,
        'evoke_indented__finally__colon__line_marker',          evoke_indented__finally__colon__line_marker,
        'evoke_indented__try__colon__line_marker',              evoke_indented__try__colon__line_marker,
    )
