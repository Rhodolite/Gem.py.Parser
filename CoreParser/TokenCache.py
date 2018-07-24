#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CoreParser.TokenCache')
def gem():
    require_gem('CoreParser.Cache')
    require_gem('CoreParser.Core')


    #
    #   Different token caches are needed to distinguish identical characters that appear in different contexts:
    #
    #       normal_token_cache          - Normal tokens.  Any '\n' in the strinss here is considered whitespace.
    #
    #                                     This includes '()' when used as a tuple {where as '()' when used as
    #                                     function arguments or function parameters appears in different caches}.
    #
    #                                     Normal whitespace also appears in this cache (for example whitespace
    #                                     before an atom on a continuation line).
    #   NOTE:
    #       See more of this comment in ../PythonParser/TokenCache.py
    #
    normal_token_cache   = create_cache('normal_token')

    lookup_normal_token  = normal_token_cache.lookup
    provide_normal_token = normal_token_cache.provide


    export(
        'lookup_normal_token',      lookup_normal_token,
        'provide_normal_token',     provide_normal_token,
    )
