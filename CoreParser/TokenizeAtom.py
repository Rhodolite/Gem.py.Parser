#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.TokenizeAtom')
def module():
    #
    #   Note:
    #       Below a few tests of `i == j` (or the equivalent `qi() = qj()`).
    #
    #       None of these tests can be optimized to `i is j` since [the original] `i` & `j` could have been created
    #       with two different calls, such as:
    #
    #           1.  m.end('atom'); .vs.
    #           2.  m.end()
    #
    #       with `ow` is empty -- and thus have the same value (but different internal addresses).
    #
    #   Note #2:
    #       The previous note also applies to tests like `qi() != j` ... cannot replace this with `qi() is not j`.
    #
    def analyze_CRYSTAL_close_operator(m, operator_s):
        #
        #   A `close` operator does not grab it's following whitespace.
        #
        #   Hence:
        #
        #       The operator ends at `operator_end`
        #
        #   The whitespace is given to the next token, as follows:
        #
        #       wi(operator_end)
        #       wj(m.end())
        #
        #   That is:
        #
        #       The spaces between `operator_end` and `m.end()` are given to the next token.
        #
        d = qd()

        if d is 0:
            #my_line('d: %d; operator_s: %r; s: %s', d, operator_s, portray_string(s[qj() : ]))
            raise_unknown_line()

        assert d > 0

        operator_end = m.end('operator')

        r = conjure_action_word(operator_s, qs()[qi() : operator_end])

        wd(d - 1)
        wi(operator_end)
        wj(m.end())

        return r



    @export
    def produce_analyze_LANGUAGE_functions(
            language,
            has_open_operator,
            find_evoke_LANGUAGE__comma_something,
            find_LANGUAGE_atom_type,
            lookup_LANGUAGE_keyword_conjure_function,
            LANGUAGE__skip_tokenize_prefix,
    ):
        #
        #   analyze_LANGUAGE_* (without `newline` in the name)
        #
        @rename('analyze_%s_comma_operator', language)
        def analyze_LANGUAGE_comma_operator(m):
            suffix_start = m.start('comma_suffix')

            if suffix_start is not -1:
                d = qd()

                if d is 0:
                    raise_unknown_line()

                assert d > 0

                suffix_end = m.end('comma_suffix')

                suffix = qs()[suffix_start : suffix_end]

                r = find_evoke_LANGUAGE__comma_something(suffix)(suffix_start, suffix_end, suffix)

                wd(d - 1)
                wi(suffix_end)
                wj(m.end())

                return r

            j = m.end()

            r = conjure_CRYSTAL_comma(qs()[qi() : j])

            wi(j)
            wj(j)

            return r


        @rename('analyze_%s_keyword_atom', language)
        def analyze_LANGUAGE_keyword_atom(m, atom_s):
            conjure = lookup_LANGUAGE_keyword_conjure_function(atom_s)

            if conjure is not none:
                j = m.end()

                r = conjure(qs()[qi() : j])

                wi(j)
                wj(j)

                return r

            atom_end = m.end('atom')

            if qi() != qj():
                r = find_evoke_crystal_whitespace_atom(atom_s[0])(qj(), atom_end)
            else:
                r = find_LANGUAGE_atom_type(atom_s[0])(atom_s)

            wi(atom_end)
            wj(m.end())

            return r


        if has_open_operator:
            @export
            @rename('analyze_%s_operator', language)
            def analyze_LANGUAGE_operator(m, operator_s):
                operator_type = is_CRYSTAL_close_or_open_operator(operator_s)

                if operator_type is 7:
                    return analyze_CRYSTAL_close_operator(m, operator_s)

                j = m.end()

                #line('analyze_%s_operator: %r', language, qs()[qi() : j])

                r = conjure_action_word(operator_s, qs()[qi() : j])

                if operator_type is 3:
                    wd(qd() + 1)

                wi(j)
                wj(j)

                return r
        else:
            @export
            @rename('analyze_%s_operator', language)
            def analyze_LANGUAGE_operator(m, operator_s):
                if is_CRYSTAL_close_or_open_operator(operator_s) is 7:
                    return analyze_CRYSTAL_close_operator(m, operator_s)

                j = m.end()

                r = conjure_action_word(operator_s, qs()[qi() : j])

                wi(j)
                wj(j)

                return r


        @rename('analyze_%s_quote', language)
        def analyze_LANGUAGE_quote(m, quote_start):
            j         = qj()
            quote_end = m.end('quote')

            if qi() != j:
                r = find_evoke_crystal_whitespace_atom(qs()[quote_start])(j, quote_end)
            else:
                s = qs()

                r = find_LANGUAGE_atom_type(s[quote_start])(s[j : quote_end])

            wi(quote_end)
            wj(m.end())

            return r



        #
        #   analyze_LANGUAGE_newline_* (with `newline` in the name)
        #
        @rename('analyze_%s_newline_comma_operator', language)
        def analyze_LANGUAGE_newline_comma_operator(m):
            suffix_start = m.start('comma_suffix')

            if suffix_start is not -1:
                d = qd()

                if d is 1:
                    s          = qs()
                    suffix_end = m.end('comma_suffix')

                    suffix = qs()[suffix_start : suffix_end]

                    r = find_evoke_LANGUAGE__comma_something(suffix)(suffix_start, suffix_end, suffix)

                    wd0()

                    wn(conjure_line_marker(s[suffix_end : ]))

                    return r

                suffix = qs()[suffix_start : ]

                r = find_evoke_LANGUAGE__comma_something(suffix)(suffix_start, none, suffix)

                assert d > 1

                wd(d - 1)

                PYTHON__skip_tokenize_prefix()

                return r

            if qd() is 0:
                raise_unknown_line()

            r = conjure_CRYSTAL_comma__ends_in_newline(qs()[qi() : ])

            LANGUAGE__skip_tokenize_prefix()

            return r


        @rename('analyze_%s_newline_keyword_atom', language)
        def analyze_LANGUAGE_newline_keyword_atom(m, atom_s):
            conjure = lookup_LANGUAGE_keyword_conjure_function(atom_s)

            if conjure is not none:
                if qd() is 0:
                    atom_end = m.end('atom')

                    r = conjure(atom_s)(qs()[qi() : atom_end])

                    wn(conjure_line_marker(s[atom_end : ]))

                    return r

                r = conjure(atom_s)(qs()[qi() : ])

                LANGUAGE__skip_tokenize_prefix()

                return r

            #
            #<similiar-to: `analyze_LANGUAGE_newline_quote` below>
            #
            #       1.  Uses `atom_s[0]` instead of `qs()[quote_quote_start]`
            #       2.  Uses "m.end('atom')" instead of "m.end('quote')"
            #       3.  Uses "qs()" intead of "s"
            #
            if qd() is not 0:
                if qi() == qj():
                    r = find_evoke_crystal_atom_whitespace(atom_s[0])(m.end('atom'), none)
                else:
                    r = find_evoke_crystal_whitespace_atom_whitespace(atom_s[0])(qj(), m.end('atom'), none)

                LANGUAGE__skip_tokenize_prefix()

                return r

            atom_end = m.end('atom')

            if qi() == qj():
                r = find_LANGUAGE_atom_type(atom_s[0])(atom_s)
            else:
                r = find_evoke_crystal_whitespace_atom(atom_s[0])(qj(), m.end('atom'))

            wn(conjure_line_marker(qs()[atom_end : ]))

            return r
            #</similiar-to>


        @rename('analyze_%s_newline_close_operator', language)
        def analyze_LANGUAGE_newline_close_operator(m, operator_s):
            d = qd()

            if d is 1:
                operator_end = m.end('operator')
                s            = qs()

                r = conjure_action_word(operator_s, s[qi() : operator_end])

                wd0()
                wn(conjure_line_marker(s[operator_end : ]))

                return r

            if d < 1:
                raise_unknown_line()

            wd(d - 1)

            r = conjure_action_word__ends_in_newline(operator_s, qs()[qi() : ])

            LANGUAGE__skip_tokenize_prefix()

            return r


        if has_open_operator:
            @rename('analyze_%s_newline_operator', language)
            def analyze_LANGUAGE_newline_operator(m, operator_s):
                operator_type = is_CRYSTAL_close_or_open_operator(operator_s)

                if operator_type is 7:
                    return analyze_LANGUAGE_newline_close_operator(m, operator_s)

                if operator_type is 3:
                    wd(qd() + 1)
                else:
                    if qd() is 0:
                        operator_end = m.end('operator')

                        s = qs()

                        r = conjure_action_word(operator_s, s[qi() : operator_end])

                        wn(conjure_line_marker(s[operator_end : ]))

                        return r

                r = conjure_action_word__ends_in_newline(operator_s, qs()[qi() : ])

                LANGUAGE__skip_tokenize_prefix()

                return r
        else:
            @rename('analyze_%s_newline_operator', language)
            def analyze_LANGUAGE_newline_operator(m, operator_s):
                if is_CRYSTAL_close_or_open_operator(operator_s) is 7:
                    return analyze_LANGUAGE_newline_close_operator(m, operator_s)

                if qd() is 0:
                    operator_end = m.end('operator')

                    s = qs()

                    r = conjure_action_word(operator_s, s[qi() : operator_end])

                    wn(conjure_line_marker(s[operator_end : ]))

                    return r

                r = conjure_action_word__ends_in_newline(operator_s, qs()[qi() : ])

                LANGUAGE__skip_tokenize_prefix()

                return r


        def analyze_LANGUAGE_newline_quote(m, quote_start):
            #
            #   NOTE:
            #
            #       In the code below: Use 'qj()' instead of "m.start('quote')" to be sure to pick up any letters
            #       prefixing the quote, such as r'prefixed'
            #

            #
            #<similiar-to: `analyze_LANGUAGE_newline_keyword_atom` above>
            #
            #   See list of differences there
            #
            if qd() is not 0:
                if qi() == qj():
                    r = find_evoke_crystal_atom_whitespace(qs()[quote_start])(m.end('quote'), none)
                else:
                    r = find_evoke_crystal_whitespace_atom_whitespace(qs()[quote_start])(qj(), m.end('quote'), none)

                LANGUAGE__skip_tokenize_prefix()

                return r

            atom_end = m.end('quote')
            s        = qs()

            if qi() == qj():
                r = find_LANGUAGE_atom_type(s[quote_start])(s[qj() : atom_end])
            else:
                r = find_evoke_crystal_whitespace_atom(s[quote_start])(qj(), atom_end)

            wn(conjure_line_marker(s[atom_end : ]))

            return r
            #</similiar-to>


        return ((
                   analyze_LANGUAGE_comma_operator,
                   analyze_LANGUAGE_keyword_atom,
                   analyze_LANGUAGE_operator,
                   analyze_LANGUAGE_quote,

                   analyze_LANGUAGE_newline_comma_operator,
                   analyze_LANGUAGE_newline_keyword_atom,
                   analyze_LANGUAGE_newline_operator,
                   analyze_LANGUAGE_newline_quote,
               ))
