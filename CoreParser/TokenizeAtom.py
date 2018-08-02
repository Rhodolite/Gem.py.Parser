#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.TokenizeAtom')
def module():
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
