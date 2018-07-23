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
    #
    #       indentation_cache           - White space at beginning of a line that is considered indentation.
    #                                     (Also used for dual token Indentation_Token)
    #
    #       line_marker_token_cache     - Line markers.  The last '\n is a significant line-maker.
    #
    #                                     Any other '\n' in the strings here is considered whitespace.
    #
    #   NOTE:
    #       See more of this comment in ../PythonParser/TokenCache.py
    #
    indentation_cache       = create_cache('indentation')
    line_marker_token_cache = create_cache('line_marker_token')
    lookup_line_marker      = line_marker_token_cache .lookup
    normal_token_cache      = create_cache('normal_token')

    lookup_indentation  = indentation_cache .lookup
    lookup_normal_token = normal_token_cache.lookup

    provide_indentation  = indentation_cache .provide
    provide_line_marker  = line_marker_token_cache .provide
    provide_normal_token = normal_token_cache.provide


    export(
        'lookup_indentation',       lookup_indentation,
        'lookup_line_marker',       lookup_line_marker,
        'lookup_normal_token',      lookup_normal_token,

        'provide_indentation',      provide_indentation,
        'provide_line_marker',      provide_line_marker,
        'provide_normal_token',     provide_normal_token,
    )
