#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.TokenizeAtom')
def module():
    require_module('PythonParser.Match')


    PYTHON__skip_tokenize_prefix = produce__LANGUAGE__skip_tokenize_prefix('python', next_crystal_nested_line_match)


    [
            analyze_PYTHON_comma_operator,
            analyze_PYTHON_keyword_atom,
            analyze_PYTHON_operator,
            analyze_PYTHON_quote,

            analyze_PYTHON_newline_comma_operator,
            analyze_PYTHON_newline_keyword_atom,
            analyze_PYTHON_newline_operator,
            analyze_PYTHON_newline_quote,
    ] = produce_analyze_LANGUAGE_functions(
            'python',
            false,                                                      #   has_open_operator = false
            find_evoke_PYTHON__comma_something,
            find_PYTHON_atom_type,
            lookup_PYTHON_keyword_conjure_function,
            PYTHON__skip_tokenize_prefix,
        )


    #
    #   produce_tokenize_multiline_quote
    #
    def produce_tokenize_multiline_quote(name, next_triple_quote_match, conjure_quote__with_newlines):
        group_name = intern_arrange('missing_%s_quote', name)


        @rename('tokenize_multiline_%s_quote', name)
        def tokenize_multiline_quote(m):
            assert qk() is qn() is 0

            j = qj()

            prefix = (0   if qi() == j else   conjure_whitespace(qs()[qi() : j]))

            many   = [qs()[j : ]]
            append = many.append

            next = next_method(parse_context.iterate_lines)

            while 7 is 7:
                next()

                m = next_triple_quote_match(qs())

                if m is none:
                    raise_unknown_line()

                if m.start(group_name) is not -1:
                    append(qs())
                    continue

                quote_end = m.end('quote')

                append(qs()[ : quote_end])

                r = conjure_quote__with_newlines(''.join(many))

                if m.start('comment_newline') is -1:
                    wi(quote_end)
                    wj(m.end())

                    if prefix is 0:
                        return r

                    return conjure_whitespace_atom(prefix, r)

                if qd() is 0:
                    wn(conjure_line_marker(qs()[quote_end : ]))

                    if prefix is 0:
                        return r

                    return conjure_whitespace_atom(prefix, r)

                suffix = conjure_whitespace__ends_in_newline(qs()[quote_end : ])

                PYTHON__skip_tokenize_prefix()

                if prefix is 0:
                    return conjure_atom_whitespace(r, suffix)

                return conjure_whitespace_atom_whitespace(prefix, r, suffix)


        return tokenize_multiline_quote


    tokenize_multiline_double_quote = produce_tokenize_multiline_quote(
                                          'double',
                                          next_triple_double_quote_line_match,
                                          conjure_triple_double_quote__with_newlines,
                                      )

    tokenize_multiline_single_quote = produce_tokenize_multiline_quote(
                                          'single',
                                          next_triple_single_quote_line_match,
                                          conjure_triple_single_quote__with_newlines,
                                      )


    #
    #   Note:
    #       See note in "CoreParser.TokenizeAtom" on the need to use `==` instead of `is` when comparing `i` & `j`
    #
    #   Note #2:
    #       The previous note also applies to tests like `qi() != j` ... cannot replace this with `qi() is not j`.
    #
    @share
    def analyze_PYTHON_atom(m):
        assert qk() is qn() is 0

        if m.start('newline') is -1:
            atom_s = m.group('atom')

            if atom_s is not none:
                return analyze_PYTHON_keyword_atom(m, atom_s)

            operator_s = m.group('operator')

            if operator_s is not none:
                return analyze_PYTHON_operator(m, operator_s)

            #
            #<similiar-to: 'left_{brace,square_bracket}__end' below>
            #
            #   Differences:
            #       Uses '*parenthesis' instead of '*{brace,square_bracket}'
            #       Uses 'EmptyTuple' instead of 'Empty{Map,List}'
            #
            left_end = m.end('left_parenthesis__ow')

            if left_end is not -1:
                right_end = m.end('right_parenthesis')

                if right_end is not -1:
                    r = evoke_empty_tuple(left_end, right_end)

                    wi(right_end)
                    wj(m.end())

                    return r

                r = conjure_left_parenthesis(qs()[qi() : left_end])

                j = m.end()

                wd(qd() + 1)
                wi(j)
                wj(j)

                return r
            #</similiar-to>

            #
            #<similiar-to: 'left_parenthesis__end' above>
            #
            #   Differences:
            #       Uses '*brace' instead of '*parenthesis'
            #       Uses 'EmptyMap' instead of 'EmptyTuple'
            #
            left_end = m.end('left_brace__ow')

            if left_end is not -1:
                right_end = m.end('right_brace')

                if right_end is not -1:
                    r = evoke_empty_map(left_end, right_end)

                    wi(right_end)
                    wj(m.end())

                    return r

                r = conjure_left_brace(qs()[qi() : left_end])

                j = m.end()

                wd(qd() + 1)
                wi(j)
                wj(j)

                return r
            #</similiar-to>

            #
            #<similiar-to: 'left_parenthesis__end' above>
            #
            #   Differences:
            #       Uses '*square_bracket' instead of '*parenthesis'
            #       Uses 'EmptyMap' instead of 'EmptyTuple'
            #
            left_end = m.end('left_square_bracket__ow')

            if left_end is not -1:
                right_end = m.end('right_square_bracket')

                if right_end is not -1:
                    r = evoke_empty_list(left_end, right_end)

                    wi(right_end)
                    wj(m.end())

                    return r

                r = conjure_left_square_bracket(qs()[qi() : left_end])

                j = m.end()

                wd(qd() + 1)
                wi(j)
                wj(j)

                return r
            #</similiar-to>

            quote_start = m.start('quote')

            if quote_start is not -1:
                if m.start('missing_double_quote') is not -1:
                    return tokenize_multiline_double_quote(m)

                if m.start('missing_single_quote') is not -1:
                    return tokenize_multiline_single_quote(m)

                return analyze_PYTHON_quote(m, quote_start)

            raise_unknown_line()

        #
        #   Newline
        #
        atom_s = m.group('atom')

        if atom_s is not none:
            return analyze_PYTHON_newline_keyword_atom(m, atom_s)

        operator_s = m.group('operator')

        if operator_s is not none:
            return analyze_PYTHON_newline_operator(m, operator_s)

        #
        #<same-as: 'left_{brace,square_bracket}__end' below>
        #
        #   Differences:
        #       Uses '*parenthesis' instead of '*brace'
        #       Uses 'EmptyTuple' instead of 'Empty{Map,List}'
        #
        left_end = m.end('left_parenthesis__ow')

        if left_end is not -1:
            right_end = m.end('right_parenthesis')

            if right_end is not -1:
                if qd() is 0:
                    right_end = m.end('right_parenthesis')

                    r = evoke_empty_tuple(left_end, right_end)

                    wn(conjure_line_marker(qs()[right_end : ]))

                    return r

                r = evoke_empty_tuple(left_end, none)

                PYTHON__skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_parenthesis__ends_in_newline(qs()[qi() : ])

            PYTHON__skip_tokenize_prefix()

            return r
        #</same-as>

        #
        #<same-as: 'left_parenthesis__end' above>
        #
        #   Differences:
        #       Uses '*brace' instead of '*parenthesis'
        #       Uses 'EmptyList' instead of 'EmptyTuple'
        #
        left_end = m.end('left_brace__ow')

        if left_end is not -1:
            right_end = m.end('right_brace')

            if right_end is not -1:
                if qd() is 0:
                    right_end = m.end('right_brace')

                    r = evoke_empty_map(left_end, right_end)

                    wn(conjure_line_marker(qs()[right_end : ]))

                    return r

                r = evoke_empty_map(left_brace, none)

                PYTHON__skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_brace__ends_in_newline(qs()[qi() : ])

            PYTHON__skip_tokenize_prefix()

            return r
        #</same-as>

        #
        #<same-as: 'left_parenthesis__end' above>
        #
        #   Differences:
        #       Uses '*square_bracket' instead of '*parenthesis'
        #       Uses 'EmptyList' instead of 'EmptyTuple'
        #
        left_end = m.end('left_square_bracket__ow')

        if left_end is not -1:
            right_end = m.end('right_square_bracket')

            if right_end is not -1:
                if qd() is 0:
                    right_end = m.end('right_square_bracket')

                    r = evoke_empty_list(left_end, right_end)

                    wn(conjure_line_marker(qs()[right_end : ]))

                    return r

                r = evoke_empty_list(left_end, none)

                PYTHON__skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_square_bracket__ends_in_newline(qs()[qi() : ])

            PYTHON__skip_tokenize_prefix()

            return r
        #</same-as>

        quote_start = m.start('quote')

        if quote_start is not -1:
            assert m.start('missing_double_quote') is m.start('missing_single_quote') is -1

            return analyze_PYTHON_newline_quote(m, quote_start)

        raise_unknown_line()


    share(
        'analyze_PYTHON_comma_operator',            analyze_PYTHON_comma_operator,
        'analyze_PYTHON_newline_comma_operator',    analyze_PYTHON_newline_comma_operator,
        'analyze_PYTHON_newline_operator',          analyze_PYTHON_newline_operator,
        'analyze_PYTHON_operator',                  analyze_PYTHON_operator,
        'PYTHON__skip_tokenize_prefix',             PYTHON__skip_tokenize_prefix,
    )
