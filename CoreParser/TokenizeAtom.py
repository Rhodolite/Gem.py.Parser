#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.TokenizeAtom')
def module():
    @export
    def produce_analyze_keyword_atom(
            lookup_language_keyword_conjure_function, find_language_evoke_whitespace_atom, find_language_atom_type,
    ):
        def analyze_keyword_atom(m, atom_s):
            conjure = lookup_language_keyword_conjure_function(atom_s)

            if conjure is not none:
                j = m.end()

                r = conjure(qs()[qi() : j])

                wi(j)
                wj(j)

                return r

            atom_end = m.end('atom')

            if qi() != qj():
                r = find_language_evoke_whitespace_atom(atom_s[0])(qj(), atom_end)
            else:
                r = find_language_atom_type(atom_s[0])(atom_s)

            wi(atom_end)
            wj(m.end())

            return r

        return analyze_keyword_atom
