#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.TokenizeName')
def module():
    def tokenize_name__X__newline(m):
        if qd() is not 0:
            if qi() == qj():
                r = evoke_name_whitespace(m.end('name'), none)
            else:
                r = evoke_whitespace_name_whitespace(qj(), m.end('name'), none)

            python__skip_tokenize_prefix()

            return r

        j        = qj()
        name_end = m.end('name')
        s        = qs()

        if qi() == j:
            r = conjure_name(s[j : name_end])
        else:
            r = evoke_whitespace_name(j, name_end)

        wn(conjure_line_marker(s[name_end : ]))

        return r


    @share
    def tokenize_name():
        assert qk() is none
        assert qn() is none

        j = qj()
        s = qs()

        m = name_ow_match(s, j)

        if m is none:
            raise_unknown_line()

        if m.start('comment_newline') is not -1:
            return tokenize_name__X__newline(m)

        name_end = m.end('name')

        r = conjure_name(s[j : name_end])

        if qi() != j:
            r = conjure_whitespace_identifier(conjure_whitespace(s[qi() : j]), r)

        wi(name_end)
        wj(m.end())

        return r
