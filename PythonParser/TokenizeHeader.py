#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.TokenizeHeader')
def module():
    @share
    def tokenize_header_parenthesis_atom():
        assert qd() is 0
        assert qk() is none
        assert qn() is none

        s = qs()

        m = definition_header_parenthesis_match(s, qj())

        if m is none:
            raise_unknown_line()

        RP_end = m.end('right_parenthesis')

        if m.start('comment_newline') is not -1:
            if RP_end is not -1:
                raise_unknown_line()

            r = conjure_left_parenthesis__ends_in_newline(s[qi() : ])

            wd1()
            PYTHON__skip_tokenize_prefix()

            return r

        if RP_end is not -1:
            r = evoke_parameters_0(m.start('right_parenthesis'), RP_end)

            wi(RP_end)
            wj(m.end())

            return r

        j = m.end()

        r = conjure_left_parenthesis(s[qi() : j])

        wd1()
        wi(j)
        wj(j)

        return r


    def tokenize_parameter_operator__X__right_parenthesis(m):
        s = qs()

        right_parenthesis__end = m.end('right_parenthesis')

        if m.end('comment_newline') is not -1:
            assert qi() == qj()

            my_line(portray_string(s[qi() : ]))
            my_line(portray_string(m.group('newline')))

            raise_unknown_line()

        r = conjure_right_parenthesis(s[qi() : right_parenthesis__end])

        wd0()
        wi(right_parenthesis__end)
        wj(m.end())

        return r


    @share
    def tokenize_parameter_atom():
        assert qd() is 1
        assert qk() is none
        assert qn() is none

        j = qj()
        s = qs()

        m = parameter_atom_match(s, j)

        if m is none:
            #my_line(portray_string(qs()[qj() : ]))
            raise_unknown_line()

        name = m.group('name')

        if name is not none:
            if m.start('comment_newline') is not -1:
                raise_unknown_line()

            star_end = m.end('star')

            if star_end is -1:
                if qi() != j:
                    name_end = m.end('name')

                    r = evoke_whitespace_name(j, name_end)

                    wi(name_end)
                    wj(m.end())

                    return r

                r = conjure_name(name)

                wi(m.end('name'))
                wj(m.end())

                return r

            r = conjure_star_parameter(conjure_star_sign(s[qi() : star_end]), conjure_name(name))

            j = m.end()

            wi(j)
            wj(j)

            return r

        return tokenize_parameter_operator__X__right_parenthesis(m)


    @share
    def tokenize_parameter_colon_newline():
        assert qd() is 0
        assert qk() is none
        assert qn() is none

        s = qs()

        m = parameter_colon_newline_match(s, qj())

        if m is none:
            #my_line(portray_string(s[qj() : ]))
            raise_unknown_line()

        return evoke_colon__line_marker(m.end('colon'))


    def tokenize_nested__X__equal_sign__blankline():
        r = conjure_equal_sign(s[qi() : ])

        PYTHON__skip_tokenize_prefix()

        return r


    @share
    def tokenize_parameter_operator():
        assert qd() is 1
        assert qk() is none
        assert qn() is none

        s = qs()

        m = parameter_operator_match(s, qj())

        if m is none:
            raise_unknown_line()

        equal_sign__end = m.end('equal_sign')

        if equal_sign__end is not -1:
            if m.start('comment_newline') is not -1:
                return tokenize_nested__X__equal_sign__blankline()

            j = m.end()

            r = conjure_equal_sign(s[qi() : j])

            wi(j)
            wj(j)

            return r

        comma_end = m.end('comma')

        if comma_end is not -1:
            comma_RP_end = m.end('comma_RP')

            if comma_RP_end is not -1:
                if m.end('newline') is not -1:
                    raise_unknown_line()

                d = qd()

                if d is 0:
                    raise_unknown_line()

                r = evoke_comma__right_parenthesis(comma_end, comma_RP_end)

                wd(d - 1)
                wi(comma_RP_end)
                wj(m.end())

                return r


            if m.end('comment_newline') is not -1:
                r = conjure_CRYSTAL_comma__ends_in_newline(s[qi() :])

                PYTHON__skip_tokenize_prefix()

                return r

            j = m.end()

            r = conjure_CRYSTAL_comma(s[qi() : j])

            wi(j)
            wj(j)

            return r

        return tokenize_parameter_operator__X__right_parenthesis(m)
