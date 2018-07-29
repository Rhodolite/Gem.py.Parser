#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('SqlParser.Comment')
def module():
    class CommentOperator(ParserToken):
        __slots__           = (())
        display_name        = 'comment-operator'
        is_comment_operator = true


    class TokenComment(ParserToken):
        __slots__        = (())
        display_name     = 'comment'
        is_token_comment = true


    class TokenCommentNewline(ParserToken):
        __slots__        = (())
        display_name     = 'comment-newline'
        is_token_comment = true
        is_token_newline = true


        def display_token(t):
            return portray_raw_string(t.s)


    class TokenNewline(ParserToken):
        __slots__       = (())
        display_name     = 'newline'
        is_token_newline = true


        def __init__(t, s):
            assert (s.count('\n') == 1) and (s[-1] == '\n')

            t.s = s


        def count_newlines(t):
            assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
            assert (t.s.count('\n') is 1) and (t.s[-1] == '\n')

            return 1


        def display_token(t):
            return portray_raw_string(t.s)


    @share
    class TreeComment(Object):
        __slots__ = ((
            'comment_operator',             #   TokenComment
            'comment',                      #   String+
            'newline',                      #   TokenNewline
        ))


        def __init__(t, comment_operator, comment, newline):
            assert (comment_operator.is_comment_operator) and (comment.is_token_comment) and (newline.is_token_newline)

            t.comment_operator = comment_operator
            t.comment          = comment
            t.newline          = newline


        def __repr__(t):
            return arrange('<comment %r %r %r>', t.comment_operator.s, t.comment.s, t.newline.s)


        def write(t, w):
            w(t.comment_operator.s + t.comment.s + t.newline.s)


    conjure_comment_operator = produce_conjure_by_name('comment_operator',         CommentOperator)
    conjure_comment_newline  = produce_conjure_by_name('comment_operator_newline', TokenCommentNewline)
    conjure_token_comment    = produce_conjure_by_name('token_comment',            TokenComment)
    conjure_token_newline    = produce_conjure_by_name('token_newline',            TokenNewline)


    share(
        'conjure_comment_operator',     conjure_comment_operator,
        'conjure_token_comment',        conjure_token_comment,
    )


    share(
        'conjure_comment_newline',     conjure_comment_newline,
        'conjure_token_newline',       conjure_token_newline,
    )
