#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('SqlParser.Statement')
def gem():
    require_gem('SqlParser.Core')


    @share
    class PoundSignComment(Object):
        __slots__ = ((
            'comment',                  #   Comment
            'newline',                  #   String
        ))


        def __init__(t, comment, newline):
            t.comment = comment
            t.newline = newline


        def __repr__(t):
            if t.comment is '':
                return arrange('<# %r>', t.newline)

            return arrange('<# %r %r>', t.comment, t.newline)


        def write(t, w):
            w('#' + t.comment + t.newline)
