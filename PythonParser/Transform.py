#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.Transform')
def gem():
    class PythonParserTransform(Object):
        __slots__ = ((
            'remove_comments',          #   Boolean
            'remove_indentation',       #   Boolean
            'indentation',              #   Vacant | Indentation
        ))


        def __init__(t, remove_comments, remove_indentation):
            t.remove_comments    = remove_comments
            t.remove_indentation = remove_indentation
            t.indentation        = empty_indentation


        def pop_indentation(t, previous):
            t.indentation = previous


        def push_indentation(t):
            indentation = t.indentation

            if t.remove_indentation:
                t.indentation = next_indentation(indentation)

            return indentation


    @share
    def create_python_parser_transform(
            remove_comments    = false,
            remove_indentation = false,
    ):
        total = remove_comments + remove_indentation

        #if total is 0:
        #    return 0

        return PythonParserTransform(remove_comments, remove_indentation)
