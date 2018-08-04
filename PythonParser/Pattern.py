#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Pattern')
def module():
    require_module('PythonParser.Path')
    require_module('Restructure.Build')
    require_module('Restructure.CreateMatch')
    require_module('Restructure.Name')


    from Restructure import create_match_code, ANY_OF, BACKSLASH, DOT, EMPTY, END_OF_PATTERN, EXACT
    from Restructure import G, LINEFEED, MATCH, NAME, NAMED_GROUP, NOT_ANY_OF, NOT_FOLLOWED_BY
    from Restructure import ONE_OR_MORE, OPTIONAL, PRINTABLE, PRINTABLE_MINUS, Q, ZERO_OR_MORE


    FULL_MATCH = MATCH
    P          = OPTIONAL


    @share
    def create_PYTHON_parser_match():
        alphanumeric_or_underscore = NAME('alphanumeric_or_underscore', ANY_OF('0-9', 'A-Z', '_', 'a-z'))
        letter_or_underscore       = NAME('letter_or_underscore',       ANY_OF('A-Z', '_', 'a-z'))
        ow                         = NAME('ow',                         ZERO_OR_MORE(' '))
        w                          = NAME('w',                          ONE_OR_MORE(' '))

        #
        #   Simple patterns
        #
        assign_operator     = NAME('assign_operator',     '=')
        colon               = NAME('colon',               ':')
        comma               = NAME('comma',               ',')
        comment_newline     = NAME('comment_newline',     P('#' + ZERO_OR_MORE(DOT)) + LINEFEED + END_OF_PATTERN)
        compare_equal       = NAME('compare_equal',       '==')
        dot                 = NAME('dot',                 '.')
        equal_sign          = NAME('equal_sign',          '=')
        greater_than_sign   = NAME('greater_than_sign',   '>')
        keyword_as          = NAME('as',                  'as')
        keyword_else        = NAME('else',                'else')
        keyword_except      = NAME('except',              'except')
        keyword_finally     = NAME('finally',             'finally')
        keyword_for         = NAME('for',                 'for')
        keyword_if          = NAME('if',                  'if')
        keyword_import      = NAME('import',              'import')
        keyword_in          = NAME('in',                  'in')
        keyword_is          = NAME('is',                  'is')
        keyword_not         = NAME('not',                 'not')
        keyword_or          = NAME('or',                  'or')
        keyword_print       = NAME('print',               'print')
        keyword_try         = NAME('try',                 'try')
        left_brace          = NAME('left_brace',          '{')                                #   }
        left_parenthesis    = NAME('left_parenthesis',    '(')                                #   )
        left_square_bracket = NAME('left_square_bracket', '[')                                #   ]
        less_than_sign      = NAME('less_than_sign',      '<')
        logical_and_sign    = NAME('logical_and_sign',    '&')
        logical_or_sign     = NAME('logical_or_sign',     '|')
        minus_sign          = NAME('minus_sign',          '-')
        not_equal           = NAME('not_equal',           '!=')
        percent_sign        = NAME('percent_sign',        '%')
        plus_sign           = NAME('plus_sign',           '+')
        slash_sign          = NAME('slash_sign',          '/')
        space               = NAME('space',               ' ')
        star_sign           = NAME('star',                '*')
        tilde_sign          = NAME('tilde',               '~')

        name                = NAME('name',   letter_or_underscore + ZERO_OR_MORE(alphanumeric_or_underscore))
        number              = NAME('number', '0' | ANY_OF('1-9') + ZERO_OR_MORE(ANY_OF('0-9')))
        period              = NAME('period', '.')


        next_triple_double_quote = NAME(
                                       'next_triple_double_quote',
                                       (
                                             ZERO_OR_MORE(
                                                   PRINTABLE_MINUS('"', '\\')
                                                 | BACKSLASH + PRINTABLE
                                                 | '"' + P('"') + NOT_FOLLOWED_BY('"')
                                             )
                                           + ('"""' | G('missing_double_quote', LINEFEED + END_OF_PATTERN))
                                       )
                                   )

        next_triple_single_quote = NAME(
                                       'next_single_double_quote',
                                       (
                                             ZERO_OR_MORE(
                                                   PRINTABLE_MINUS("'", '\\')
                                                 | BACKSLASH + PRINTABLE
                                                 | "'" + P("'") + NOT_FOLLOWED_BY("'")
                                             )
                                           + ("'''" | G('missing_single_quote', LINEFEED + END_OF_PATTERN))
                                       )
                                   )

        double_quote = NAME(
                           'double_quote',
                           (
                                  '"'
                                + (
                                      (
                                            '"'
                                          + (
                                                  '"' + next_triple_double_quote
                                                | NOT_FOLLOWED_BY('"')
                                            )
                                      )
                                      | ONE_OR_MORE(PRINTABLE_MINUS('"', '\\') | BACKSLASH + PRINTABLE) + '"'
                                  )
                           ),
                       )

        single_quote = NAME(
                           'single_quote',
                           (
                                  "'"
                                + (
                                      (
                                            "'"
                                          + (
                                                  "'" + next_triple_single_quote
                                                | NOT_FOLLOWED_BY("'")
                                            )
                                      )
                                      | ONE_OR_MORE(PRINTABLE_MINUS("'", '\\') | BACKSLASH + PRINTABLE) + "'"
                                  )
                           ),
                       )


        #   [(
        right_brace             = NAME('right_brace',             '}')
        right_parenthesis       = NAME('right_parenthesis',       ')')
        right_square_bracket    = NAME('right_square_bracket',    ']')

        #
        #   More complicated patterns
        #
        keyword_in__ow  = NAME('keyword_in__ow',  keyword_in  + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore)))
        keyword_is__ow  = NAME('keyword_is__ow',  keyword_is  + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore)))
        keyword_not__ow = NAME('keyword_not__ow', keyword_not + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore)))

        left_brace__ow          = NAME('left_brace__ow',          left_brace + ow)
        left_square_bracket__ow = NAME('left_square_bracket__ow', left_square_bracket + ow)
        left_parenthesis__ow    = NAME('left_parenthesis__ow',    left_parenthesis + ow)
        name1                   = NAME('name1',                   name)
        name2                   = NAME('name2',                   name)
        name3                   = NAME('name3',                   name)
        name4                   = NAME('name4',                   name)
        ow_comma_ow             = NAME('ow_comma_ow',             ow + comma + ow)
        ow_dot_ow               = NAME('ow_dot_ow',               ow + period + ow)
        w_as_w                  = NAME('w_as_w',                  w + keyword_as + w)
        w_import_w              = NAME('w_import_w',              w + keyword_import + w)


        #
        #   Generic
        #
        name_match                     = MATCH('name_match', name)
        name_ow_match                  = MATCH('name_ow_match', G(name) + ow + Q(comment_newline))
        next_crystal_nested_line_match = MATCH('next_crystal_nested_line_match', ow + Q(comment_newline))


        #
        #   Copyright
        #
        FULL_MATCH(
            'copyright_match',
            (
                  EXACT('   Copyright (c)')
                + space + G('year', '2017' + OPTIONAL('-2018'))
                + space + G('author', 'Joy Diamond')
                + '.  All rights reserved.'
            ),
        )


        #
        #   Expressions 1
        #
        MATCH(
            'line_match',
            (
                  G('indented', ow)
                + Q(
                      'something',
                      (
                            #
                            #   Note:
                            #       Both 'keyword' and 'quote' must preceed 'atom', since otherwise they would
                            #       [partially] match 'atom'
                            #
                            G(
                                'keyword',
                                keyword_else | keyword_except | keyword_finally | keyword_try,
                            ) + ow + G(colon) + ow
                          | OPTIONAL('r') + G('quote', double_quote | single_quote) + ow
                          | G('atom', number | '@' | name) + ow
                          | G(
                                'operator',
                                ANY_OF(
                                    right_parenthesis, star_sign, minus_sign, right_square_bracket, right_brace,
                                    tilde_sign,
                                )
                            ) + ow
                          | G(left_parenthesis__ow)    + P(G(right_parenthesis)    + ow)
                          | G(left_square_bracket__ow) + P(G(right_square_bracket) + ow)
                          | G(left_brace__ow)          + P(G(right_brace)          + ow)
                      ),
                  )
                + P(
                        Q('comment', '#' + ZERO_OR_MORE(DOT))
                      + G('newline', LINEFEED + END_OF_PATTERN)
                  )
            ),
        )

        MATCH(
            'PYTHON_atom_match',
            (
                  OPTIONAL('r') + G('quote', double_quote | single_quote) + ow  #   Must preceed 'name'
                | G('atom', number | name) + ow
                | G(
                      'operator',
                      ANY_OF(
                          right_parenthesis, star_sign, minus_sign, colon, right_square_bracket, right_brace,
                          tilde_sign,
                      ),
                  ) + ow
                | G(left_parenthesis__ow)    + P(G(right_parenthesis)    + ow)
                | G(left_square_bracket__ow) + P(G(right_square_bracket) + ow)
                | G(left_brace__ow)          + P(G(right_brace)          + ow)
            ) + Q('newline', comment_newline),
        )

        MATCH(
            #
            #   Same as `PYTHON_atom_match`, but without ')', ']', or '}'.
            #
            #   NOTE:
            #       'name' is also analyzed to see if it a keyword such as 'return'.
            #
            'simple_statement_match',
            (
                  OPTIONAL('r') + G('quote', double_quote | single_quote) + ow  #   Must preceed 'name'
                | G('atom', number | name) + ow
                | G(
                      'operator',
                      ANY_OF(star_sign, minus_sign, tilde_sign)
                  ) + ow
                | G(left_parenthesis__ow)    + P(G(right_parenthesis)    + ow)
                | G(left_square_bracket__ow) + P(G(right_square_bracket) + ow)
                | G(left_brace__ow)          + P(G(right_brace)          + ow)
            ) + Q('newline', comment_newline),
        )

        MATCH(
           'PYTHON_operator_match',
            (
                  G(
                      'operator',
                       (
                             (
                                   ANY_OF(
                                       logical_and_sign, percent_sign, plus_sign, minus_sign, equal_sign,
                                       logical_or_sign,
                                   )
                                 | greater_than_sign + P(greater_than_sign)
                                 | less_than_sign    + P(less_than_sign)
                                 | star_sign         + P(star_sign)
                                 | slash_sign        + P(slash_sign)
                             ) + P(equal_sign)
                           | ANY_OF(right_parenthesis, dot, right_square_bracket, right_brace)
                           | not_equal
                       ),
                  ) + ow
                | G(left_parenthesis__ow) + P(G(right_parenthesis) + ow)
                | G(left_square_bracket__ow) + P(G('tail_index__ow', colon + ow) + P(G(right_square_bracket) + ow))
                | G(comma) + ow + P(G('comma_suffix', right_parenthesis | right_square_bracket) + ow)
                | G(colon) + ow + P(G('head_index', right_square_bracket) + ow)
                | (
                        G(
                            'keyword',
                            (
                                  'a' + (EXACT('nd') | 's')
                                | keyword_else
                                | keyword_for
                                | 'i' + ANY_OF('f', 'n')
                                | keyword_or
                                | keyword_print
                            ),
                        )
                      + (w | NOT_FOLLOWED_BY(alphanumeric_or_underscore))
                  )
                | G(keyword_is__ow)  + Q('is_not', keyword_not__ow)
                | G(keyword_not__ow) + Q('not_in', keyword_in__ow)
            ) + Q(comment_newline),
        )

        MATCH('next_triple_double_quote_line_match', G('quote', next_triple_double_quote) + ow + Q(comment_newline))
        MATCH('next_triple_single_quote_line_match', G('quote', next_triple_single_quote) + ow + Q(comment_newline))


        #
        #   Statements
        #
        MATCH(
            'definition_header_parenthesis_match',
            G(left_parenthesis) + ow + P(G(right_parenthesis) + ow) + Q(comment_newline)
        )

        MATCH(
            'parameter_atom_match',
            (
                  Q(star_sign) + G(name) + ow
                | G(right_parenthesis) + ow
            ) + Q(comment_newline),
        )

        MATCH(
            'parameter_operator_match',
            (
                  G(equal_sign) + ow
                | G(comma) + ow + P(G('comma_RP', right_parenthesis) + ow)
                | G(right_parenthesis) + ow
            ) + Q(comment_newline),
        )

        FULL_MATCH(
            'parameter_colon_newline_match',
            G(colon) + ow + comment_newline,
        )


        MATCH(
            'from_module_match1',
            ow + G('operator', period | keyword_import) + ow,
        )

        MATCH(
            'from_as_match1',
            (
                  ow
                + (
                        G('operator', keyword_as | comma) + ow
                      | comment_newline
                  )
            ),
        )

        MATCH(
            'comma_or_newline_match1',
            (
                  ow
                + (
                        G(comma) + ow
                      | comment_newline
                  )
            ),
        )

        MATCH(
            'import_module_match1',
            (
                  ow
                + (
                        G('operator', period | keyword_as | comma) + ow
                      | comment_newline
                  )
            ),
        )


        #
        #   Create ../Parser-py/PythonParser/Match.py
        #
        create_match_code(
                path_join(source_path, 'Parser/PythonParser/Match.py'),
                '2017-2018',
                'Joy Diamond',
                'PythonParser.Match',
            )
