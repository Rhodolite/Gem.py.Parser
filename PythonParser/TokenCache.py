#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.TokenCache')
def gem():
    require_gem('PythonParser.Cache')


    #
    #   Different token caches are needed to distinguish identical characters that appear in different contexts:
    #
    #       arguments_0_token_cache     - '()' that is used as function arguments.
    #
    #       comment_line_cache          - COmment lines (See PythonParser/Whitespace.py)
    #
    #       empty_line_cache            - Empty lines (See PythonParser/Whitespace.py)
    #
    #       indentation_cache           - White space at beginning of a line that is considered indentation.
    #                                     (Also used for dual token Indentation_Token)
    #
    #       join_token_cache            - Whitespace that is used to concatanate strings; Example:
    #
    #                                           "hi"  'there'
    #
    #                                     The two spaces between the two strings are considered an "invisible" join
    #                                     token & are stored in join_token_cache (or 'will be stored', when this
    #                                     feature is implemented)
    #
    #       line_marker_token_cache     - Line markers.  The last '\n is a significant line-maker.
    #
    #                                     Any other '\n' in the strings here is considered whitespace.
    #
    #       parameters_0_token_cache     - '()' that is used as function parameters.
    #
    #   NOTE:
    #       See more of this comment in ../CoreParser/TokenCache.py
    #
    arguments_0_token_cache  = create_cache('arguments_0_token')
    indentation_cache        = create_cache('indentation')
    join_token_cache         = create_cache('join_token')
    line_marker_token_cache  = create_cache('line_marker_token')
    parameters_0_token_cache = create_cache('parameters_0_token')

    lookup_arguments_0_token  = arguments_0_token_cache .lookup
    lookup_indentation        = indentation_cache       .lookup
    lookup_join_token         = join_token_cache        .lookup
    lookup_line_marker        = line_marker_token_cache .lookup
    lookup_parameters_0_token = parameters_0_token_cache.lookup

    provide_arguments_0_token  = arguments_0_token_cache .provide
    provide_indentation        = indentation_cache       .provide
    provide_join_token         = join_token_cache        .provide
    provide_line_marker        = line_marker_token_cache .provide
    provide_parameters_0_token = parameters_0_token_cache.provide


    share(
        'lookup_arguments_0_token',     lookup_arguments_0_token,
        'lookup_join_token',            lookup_join_token,
        'lookup_line_marker',           lookup_line_marker,
        'lookup_parameters_0_token',    lookup_parameters_0_token,
        'lookup_indentation',           lookup_indentation,

        'provide_arguments_0_token',    provide_arguments_0_token,
        'provide_join_token',           provide_join_token,
        'provide_line_marker',          provide_line_marker,
        'provide_parameters_0_token',   provide_parameters_0_token,
        'provide_indentation',          provide_indentation,
    )
