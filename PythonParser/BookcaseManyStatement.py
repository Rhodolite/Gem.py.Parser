#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.BookcaseManyStatement')
def module():
    require_module('PythonParser.BookcaseManyExpression')


    def write__comment_many(t, w):
        begin = t.frill.begin

        begin.comment.write(w)
        w(begin.v.s)
        write__X__many_end(t, w)


    def scout_variables__assign_statement_many(t, art):
        i          = 0
        maximum_m1 = length(t.many) - 1

        for v in t.many:
            if i == maximum_m1:
                v.scout_variables(art)
                return

            v.write_variables(art)
            i += 1


    def scout_variables__delete_statement_many(t, art):
        for v in t.many:
            v.write_variables(art)


    def produce_transform_comment_statement_many(
                name, first_priority, middle_priority, last_priority, conjure_with_frill,
                conjure_uncommented__with_frill,
    ):
        @rename('transform_%s', name)
        def transform(t, vary):
            frill    = t.frill
            many     = t.many

            frill__2 = frill .transform(vary)
            many__2  = t.many.morph    (vary, first_priority, middle_priority, last_priority)

            if (frill is frill__2) and (many is many__2):
                return t

            return (
                       conjure_uncommented__with_frill   if frill__2.begin.comment is 0 else
                       conjure_with_frill
                   )(frill__2, many__2)


        return transform


    def produce_transform_statement_many(name, first_priority, middle_priority, last_priority, conjure_with_frill):
        @rename('transform_%s', name)
        def transform(t, vary):
            frill    = t.frill
            many     = t.many

            frill__2 = frill .transform(vary)
            many__2  = t.many.morph    (vary, first_priority, middle_priority, last_priority)

            if (frill is frill__2) and (many is many__2):
                return t

            return conjure_with_frill(frill__2, many__2)


        return transform


    class AssignStatement_Many(BookcaseManyExpression):
        __slots__                  = (())
        display_name               = 'assign-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        def add_comment(t, comment):
            frill = t.frill

            assert frill.begin.comment is 0

            return conjure_comment_assign_many(conjure_commented_v_frill(comment, frill.begin), t.many, frill.many, frill.end)


        def display_token(t):
            frill = t.frill
            begin = frill.begin

            return arrange('<assign-* +%d %s %s %s>',
                           begin.total,
                           ' '.join(v.display_token()   for v in t.many),
                           frill.many.display_token(),
                           frill.end.display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<assign-* +%d ', frill.begin.total)

            dump_token__X__many(t, f)

            r = frill.end.dump_token(f, false)

            return f.token_result(r, newline)


        find_require_module = find_require_module__0
        scout_variables     = scout_variables__assign_statement_many


        @property
        def indentation(t):
            return t.frill.begin


    class Comment_AssignStatement_Many(BookcaseManyExpression):
        __slots__                  = (())
        display_name               = '#assign-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        def display_token(t):
            frill = t.frill
            begin = frill.begin

            return arrange('<#assign-* +%d %s %s %s %s>',
                           begin.      v.total,
                           begin.comment.display_token(),
                           ' '.join(v   .display_token()   for v in t.many),
                           frill.many   .display_token(),
                           frill.end    .display_token())


        def dump_token(t, f, newline = true):
            frill = t.frill
            begin = frill.begin

            with f.indent(arrange('<#assign-* +%d ', begin.v.total), '>'):
                begin.comment.dump_token(f)
                dump_token__X__many(t, f)
                frill.end    .dump_token(f)


        find_require_module = find_require_module__0


        @property
        def indentation(t):
            return t.frill.begin.v


        scout_variables = scout_variables__assign_statement_many
        write           = write__comment_many


    class Comment_DeleteStatement_Many(BookcaseManyExpression):
        __slots__                  = (())
        display_name               = '#delete-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        @property
        def indentation(t):
            return t.frill.begin.w.a


        def display_token(t):
            frill          = t.frill
            begin          = frill.begin
            comment        = begin.comment
            indented_token = begin.v

            return arrange('<#delete-* +%d %s %s %s %s %s>',
                           indented_token.a.total,
                           indented_token.b.display_token(),
                           comment         .display_token(),
                           ' '.join(v      .display_token()   for v in t.many),
                           frill.many      .display_token(),
                           frill.end       .display_token())


        def dump_token(t, f, newline = true):
            frill          = t.frill
            begin          = frill.begin
            comment        = begin.comment
            indented_token = begin.v

            with f.indent(arrange('<#delete-* +%d ', indented_token.a.total), '>'):
                comment           .dump_token(f)
                indented_token.b  .dump_token(f)
                dump_token__X__many(t, f)
                frill         .end.dump_token(f)


        find_require_module = find_require_module__0
        scout_variables     = scout_variables__delete_statement_many
        write               = write__comment_many


    class DeleteStatement_Many(BookcaseManyExpression):
        __slots__                  = (())
        display_name               = 'delete-*'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement               = true
        is_statement_header        = false


        def add_comment(t, comment):
            frill = t.frill

            return conjure_comment_delete_many(conjure_vw_frill(comment, frill.begin), t.many, frill.many, frill.end)


        @property
        def indentation(t):
            return t.frill.begin.a


        def display_token(t):
            frill          = t.frill
            indented_token = frill.begin

            return arrange('<delete-* +%d %s %s %s %s>',
                           indented_token.a   .total,
                           indented_token.b   .display_token(),
                           ' '.join(v         .display_token()   for v in t.many),
                           frill         .many.display_token(),
                           frill         .end .display_token())


        def dump_token(t, f, newline = true):
            frill          = t.frill
            indented_token = frill.begin

            f.partial('<delete-* +%d ', indented_token.a.total)
            indented_token.b.dump_token(f)

            dump_token__X__many(t, f)

            r = frill.end.dump_token(f, false)

            return f.token_result(r, newline)


        find_require_module = find_require_module__0
        scout_variables     = scout_variables__delete_statement_many


    [
        conjure_assign_many, conjure_assign_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'assign-*',
            AssignStatement_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_comment_assign_many, conjure_comment_assign_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            '#assign-*',
            Comment_AssignStatement_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_comment_delete_many, conjure_comment_delete_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            '#delete-*',
            Comment_DeleteStatement_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_delete_many, conjure_delete_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'delete-*',
            DeleteStatement_Many,

            produce_conjure_with_frill = 1,
        )


    #
    #   .transform
    #
    AssignStatement_Many.transform = produce_transform_statement_many(
                                         'assign_statement_many',
                                         PRIORITY_ASSIGN,
                                         PRIORITY_ASSIGN,
                                         PRIORITY_YIELD,
                                         conjure_assign_many__with_frill,
                                     )

    Comment_AssignStatement_Many.transform = produce_transform_comment_statement_many(
                                                 'comment_assign_statement_many',
                                                 PRIORITY_ASSIGN,
                                                 PRIORITY_ASSIGN,
                                                 PRIORITY_YIELD,
                                                 conjure_comment_assign_many__with_frill,
                                                 conjure_assign_many__with_frill,
                                             )

    DeleteStatement_Many.transform = produce_transform_statement_many(
                                         'delete_statement_many',
                                         PRIORITY_NORMAL,
                                         PRIORITY_NORMAL,
                                         PRIORITY_NORMAL,
                                         conjure_delete_many__with_frill,
                                     )


    share(
        'conjure_assign_many',      conjure_assign_many,
        'conjure_delete_many',      conjure_delete_many,
    )
