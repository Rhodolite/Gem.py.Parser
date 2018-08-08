#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.TripleToken')
def module():
    require_module('PythonParser.CreateMeta')
    require_module('PythonParser.DualStatement')
    require_module('PythonParser.Elemental')


    def add_comment__commented_statement(t, comment):
        return conjure_commented_statement(comment, t)


    def construct_triple_operator__line_marker_1(t, s, a, b, c):
        assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
        assert s == a.s + b.s + c.s
        assert s.count('\n') is 1
        assert c.s[-1] == '\n'

        t.s = s
        t.a = a
        t.b = b
        t.c = c


    def construct_triple_token__line_marker__many(t, s, a, b, c, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines > 1)
        assert s == a.s + b.s + c.s
        assert s.count('\n') == newlines
        assert c.s[-1] == '\n'

        t.s        = s
        t.a        = a
        t.b        = b
        t.c        = c
        t.newlines = newlines


    def dump_token__indented__keyword__line_marker(t, f, newline = true):
        f.partial('<%s +%d ', t.display_name, t.a.total)

        t    .b.dump_token(f)
        r = t.c.dump_token(f, false)

        return f.token_result(r, newline)


    def produce_transform__indented__keyword__c(name, conjure, keyword, uncommented_c):
        @rename('transform_%s', name)
        def transform(t, vary):
            a = t.a
            b = t.b
            c = t.c

            a__2 = (vary.indentation   if vary.remove_indentation else   a)

            if vary.remove_comments:
                b__2 = keyword
                c__2 = uncommented_c

                if (a is a__2) and (b is b__2) and (c is c__2):
                    return t

                return conjure(a__2, b__2, c__2)

            if a is a__2:
                return t

            return conjure(a__2, b, c)


        return transform


    def produce_mutate_whitespace_atom_whitespace(name, conjure):
        @rename('mutate_%s', name)
        def mutate(t, vary, priority):
            b    = t.b
            b__2 = b.mutate(vary, priority)

            if vary.remove_comments:
                return b__2

            a = t.a
            c = t.c

            a__2 = a.transform(vary)
            c__2 = c.transform(vary)

            if (a is a__2) and (b is b__2) and (c is c__2):
                return t

            return conjure(a__2, b__2, c__3)


        return mutate


    class AllIndex(TripleToken):
        __slots__           = (())
        display_name        = '[:]'
        is_all_index        = true
        is_postfix_operator = true

        scout_variables = scout_variables__0


    class DotNameTriplet(TripleToken):
        __slots__           = (())
        display_name        = '.name-triplet'
        is_postfix_operator = true


    class Indented_Break_LineMarker_1(TripleToken):
        __slots__   = (())
        indentation = TripleToken.a

        class_order                = CLASS_ORDER__INDENTED__KEYWORD__LINE_MARKER
        display_name               = r'indented-break\n'
        ends_in_newline            = true
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        line_marker                = true
        newlines                   = 1

        __init__            = construct_triple_operator__line_marker_1
        add_comment         = add_comment__commented_statement
        count_newlines      = count_newlines__line_marker
        dump_token          = dump_token__indented__keyword__line_marker
        find_require_module = find_require_module__0
        scout_variables     = scout_variables__0


    class Indented_Continue_LineMarker_1(TripleToken):
        __slots__   = (())
        indentation = TripleToken.a

        class_order                = CLASS_ORDER__INDENTED__KEYWORD__LINE_MARKER
        display_name               = r'indented-continue\n'
        ends_in_newline            = true
        indentation                = TripleToken.a
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        line_marker                = true
        newlines                   = 1

        __init__            = construct_triple_operator__line_marker_1
        add_comment         = add_comment__commented_statement
        count_newlines      = count_newlines__line_marker
        dump_token          = dump_token__indented__keyword__line_marker
        find_require_module = find_require_module__0
        scout_variables     = scout_variables__0


    class Indented_Else_Colon(TripleToken):
        __slots__    = (())
        display_name = r'indented-else:'
        indentation  = TripleToken.a

        scout_variables = scout_variables__0


    class Indented_Pass_LineMarker_1(TripleToken):
        __slots__   = (())
        indentation = TripleToken.a

        class_order                = CLASS_ORDER__INDENTED__KEYWORD__LINE_MARKER
        display_name               = r'indented-pass\n'
        ends_in_newline            = true
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        line_marker                = true
        newlines                   = 1

        __init__            = construct_triple_operator__line_marker_1
        add_comment         = add_comment__commented_statement
        count_newlines      = count_newlines__line_marker
        dump_token          = dump_token__indented__keyword__line_marker
        find_require_module = find_require_module__0
        scout_variables     = scout_variables__0


    class Indented_Raise_LineMarker_1(TripleToken):
        __slots__   = (())
        indentation = TripleToken.a

        class_order                = CLASS_ORDER__INDENTED__KEYWORD__LINE_MARKER
        display_name               = r'indented-raise\n'
        ends_in_newline            = true
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        line_marker                = true
        newlines                   = 1

        __init__            = construct_triple_operator__line_marker_1
        add_comment         = add_comment__commented_statement
        count_newlines      = count_newlines__line_marker
        dump_token          = dump_token__indented__keyword__line_marker
        find_require_module = find_require_module__0
        scout_variables     = scout_variables__0


    class Indented_Return_LineMarker_1(TripleToken):
        __slots__   = (())
        indentation = TripleToken.a

        class_order                = CLASS_ORDER__INDENTED__KEYWORD__LINE_MARKER
        display_name               = r'indented-return\n'
        ends_in_newline            = true
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        line_marker                = true
        newlines                   = 1

        __init__            = construct_triple_operator__line_marker_1
        add_comment         = add_comment__commented_statement
        count_newlines      = count_newlines__line_marker
        dump_token          = dump_token__indented__keyword__line_marker
        find_require_module = find_require_module__0
        scout_variables     = scout_variables__0


    class Indented_Yield_LineMarker_1(TripleToken):
        __slots__   = (())
        indentation = TripleToken.a

        class_order                = CLASS_ORDER__INDENTED__KEYWORD__LINE_MARKER
        display_name               = r'indented-yield\n'
        ends_in_newline            = true
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true
        line_marker                = true
        newlines                   = 1

        __init__            = construct_triple_operator__line_marker_1
        add_comment         = add_comment__commented_statement
        count_newlines      = count_newlines__line_marker
        dump_token          = dump_token__indented__keyword__line_marker
        find_require_module = find_require_module__0
        scout_variables     = scout_variables__0


    #
    #   conjure_*
    #
    conjure_all_index__with_newlines = produce_conjure_triple_token__with_newlines('all_index', AllIndex)

    conjure_dot_name_triplet__with_newlines = produce_conjure_triple_token__with_newlines(
            '.name-triplet',
            DotNameTriplet,
        )

    conjure_indented__break__line_marker = produce_conjure_triple_token__line_marker(
            'indented__break__line_marker',
            Indented_Break_LineMarker_1,
        )

    conjure_indented__continue__line_marker = produce_conjure_triple_token__line_marker(
            'indented__continue__line_marker',
            Indented_Continue_LineMarker_1,
        )

    conjure_indented_else_colon__with_newlines = produce_conjure_triple_token__with_newlines(
            'indented-else-colon',
            Indented_Else_Colon,
        )

    conjure_indented__pass__line_marker = produce_conjure_triple_token__line_marker(
            'indented__pass__line_marker',
            Indented_Pass_LineMarker_1,
        )

    conjure_indented__raise__line_marker = produce_conjure_triple_token__line_marker(
            'indented__raise__line_marker',
            Indented_Raise_LineMarker_1,
        )

    conjure_indented__return__line_marker = produce_conjure_triple_token__line_marker(
            'indented__return__line_marker',
            Indented_Return_LineMarker_1,
        )

    conjure_indented__yield__line_marker = produce_conjure_triple_token__line_marker(
            'indented__yield__line_marker',
            Indented_Yield_LineMarker_1,
        )

    conjure_whitespace_atom_whitespace__with_newlines = produce_conjure_triple_token__with_newlines(
            'whitespace_atom_whitespace',
            Whitespace_Atom_Whitespace,
        )

    conjure_whitespace_name_whitespace = produce_conjure_triple_token__with_newlines(
            'whitespace_name_whitespace',
            Whitespace_Name_Whitespace,
        )


    #
    #   evoke_*
    #
    evoke_all_index = produce_evoke_triple_token__ends_in_newline(
            'all_index',
            AllIndex,
            conjure_left_square_bracket,
            conjure_colon,
            conjure_right_square_bracket,
            conjure_right_square_bracket__ends_in_newline,
        )


    evoke_indented__break__line_marker = produce_evoke_triple_token__line_marker(
            'indented__break__line_marker',
            Indented_Break_LineMarker_1,
            conjure_indentation,
            conjure_keyword_break,
        )

    evoke_indented__continue__line_marker = produce_evoke_triple_token__line_marker(
            'indented__continue__line_marker',
            Indented_Continue_LineMarker_1,
            conjure_indentation,
            conjure_keyword_continue,
        )

    evoke_indented_else_colon = produce_evoke_triple_token__ends_in_newline(
            'indented_else_colon',
            Indented_Else_Colon,
            conjure_indentation,
            conjure_keyword_else,
            conjure_colon,
            conjure_colon__ends_in_newline,
        )

    evoke_indented__pass__line_marker = produce_evoke_triple_token__line_marker(
            'indented__pass__line_marker',
            Indented_Pass_LineMarker_1,
            conjure_indentation,
            conjure_keyword_pass,
        )

    evoke_indented__raise__line_marker = produce_evoke_triple_token__line_marker(
            'indented__raise__line_marker',
            Indented_Raise_LineMarker_1,
            conjure_indentation,
            conjure_keyword_return,
        )

    evoke_indented__return__line_marker = produce_evoke_triple_token__line_marker(
            'indented__return__line_marker',
            Indented_Return_LineMarker_1,
            conjure_indentation,
            conjure_keyword_return,
        )

    evoke_indented__yield__line_marker = produce_evoke_triple_token__line_marker(
            'indented__yield__line_marker',
            Indented_Yield_LineMarker_1,
            conjure_indentation,
            conjure_keyword_yield,
        )


    #
    #   Constants
    #
    ALL_INDEX = conjure_all_index__with_newlines(LSB, COLON, RSB)


    #
    #   .mutate
    #
    DotNameTriplet.mutate = produce_mutate__abc('dot_name_triplet', conjure_dot_name_triplet__with_newlines)

    Whitespace_Atom_Whitespace.mutate = produce_mutate_whitespace_atom_whitespace(
            'whitespace_atom_whitespace',
            conjure_whitespace_atom_whitespace__with_newlines,
        )

    Whitespace_Name_Whitespace.mutate = produce_mutate_whitespace_atom_whitespace(
            'whitespace_name_whitespace',
            conjure_whitespace_name_whitespace,
        )


    #
    #   .mutate
    #
    AllIndex.mutate = produce_mutate__uncommented('all_index', ALL_INDEX)

    Indented_Break_LineMarker_1.transform = produce_transform__indented__keyword__c(
            'indented_break__line_marker_1',
            conjure_indented__break__line_marker,
            BREAK,
            LINE_MARKER,
        )

    Indented_Continue_LineMarker_1.transform = produce_transform__indented__keyword__c(
            'indented_continue__line_marker_1',
            conjure_indented__continue__line_marker,
            CONTINUE,
            LINE_MARKER,
        )

    Indented_Else_Colon.transform = produce_transform__indented__keyword__c(
            'indented_else_colon',
            conjure_indented_else_colon__with_newlines,
            ELSE,
            COLON,
        )

    Indented_Pass_LineMarker_1.transform = produce_transform__indented__keyword__c(
            'indented_pass__line_marker_1',
            conjure_indented__pass__line_marker,
            PASS,
            LINE_MARKER,
        )

    Indented_Raise_LineMarker_1.transform = produce_transform__indented__keyword__c(
            'indented_raise__line_marker_1',
            conjure_indented__raise__line_marker,
            RAISE,
            LINE_MARKER,
        )

    Indented_Return_LineMarker_1.transform = produce_transform__indented__keyword__c(
            'indented_return__line_marker_1',
            conjure_indented__return__line_marker,
            RETURN,
            LINE_MARKER,
        )

    Indented_Yield_LineMarker_1.transform = produce_transform__indented__keyword__c(
            'indented_yield__line_marker_1',
            conjure_indented__yield__line_marker,
            YIELD,
            LINE_MARKER,
        )

    share(
        'conjure_all_index__with_newlines',                     conjure_all_index__with_newlines,
        'conjure_dot_name_triplet__with_newlines',              conjure_dot_name_triplet__with_newlines,
        'conjure_indented__pass__line_marker',                  conjure_indented__pass__line_marker,
        'conjure_whitespace_atom_whitespace__with_newlines',    conjure_whitespace_atom_whitespace__with_newlines,
        'evoke_all_index',                                      evoke_all_index,
        'evoke_indented__break__line_marker',                   evoke_indented__break__line_marker,
        'evoke_indented__continue__line_marker',                evoke_indented__continue__line_marker,
        'evoke_indented_else_colon',                            evoke_indented_else_colon,
        'evoke_indented__pass__line_marker',                    evoke_indented__pass__line_marker,
        'evoke_indented__raise__line_marker',                   evoke_indented__raise__line_marker,
        'evoke_indented__return__line_marker',                  evoke_indented__return__line_marker,
        'evoke_indented__yield__line_marker',                   evoke_indented__yield__line_marker,
    )
