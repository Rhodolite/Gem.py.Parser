#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CoreParser.Line')
def gem():
    require_gem('CoreParser.Core')
    require_gem('CoreParser.Token')


    @export
    class EmptyLine(Token):
        __slots__    = (())
        display_name = 'empty-line'
        indentation  = none
