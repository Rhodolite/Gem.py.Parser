#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.TokenCache')
def module():
    require_module('PythonParser.Cache')


    #
    #   Different token caches are needed to distinguish identical characters that appear in different contexts:
    #
    #       arguments_0_token_cache     - '()' that is used as function arguments.
    #
    #       comment_line_cache          - Comment lines (See CoreParser/CrystalComment.py)
    #
    #       empty_line_cache            - Empty lines (See CoreParser/EmptyLine.py)
    #
    #       join_token_cache            - Whitespace that is used to concatanate strings; Example:
    #
    #                                           "hi"  'there'
    #
    #                                     The two spaces between the two strings are considered an "invisible" join
    #                                     token & are stored in join_token_cache (or 'will be stored', when this
    #                                     feature is implemented)
    #
    #       parameters_0_token_cache     - '()' that is used as function parameters.
    #
    #   NOTE:
    #       See more of this comment in ../CoreParser/TokenCache.py
    #
    arguments_0_token_cache  = create_cache('arguments_0_token')
    join_token_cache         = create_cache('join_token')
    parameters_0_token_cache = create_cache('parameters_0_token')

    lookup_arguments_0_token  = arguments_0_token_cache .lookup
    lookup_join_token         = join_token_cache        .lookup
    lookup_parameters_0_token = parameters_0_token_cache.lookup

    provide_arguments_0_token  = arguments_0_token_cache .provide
    provide_join_token         = join_token_cache        .provide
    provide_parameters_0_token = parameters_0_token_cache.provide


    share(
        'lookup_arguments_0_token',     lookup_arguments_0_token,
        'lookup_join_token',            lookup_join_token,
        'lookup_parameters_0_token',    lookup_parameters_0_token,

        'provide_arguments_0_token',    provide_arguments_0_token,
        'provide_join_token',           provide_join_token,
        'provide_parameters_0_token',   provide_parameters_0_token,
    )
