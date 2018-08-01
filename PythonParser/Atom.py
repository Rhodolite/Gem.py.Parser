#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Atom')
def module():
    require_module('PythonParser.Method')


    lookup_atom  = lookup_normal_token
    provide_atom = provide_normal_token


    def construct__quote_with_newlines(t, s, newlines):
        t.s        = s
        t.newlines = newlines


    def count_newlines__quote_with_newlines(t):
        assert t.s[-1] != '\n'
        assert t.ends_in_newline is t.line_marker is false
        assert t.newlines == t.s.count('\n')

        return t.newlines


    def produce_conjure_triple_quote__with_newlines(name, Meta):
        @rename('conjure_%s__with_newlines', name)
        def conjure_triple_quote__with_newlines(s):
            assert s[-1] != '\n'

            r = lookup_atom(s)

            if r is not none:
                return r

            TripleXQuote_WithNewlines = lookup_adjusted_meta(Meta)

            if TripleXQuote_WithNewlines is none:
                class TripleXQuote_WithNewlines(Meta):
                    __slots__ = ((
                        'newlines',                                 #   Integer > 0
                    ))


                    __init__       = construct__quote_with_newlines
                    count_newlines = count_newlines__quote_with_newlines


                if python_debug_mode:
                    TripleXQuote_WithNewlines.__name__ = intern_arrange('%s_WithNewlines', Meta.__name__)

                store_adjusted_meta(Meta, TripleXQuote_WithNewlines)

            s = intern_string(s)

            return provide_atom(s, TripleXQuote_WithNewlines(s, s.count('\n')))


        return conjure_triple_quote__with_newlines


    @share
    def count_newlines__line_marker(t):
        assert (t.ends_in_newline is t.line_marker is true)
        assert t.s[-1] == '\n'
        assert t.newlines == t.s.count('\n')

        return t.newlines


    class EndOfData(ParserToken):
        __slots__                        = (())
        indentation                      = none
        is_comment_line                  = false
        is_comment__or__empty_line       = false
        is_any_else                      = false
        is_any_except_or_finally         = false
        is_else_header_or_fragment       = false
        is_end_of_data                   = true
        is_end_of_data__or__unknown_line = true
        is_statement_header              = false


        def __repr__(t):
            return t.s


    conjure_triple_double_quote__with_newlines = produce_conjure_triple_quote__with_newlines(
            'triple-double-quote',
            DoubleQuote,
        )

    conjure_triple_single_quote__with_newlines = produce_conjure_triple_quote__with_newlines(
            'triple-single-quote',
            SingleQuote,
        )

    end_of_data = EndOfData(intern_string('<end-of-data>'))


    share(
        'conjure_double_quote',                         conjure_double_quote,
        'conjure_token_number',                         conjure_token_number,
        'conjure_single_quote',                         conjure_single_quote,
        'conjure_triple_double_quote__with_newlines',   conjure_triple_double_quote__with_newlines,
        'conjure_triple_single_quote__with_newlines',   conjure_triple_single_quote__with_newlines,
        'end_of_data',                                  end_of_data,
    )
