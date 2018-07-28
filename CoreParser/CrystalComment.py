#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.CrystalComment')
def module():
    require_module('CoreParser.Core')
    require_module('CoreParser.ClassOrder')
    require_module('CoreParser.CrystalIndentation')


    comment_line_cache   = {}
    lookup_comment_line  = comment_line_cache.get
    provide_comment_line = comment_line_cache.setdefault
    store_comment_line   = comment_line_cache.__setitem__


    def dump_token__comment(t, f, newline = true):
        f.partial(t.display_token())

        if newline:
            f.line()
            return false

        return true


    class CommentLine(String):
        __slots__                        = (())
        class_order                      = CLASS_ORDER__COMMENT_LINE__STRING
        ends_in_newline                  = true
        impression                       = empty_indentation
        indentation                      = none
        is_empty_line                    = false
        is_end_of_data                   = false
        is_end_of_data__or__unknown_line = false
        line_marker                      = false
        newlines                         = 1

        
        if capital_global.python_parser:
            is_any_else                      = false
            is_any_except_or_finally         = false
            is_comment_line                  = true
            is_comment__or__empty_line       = true
            is_comment_suite                 = false
            is_else_header_or_fragment       = false
            is_statement                     = false
            is_statement_header              = false


        def __repr__(t):
            return arrange('<CommentLine %s>', portray_string(t))


        def count_newlines(t):
            assert '\n' not in t

            return 1


        def display_token(t):
            if t is empty_comment_line:
                return '<#>'

            return arrange('<# %s>', portray_string(t))


        dump_token = dump_token__comment


        if capital_global.python_parser:
            find_require_module = find_require_module__0
            order            = order__string
            scout_variables  = scout_variables__0
            transform        = transform__remove_comments_0


        def write(t, w):
            w('#' + t + '\n')


    class CommentLine_WithTrailer(ParserToken):
        __slots__ = ((
            'comment',                  #   CommentLine
            'newline',                  #   EmptyLine
        ))


        class_order                      = CLASS_ORDER__COMMENT_LINE
        ends_in_newline                  = true
        impression                       = empty_indentation
        indentation                      = none
        is_empty_line                    = false
        is_end_of_data                   = false
        is_end_of_data__or__unknown_line = false
        newlines                         = 1


        if capital_global.python_parser:
            is_any_else                = false
            is_any_except_or_finally   = false
            is_comment_line            = true
            is_comment__or__empty_line = true
            is_else_header_or_fragment = false
            is_statement               = false
            is_statement_header        = false


        def __init__(t, s, comment, newline):
            t.s       = s
            t.comment = comment
            t.newline = newline


        def __repr__(t):
            return arrange('<CommentLineWithTrailer %s %r>', portray_string(t.comment), t.newline)


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.line_marker is false) and (t.newlines is 1)
            assert ('\n' not in t.comment) and (t.newline.count_newlines() is 1)

            return 1


        def display_token(t):
            return arrange('<# %s %s>', portray_string(t.comment), portray_string(t.newline))


        dump_token = dump_token__comment


        if capital_global.python_parser:
            find_require_module = find_require_module__0
            order               = order__s
            scout_variables     = scout_variables__0
            transform           = transform__remove_comments_0


    class IndentedCommentLine(ParserToken):
        __slots__ = ((
            'impression',               #   Indentation
            'comment',                  #   CommentLine
        ))


        class_order                      = CLASS_ORDER__COMMENT_LINE
        ends_in_newline                  = true
        indentation                      = none
        is_empty_line                    = false
        is_end_of_data                   = false
        is_end_of_data__or__unknown_line = false
        newlines                         = 1


        if capital_global.python_parser:
            is_any_else                = false
            is_any_except_or_finally   = false
            is_comment_line            = true
            is_comment__or__empty_line = true
            is_else_header_or_fragment = false
            is_statement               = false
            is_statement_header        = false


        def __init__(t, s, impression, comment):
            t.s          = s
            t.impression = impression
            t.comment    = comment


        def __repr__(t):
            return arrange('<IndentedCommentLine ++%d %r>', t.impression.total, portray_string(t.comment))


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.line_marker is false) and (t.newlines is 1)
            assert (t.impression.count_newlines() is 0) and ('\n' not in t.comment)

            return 1


        def display_token(t):
            if t.comment is empty_comment_line:
                return arrange('<# ++%d>', t.impression.total)

            return arrange('<# ++%d %s>', t.impression.total, portray_string(t.comment))


        dump_token = dump_token__comment


        if capital_global.python_parser:
            find_require_module = find_require_module__0
            order               = order__s
            scout_variables     = scout_variables__0
            transform           = transform__remove_comments_0


    class IndentedCommentLine_WithTrailer(ParserToken):
        __slots__ = ((
            'impression',               #   Indentation
            'comment',                  #   CommentLine
            'newline',                  #   EmptyLine
        ))


        class_order     = CLASS_ORDER__COMMENT_LINE
        ends_in_newline = true
        indentation     = none
        is_empty_line   = false
        newlines        = 1


        if capital_global.python_parser:
            is_any_else                = false
            is_any_except_or_finally   = false
            is_comment_line            = true
            is_comment__or__empty_line = true
            is_else_header_or_fragment = false
            is_statement               = false
            is_statement_header        = false


        def __init__(t, s, impression, comment, newline):
            t.s          = s
            t.impression = impression
            t.comment    = comment
            t.newline    = newline


        def __repr__(t):
            return arrange('<IndentedCommentLine_WithTrailer ++%d %s %s>',
                           t.impression.total, portray_string(t.comment), portray_string(t.newline))


        def count_newlines(t):
            assert (t.ends_in_newline is true) and (t.line_marker is false) and (t.newlines is 1)
            assert (t.impression.count_newlines() is 0) and ('\n' not in t.comment)
            assert t.newline.count_newlines() is 1

            return 1


        def display_token(t):
            return arrange('<# ++%d %s %s>', t.impression.total, portray_string(t.comment), portray_string(t.newline))


        dump_token = dump_token__comment


        if capital_global.python_parser:
            order           = order__s
            scout_variables = scout_variables__0
            transform       = transform__remove_comments_0


    def conjure_comment_line(comment):
        r = lookup_comment_line(comment)

        if r is not none:
            return r

        r = CommentLine(comment)

        return provide_comment_line(r, r)


    @export
    def conjure_any_comment_line(impression_end, comment_end):
        r = lookup_comment_line(qs())

        if r is not none:
            return r

        s = intern_string(qs())

        comment = conjure_comment_line(s[impression_end + 1 : comment_end])
        newline =                      s[comment_end        :            ]

        if impression_end is 0:
            if newline == '\n':
                return provide_comment_line(s, comment)

            return provide_comment_line(s, CommentLine_WithTrailer(s, comment, conjure_empty_line(newline)))

        impression = conjure_indentation(s[ : impression_end])

        if newline == '\n':
            return provide_comment_line(s, IndentedCommentLine(s, impression, comment))

        return provide_comment_line(
                   s,
                   IndentedCommentLine_WithTrailer(s, impression, comment, conjure_empty_line(newline)),
               )


    empty_comment_line = conjure_comment_line('')


    append_cache('comment-line', comment_line_cache)


    export(
        'empty_comment_line',   empty_comment_line,
    )
