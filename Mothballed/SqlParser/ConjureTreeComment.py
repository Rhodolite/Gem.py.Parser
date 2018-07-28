#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('SqlParser.ConjureTreeComment')
def module():
    require_module('SqlParser.Core')
    require_module('SqlParser.Comment')


    tree_comment_cache   = {}
    provide_tree_comment = tree_comment_cache.setdefault
    lookup_tree_comment  = tree_comment_cache.get
    store_tree_comment   = tree_comment_cache.__setitem__


    @export
    def conjure_tree_comment(comment_operator_s, comment_s, newline_s):
        first = lookup_tree_comment(comment_s)

        if first is none:
            comment = conjure_token_comment(comment_s)

            return provide_tree_comment(
                       comment.s,
                       TreeComment(
                           conjure_comment_operator(comment_operator_s),
                           comment,
                           conjure_token_newline(newline_s),
                       ),
                   )

        if first.__class__ is TreeComment:
            if first.comment_operator.s == comment_operator_s:
                if first.newline.s == newline_s:
                    return first

                r = TreeComment(
                        first.comment_operator,
                        first.comment,
                        conjure_token_newline(newline_s),
                    )

                store_tree_comment(
                    first.comment.s,
                    {
                        first.comment_operator.s : {
                            first.newline.s : first,
                            r.newline.s     : r,
                        },
                    },
                )

                return r

            r = TreeComment(
                    conjure_comment_operator(comment_operator_s),
                    first.comment,
                    conjure_token_newline(newline_s),
                )

            store_tree_comment(
                first.comment.s,
                {
                    first.comment_operator.s : first,
                    r.comment_operator.s     : r,
                },
            )

            return r

        second = first.get(comment_operator_s)

        if second is none:
            comment_operator = conjure_comment_operator(comment_operator_s)

            return first.setdefault(
                       comment_operator.s,
                       TreeComment(
                           comment_operator,
                           conjure_token_comment(comment_s),
                           conjure_token_newline(newline_s),
                       ),
                   )


        if second.__class__ is TreeComment:
            if second.newline.s == newline_s:
                return second

            r = TreeComment(second.comment_operator, second.comment, conjure_token_newline(newline_s))

            first[second.comment_operator.s] = {
                    second.newline.s : second,
                    r.newline.s      : r,
                }

            return r

        third = second.get(newline_s)

        if third is none:
            newline = conjure_token_newline(newline_s)

            return second.setdefault(
                       newline.s,
                       TreeComment(
                           conjure_comment_operator(comment_operator_s),
                           conjure_token_comment(comment_s),
                           newline,
                       ),
                   )

        return third


    if capital_global.testing:
        export(
            'tree_comment_cache',   tree_comment_cache,
        )
