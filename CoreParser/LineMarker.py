#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.LineMarker')
def module():
    require_module('CoreParser.Core')
    require_module('CoreParser.ClassOrder')
    require_module('CoreParser.Method')
    require_module('CoreParser.ParserToken')


    def construct_token__line_marker__many(t, s, newlines):
        assert (t.ends_in_newline is t.line_marker is true) and (newlines > 1)

        t.s        = s
        t.newlines = newlines


    class LineMarker(ParserToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__LINE_MARKER
        display_name = 'line-marker'


        if capital_global.crystal_parser:
            ends_in_newline = true
            line_marker     = true
            newlines        = 1


        if capital_global.python_parser:
            is_end_of_boolean_and_expression        = true
            is_end_of_boolean_or_expression         = true
            is_end_of_compare_expression            = true
            is_end_of_comprehension_expression_list = true
            is_end_of_comprehension_expression      = true
            is_end_of_logical_and_expression        = true
            is_end_of_logical_or_expression         = true
            is_end_of_multiply_expression           = true
            is_end_of_normal_expression_list        = true
            is_end_of_normal_expression             = true
            is_end_of_python_arithmetic_expression  = true
            is_end_of_ternary_expression_list       = true
            is_end_of_ternary_expression            = true
            is_end_of_unary_expression              = true


        if capital_global.tremolite_parser:
            is_end_of_tremolite_arithmetic_expression = true
            is_end_of_tremolite_unary_expression      = true


        def __init__(t, s):
            assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
            assert (s.count('\n') == 1) and (s[-1] == '\n')

            t.s = s


        def count_newlines(t):
            assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
            assert (t.s.count('\n') == 1) and (t.s[-1] == '\n')

            return 1


        def display_token(t):
            return arrange('<line-marker %s>', portray_string(t.s))


        def dump_token(t, f, newline = true):
            assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
            assert (t.s.count('\n') == 1) and (t.s[-1] == '\n')

            f.partial('{%s}', portray_string(t.s)[1:-1])

            if newline:
                f.line()
                return false

            return true


        order = order__s


    @export
    def conjure_line_marker(s):
        r = lookup_line_marker(s)

        if r is not none:
            return r

        s = intern_string(s)

        return provide_line_marker(s, LineMarker(s))


    if capital_global.python_parser:
        @export
        def produce_conjure_action_word__line_marker(name, Meta):
            @rename('conjure_%s__line_marker', name)
            def conjure_action_word__line_marker(s):
                assert s[-1] == '\n'

                r = lookup_line_marker(s)

                if r is not none:
                    return r

                s = intern_string(s)

                newlines = s.count('\n')

                return provide_line_marker(
                           s,
                           (
                               Meta(s)
                                   if newlines is 1 else
                                       conjure_ActionWord_LineMarker_Many(
                                           Meta, construct_token__line_marker__many,
                                       )(s, s.count('\n'))
                           ),
                       )


            return conjure_action_word__line_marker


    LINE_MARKER = conjure_line_marker('\n')


    if capital_global.python_parser:
        LineMarker.mutate    = produce_mutate__uncommented   ('line_marker', LINE_MARKER)
        LineMarker.transform = produce_transform__uncommented('line_marker', LINE_MARKER)


    export(
        'LINE_MARKER',    LINE_MARKER,
    )
