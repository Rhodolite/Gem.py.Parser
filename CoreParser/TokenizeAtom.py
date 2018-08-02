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

    #
    #   produce_analyze_LANGUAGE_* (without `newline` in the name)
    #
    @export
    def produce_analyze_LANGUAGE_keyword_atom(
            language, find_LANGUAGE_atom_type, lookup_LANGUAGE_keyword_conjure_function,
    ):
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


        return analyze_LANGUAGE_keyword_atom


    @export
    def produce_analyze_LANGUAGE_quote(language, find_LANGUAGE_atom_type):
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


        return analyze_LANGUAGE_quote


    #
    #   produce_analyze_LANGUAGE_newline_* (without `newline` in the name)
    #
    @export
    def produce_analyze_LANGUAGE_newline_keyword_atom(
            language,
            find_LANGUAGE_atom_type,
            lookup_LANGUAGE_keyword_conjure_function,
            LANGUAGE__skip_tokenize_prefix,
    ):
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


        return analyze_LANGUAGE_newline_keyword_atom


    @export
    def produce_analyze_LANGUAGE_newline_quote(
            language,
            find_LANGUAGE_atom_type,
            LANGUAGE__skip_tokenize_prefix,
    ):
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


        return analyze_LANGUAGE_newline_quote
