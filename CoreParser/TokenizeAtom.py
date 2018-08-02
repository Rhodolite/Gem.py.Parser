#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.TokenizeAtom')
def module():
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
            #<similiar-to: {quote_s} below>
            #
            #   Differences:
            #
            #       Uses "m.end('atom')" instead of "quote_end"
            #       Uses "qs()" intead of "s"
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
