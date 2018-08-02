#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Tokenize1Operator')
def module():
    python__skip_tokenize_prefix = produce__LANGUAGE__skip_tokenize_prefix('python', next_crystal_nested_line_match)


    @share
    def tokenize_python_operator():
        assert qk() is none
        assert qn() is none

        s = qs()

        #my_line('d: %d; full: %r; s: %r', qd(), s, portray_string(s[qj() : ]))

        m = operator_match(s, qj())

        if m is none:
            #my_line(portray_string(s[qj() : ]))
            raise_unknown_line()

        if m.end('comment_newline') is -1:
            operator_s = m.group('operator')

            if operator_s is not none:
                if is_close_operator(operator_s) is 7:
                    d = qd()

                    if d is 0:
                        #my_line('d: %d; operator_s: %r; s: %s', d, operator_s, portray_string(s[qj() : ]))
                        raise_unknown_line()

                    operator_end = m.end('operator')

                    r = conjure_action_word(operator_s, s[qi() : operator_end])

                    wd(d - 1)
                    wi(operator_end)
                    wj(m.end())

                    return r

                j = m.end()

                r = conjure_action_word(operator_s, s[qi() : j])

                wi(j)
                wj(j)

                return r

            #
            #<similiar-to: 'keyword_is__ow' below>
            #
            #   Differences:
            #
            #       See each of them for documented differences
            #
            #   NOTE:
            #       As this is an 'operator' the meaning of '()' must be 'Arguments_0' instead of 'Tuple_0'
            #       (Tuple_0 is an atom)
            #
            left_end = m.end('left_parenthesis__ow')

            if left_end is not -1:
                right_end = m.end('right_parenthesis')

                if right_end is not -1:
                    r = evoke_arguments_0(left_end, right_end)

                    wi(m.end('right_parenthesis'))
                    wj(m.end())

                    return r

                left = conjure_left_parenthesis(s[qi() : left_end])

                wd(qd() + 1)
                wi(left_end)
                wj(left_end)

                return left
            #</similiar-to>

            left_end = m.end('left_square_bracket__ow')

            if left_end is not -1:
                tail_index__end = m.end('tail_index__ow')

                if tail_index__end is not -1:
                    RSB_end = m.end('right_square_bracket')

                    if RSB_end is not -1:
                        r = evoke_all_index(left_end, tail_index__end, RSB_end)

                        j = m.end()

                        wi(RSB_end)
                        wj(j)

                        return r

                    r = evoke__left_square_bracket__colon(left_end, tail_index__end)

                    wd(qd() + 1)
                    wi(tail_index__end)
                    wj(m.end())

                    return r

                r = conjure_left_square_bracket(s[qi() : left_end])

                wd(qd() + 1)
                wi(left_end)
                wj(left_end)

                return r

            if m.start('comma') is not -1:
                suffix_start = m.start('comma_suffix')

                if suffix_start is not -1:
                    d = qd()

                    if d is 0:
                        raise_unknown_line()

                    suffix_end = m.end('comma_suffix')

                    r = find_evoke_comma_something(s[suffix_start])(suffix_start, suffix_end)

                    wd(d - 1)
                    wi(suffix_end)
                    wj(m.end())

                    return r

                j = m.end()

                r = conjure_comma(s[qi() : j])

                wi(j)
                wj(j)

                return r

            if m.start('colon') is not -1:
                suffix_start = m.start('head_index')

                if suffix_start is not -1:
                    d = qd()

                    if d is 0:
                        raise_unknown_line()

                    suffix_end = m.end('head_index')

                    r = evoke__colon__right_square_bracket(suffix_start, suffix_end)

                    wd(d - 1)
                    wi(suffix_end)
                    wj(m.end())

                    return r

                j = m.end()

                r = conjure_colon(s[qi() : j])

                wi(j)
                wj(j)

                return r

            keyword_s = m.group('keyword')

            if keyword_s is not none:
                j = m.end()

                r = conjure_action_word(keyword_s, s[qi() : j])

                wi(j)
                wj(j)

                return r

            #
            #<similiar-to: {left_parenthesis__ow} above>
            #
            #   Differences:
            #       Uses keyword_is*  instead of left_parenthesis*
            #       Uses keyword_not* instead of right_parenthesis*
            #       Uses Is_Not       instead of Arguments_0
            #
            #       Does not increment depth when parsing the 'is' keyword.
            #
            #   NOTE:
            #       When parsing 'is not' the whitespace after 'not' is treated as part of the 'not' keyword
            #
            #       This is different than ')', ']' & '}', none of which treat the whitespace as part of
            #       of the closing operator.
            #
            #       This subtle difference is implemented in three ways:
            #
            #           1.  By the regular pattern, which includes the whitespace as part of the 'not' keyword
            #               (but not included as part of ')', ']', and '}')
            #
            #           2.  The code below on setting 'wi' is different than the code above.
            #
            #           3.  The 'return Is_Not()' statement is also optimized since it is able to use 'right_s'
            #               to construct the 'not' keyword.
            #
            left_end = m.end('keyword_is__ow')

            if left_end is not -1:
                right_end = m.end('is_not')

                if right_end is not -1:
                    r = evoke_is_not(left_end, right_end)

                    j = m.end()

                    wi(j)
                    wj(j)

                    return r

                r = conjure_keyword_is(s[qi() : left_end])

                j = m.end()

                wi(j)
                wj(j)

                return r
            #</similiar-to>


            #
            #<similiar-to: {keyword_is__ow} above>
            #
            #   Differences:
            #       Uses keyword_not* instead of keyword_is
            #       Uses keyword_in*  instead of keyword_in
            #       Uses Not_In       instead of Is_Not
            #
            left_end = m.end('keyword_not__ow')

            if left_end is not -1:
                right_end = m.end('not_in')

                if right_end is not -1:
                    r = evoke_not_in(left_end, right_end)

                    j = m.end()

                    wi(j)
                    wj(j)

                    return r

                r = conjure_keyword_not(s[qi() : left_end])

                j = m.end()

                wi(j)
                wj(j)

                return r
            #</similiar-to>

            raise_unknown_line()


        #
        #   Newline version
        #
        operator_s = m.group('operator')

        if operator_s is not none:
            if is_close_operator(operator_s) is 7:
                d = qd()

                if d is 1:
                    i = m.end('operator')

                    r = conjure_action_word(operator_s, s[qi() : i])

                    wd0()
                    wn(conjure_line_marker(s[i : ]))

                    return r

                if d is 0:
                    raise_unknown_line()

                wd(d - 1)
            elif qd() is 0:
                operator_end = m.end('operator')

                r = conjure_action_word(operator_s, s[qi() : operator_end])

                wn(conjure_line_marker(s[operator_end : ]))

                return r

            r = conjure_action_word__ends_in_newline(operator_s, s[qi() : ])

            python__skip_tokenize_prefix()

            return r

        left_end = m.end('left_parenthesis__ow')

        if left_end is not -1:
            right_end = m.end('right_parenthesis')

            if right_end is not -1:
                d = qd()

                r = evoke_arguments_0(left_end, (right_end   if d is 0 else   none))

                if qd() is 0:
                    wn(conjure_line_marker(s[right_end : ]))
                else:
                    python__skip_tokenize_prefix()

                return r

            left = conjure_left_parenthesis__ends_in_newline(s[qi() : ])

            python__skip_tokenize_prefix()

            wd(qd() + 1)

            return left

        left_end = m.end('left_square_bracket__ow')

        if left_end is not -1:
            tail_index__end = m.end('tail_index__ow')

            if tail_index__end is not -1:
                right_end = m.end('right_square_bracket')

                if right_end is not -1:
                    if qd() is 0:
                        r = evoke_all_index(left_end, tail_index__end, right_end)

                        wn(conjure_line_marker(s[right_end : ]))

                        return r
                    else:
                        r = evoke_all_index(left_end, tail_index__end, none)

                        python__skip_tokenize_prefix()

                        return r

                left = evoke__left_square_bracket__colon(left_end, none)
            else:
                left = conjure_left_square_bracket__ends_in_newline(s[qi() : ])

            python__skip_tokenize_prefix()

            wd(qd() + 1)

            return left

        if m.start('comma') is not -1:
            suffix_start = m.start('comma_suffix')

            if suffix_start is not -1:
                d = qd()

                if d is 1:
                    suffix_end = m.end('comma_suffix')

                    r = find_evoke_comma_something(s[suffix_start])(suffix_start, suffix_end)

                    wd0()

                    wn(conjure_line_marker(s[suffix_end : ]))

                    return r

                r = find_evoke_comma_something(s[suffix_start])(suffix_start, none)

                assert d > 1

                wd(d - 1)

                python__skip_tokenize_prefix()

                return r

            if qd() is 0:
                raise_unknown_line()

            r = conjure_comma__ends_in_newline(s[qi() : ])

            python__skip_tokenize_prefix()

            return r

        if m.start('colon') is not -1:
            suffix_start = m.start('head_index')

            if suffix_start is not -1:
                d = qd()

                if d is 1:
                    suffix_end = m.end('head_index')

                    r = evoke__colon__right_square_bracket(suffix_start, suffix_end)

                    wd0()

                    wn(conjure_line_marker(s[suffix_end : ]))

                    return r

                r = evoke__colon__right_square_bracket(suffix_start, none)

                assert d > 1

                wd(d - 1)

                python__skip_tokenize_prefix()

                return r

            if qd() is 0:
                return evoke_colon__line_marker(m.end('colon'))

            r = conjure_colon__ends_in_newline(s[qi() : ])

            python__skip_tokenize_prefix()

            return r

        keyword_s = m.group('keyword')

        if keyword_s is not none:
            if qd() is 0:
                keyword_end = m.end('keyword')

                r = conjure_action_word(keyword_s, s[qi() : keyword_end])

                wn(conjure_line_marker(s[keyword_end : ]))

                return r

            r = conjure_action_word__ends_in_newline(keyword_s, s[qi() : ])

            python__skip_tokenize_prefix()

            return r

        raise_unknown_line()


    share(
        'python__skip_tokenize_prefix',     python__skip_tokenize_prefix,
    )
