#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('SqlParser.Pattern')
def module():
    require_module('Restructure.Build')
    require_module('Restructure.CreateMatch')
    require_module('Restructure.Name')


    from Restructure import create_match_code, ANY_OF, BACKSLASH, DOT, EMPTY, END_OF_PATTERN, EXACT
    from Restructure import G, LINEFEED, MATCH, NAME, NAMED_GROUP, NOT_FOLLOWED_BY
    from Restructure import ONE_OR_MORE, OPTIONAL, PRINTABLE, PRINTABLE_MINUS, Q, ZERO_OR_MORE


    FULL_MATCH = MATCH
    P          = OPTIONAL


    @share
    def create_sql_parser_match():
        ow         = NAME('ow',         ZERO_OR_MORE(' '))
        w          = NAME('w',          ONE_OR_MORE(' '))
        identifier = NAME('identifier', ONE_OR_MORE(ANY_OF('$', '0-9', 'A-Z', '_', 'a-z')))


        #
        #   Generic
        #
        trailing_newline = NAME(
            'trailing_newline',
            (
                  ow
                + P(
                        G('newline_pound_sign', '#') +  ow + Q('newline_pound_sign_comment', ONE_OR_MORE(DOT))
                      | G('newline_dash_dash', '--') + P(w + Q('newline_dash_dash_comment',  ONE_OR_MORE(DOT)))
                  )
                + G('newline', LINEFEED)
            )
        )


        #
        #   MySQL 5.6
        #
        FULL_MATCH(
            'mysql_line_match',
            (
                  ow
                + (
                        G(identifier)
                      | (
                              P(
                                      G('pound_sign', '#') +  ow + Q('pound_sign_comment', ONE_OR_MORE(DOT))
                                    | G('dash_dash', '--') + P(w + Q('dash_dash_comment',  ONE_OR_MORE(DOT)))
                              )
                            + LINEFEED
                        )
                  )
            ),
        )


        #
        #   Create ../SqlParser/Match.py
        #
        create_match_code(
                path_join(module_path[0], 'SqlParser/Match.py'),
                '2017-2018',
                'Joy Diamond',
                'SqlParser.Match',
            )
