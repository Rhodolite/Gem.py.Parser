#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.Tokenize1Atom')
def gem():
    require_gem('Sapphire.Tokenize1Operator')


    conjure_atom_whitespace             = Shared.conjure_atom_whitespace
    conjure_line_marker                 = Shared.conjure_line_marker
    conjure_whitespace_atom_whitespace  = Shared.conjure_whitespace_atom_whitespace
    conjure_whitespace__ends_in_newline = Shared.conjure_whitespace__ends_in_newline
    conjure_whitespace                  = Shared.conjure_whitespace
    parse_context                       = Shared.parse_context
    qd                                  = Shared.qd
    qi                                  = Shared.qi
    qj                                  = Shared.qj
    qs                                  = Shared.qs
    raise_unknown_line                  = Shared.raise_unknown_line
    skip_tokenize_prefix                = Shared.skip_tokenize_prefix
    wi                                  = Shared.wi
    wj                                  = Shared.wj
    wn                                  = Shared.wn

    @privileged
    def produce_tokenize_multiline_quote(name, next_triple_quote_match, conjure_quote__with_newlines):
        group_name = intern_arrange('missing_%s_quote', name)


        def tokenize_multiline_quote(m):
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

                skip_tokenize_prefix()

                if prefix is 0:
                    return conjure_atom_whitespace(r, suffix)

                return conjure_whitespace_atom_whitespace(prefix, r, suffix)


        if __debug__:
            tokenize_multiline_quote.__name__ = intern_arrange('tokenize_multiline_%s_quote', name)

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
    #       Below a few tests of 'i == j' (or the equivalent 'qi() = qj()').
    #
    #       None of these tests can be optimized to 'i is j' since [the original] 'i' & 'j' could have been created
    #       with two different calls, such as:
    #
    #           1.  m.end('atom'); .vs.
    #           2.  m.end()
    #
    #       with 'ow' is empty -- and thus have the same value (but different internal addresses).
    #
    #   Note #2:
    #       The previous note also applies to tests like 'qi() != j', cannot replace this with 'qi() is not j'
    #
    @share
    def analyze_atom(m):
        if m.start('newline') is -1:
            atom_s = m.group('atom')

            if atom_s is not none:
                conjure = lookup_keyword_conjure_function(atom_s)

                if conjure is not none:
                    j = m.end()

                    r = conjure(qs()[qi() : j])

                    wi(j)
                    wj(j)

                    return r

                atom_end = m.end('atom')

                if qi() != qj():
                    r = find_evoke_whitespace_atom(atom_s[0])(qj(), atom_end)
                else:
                    r = find_atom_type(atom_s[0])(atom_s)

                wi(atom_end)
                wj(m.end())

                return r

            operator_s = m.group('operator')

            if operator_s is not none:
                s = qs()

                if is_close_operator(operator_s) is 7:
                    d            = qd()
                    operator_end = m.end('operator')

                    r = conjure_action_word(operator_s, s[qi() : operator_end])

                    if d is 0:
                        raise_unknown_line()

                    assert d > 0

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
                j         = qj()
                quote_end = m.end('quote')

                if m.start('missing_double_quote') is not -1:
                    return tokenize_multiline_double_quote(m)

                if m.start('missing_single_quote') is not -1:
                    return tokenize_multiline_single_quote(m)

                if qi() != j:
                    r = find_evoke_whitespace_atom(qs()[quote_start])(j, quote_end)
                else:
                    s = qs()

                    r = find_atom_type(s[quote_start])(s[j : quote_end])

                wi(quote_end)
                wj(m.end())

                return r

            raise_unknown_line()

        #
        #   Newline
        #
        atom_s = m.group('atom')

        if atom_s is not none:
            conjure = lookup_keyword_conjure_function(atom_s)

            if conjure is not none:
                if qd() is 0:
                    atom_end = m.end('atom')

                    r = conjure(atom_s)(qs()[qi() : atom_end])

                    wn(conjure_line_marker(s[atom_end : ]))

                    return r

                r = conjure(atom_s)(qs()[qi() : ])

                skip_tokenize_prefix()

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
                    r = find_evoke_atom_whitespace(atom_s[0])(m.end('atom'), none)
                else:
                    r = find_evoke_whitespace_atom_whitespace(atom_s[0])(qj(), m.end('atom'), none)

                skip_tokenize_prefix()

                return r

            atom_end = m.end('atom')

            if qi() == qj():
                r = find_atom_type(atom_s[0])(atom_s)
            else:
                r = find_evoke_whitespace_atom(atom_s[0])(qj(), m.end('atom'))

            wn(conjure_line_marker(qs()[atom_end : ]))

            return r
            #</similiar-to>

        operator_s = m.group('operator')

        if operator_s is not none:
            if is_close_operator(operator_s) is 7:
                d = qd()

                if d is 1:
                    operator_end = m.end('operator')
                    s            = qs()

                    r = conjure_action_word(operator_s, s[qi() : operator_end])

                    wd0()
                    wn(conjure_line_marker(s[operator_end : ]))

                    return r

                wd(d - 1)

                r = conjure_action_word__ends_in_newline(operator_s, qs()[qi() : ])

                skip_tokenize_prefix()

                return r

            if qd() is 0:
                operator_end = m.end('operator')

                s = qs()

                r = conjure_action_word(operator_s, s[qi() : operator_end])

                wn(conjure_line_marker(s[operator_end : ]))

                return r

            r = conjure_action_word__ends_in_newline(operator_s, qs()[qi() : ])

            skip_tokenize_prefix()

            return r

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

                skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_parenthesis__ends_in_newline(qs()[qi() : ])

            skip_tokenize_prefix()

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

                skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_brace__ends_in_newline(qs()[qi() : ])

            skip_tokenize_prefix()

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

                skip_tokenize_prefix()

                return r

            wd(qd() + 1)

            r = conjure_left_square_bracket__ends_in_newline(qs()[qi() : ])

            skip_tokenize_prefix()

            return r
        #</same-as>

        quote_start = m.start('quote')

        if quote_start is not -1:
            assert m.start('missing_double_quote') is m.start('missing_single_quote') is -1

            #
            #   NOTE:
            #
            #       In the code below: Use 'qj()' instead of "m.start('quote')" to be sure to pick up any letters
            #       prefixing the quote, such as r'prefixed'
            #

            #
            #<similiar-to: {atom_s} above>
            #
            #   Differences:
            #
            #       Uses "quote_end" instead of "m.end('atom')"
            #       Uses "s" intead of "qs()"
            #
            if qd() is not 0:
                if qi() == qj():
                    r = find_evoke_atom_whitespace(qs()[quote_start])(m.end('quote'), none)
                else:
                    r = find_evoke_whitespace_atom_whitespace(qs()[quote_start])(qj(), m.end('quote'), none)

                skip_tokenize_prefix()

                return r

            j         = qj()
            quote_end = m.end('quote')
            s         = qs()

            if qi() == qj():
                r = find_atom_type(s[quote_start])(s[j : quote_end])
            else:
                r = find_evoke_whitespace_atom(s[quote_start])(j, quote_end)

            wn(conjure_line_marker(s[m.end('quote') : ]))

            return r
            #</similiar-to>

        raise_unknown_line()
