#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.DualExpressionStatement')
def module():
    require_module('CoreParser.BookcaseDualTwig')


    #
    #   DualExpressionStatement:
    #
    #       A statement with two expressions, seperated by an operator.
    #
    #       The frill is as follows:
    #
    #           `.frill.comment`    - An optional preceeding comment; or `0` if no comment.
    #           `.frill.v`          - indentation.
    #           `.frill.w`          - The operator.
    #           `.frill.x`          - The line marker.
    #
    #       Uses a `BookcaseDualTwig` with the following changes:
    #
    #           The `frill` can be either:
    #
    #           1.  `VWX_Frill`                 - in which vase `frill.comment` is `0`
    #           2.  `Commented_VWX_Frill`       - in which vase `frill.comment` is a comment.
    #
    #           The comment is only outputed if it is not `0`, the is done in the three
    #           routines:
    #
    #               `.display_token__frill`
    #               `.dump_token__frill`
    #               `.write__frill`
    #
    #           which replace (respectivily):
    #
    #               `.display_token`
    #               `.dump_token`
    #               `.write`
    #
    #           When a [factory of a] `BookcaseDualTwig_WithFrill` derived class is created.
    #
    @export
    class DualExpressionStatement(BookcaseDualTwig):
        __slots__ = (())


        if capital_global.python_parser:
            is_any_else                = false
            is_any_except_or_finally   = false
            is_else_header_or_fragment = false
            is_statement_header        = false
            is_statement               = true


        #
        #   Here we have the default frill (as a class member in `.frill`), hence:
        #
        #       1.  No comment.
        #       2.  No indentation (i.e.: `.frill.v` is `empty_indentation`)
        #       3.  `.frill.v` is the keyword (with one space before & one space after)
        #       3.  `.frill.w` is a `LINE_MARKER`
        #
        #   Thus we do not display the default frill.
        #
        def display_token(t):
            assert t.frill.comment is 0
            assert t.frill.v.total is 0
        #   assert t.frill.w       is # An operator with one space before & one space after
            assert t.frill.x       is LINE_MARKER

            return arrange('<%s %s %s>', t.display_name, t.a.display_token(), t.b.display_token())


        def display_token__frill(t):
            frill   = t.frill
            comment = frill.comment

            return arrange('<%s+frill +%d%s %s %s %s %s>',
                           t.display_name,
                           frill.v.total,
                           (''   if comment is 0 else   ' ' + comment.display_token()),
                           t.a    .display_token(),
                           frill.w.display_token(),
                           t.b    .display_token(),
                           frill.x.display_token())


        #
        #   NOTE:
        #       See comments above in `display_token` as to the limitations of `.frill`
        #
        def dump_token(t, f, newline = true):
            frill = t.frill

            assert frill.comment is 0
            assert frill.v.total is 0
        #   assert frill.w       is # An operator with one space before & one space after
            assert frill.x       is LINE_MARKER

            f.partial('<%s ', t.display_name)

            t        .a.dump_token(f)
            frill    .w.dump_token(f)
            t        .b.dump_token(f)
            r = frill.x.dump_token(f, false)

            return f.token_result(r, newline)


        def dump_token__frill(t, f, newline = true):
            frill = t.frill

            comment = frill.comment

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, frill.v.total)

                t        .a.dump_token(f)
                frill    .w.dump_token(f)
                t        .b.dump_token(f)
                r = frill.x.dump_token(f, false)

                return f.token_result(r, newline)

            with f.indent(arrange('<%s +%d ', t.display_name, frill.v.total), '>'):
                comment  .dump_token(f)
                t      .a.dump_token(f)
                frill  .w.dump_token(f)
                t      .b.dump_token(f)
                frill  .x.dump_token(f)

            return false


        if capital_global.python_parser:
            @property
            def indentation(t):
                return t.frill.v


        if capital_global.python_parser:
            def scout_variables(t, art):
                t.a.write_variables(art)
                t.b.scout_variables(art)


        def write__frill(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.v.s)
            t.a.write(w)
            w(frill.w.s)
            t.b.write(w)
            w(frill.x.s)


    produce_dual_expression_statement = rename('produce_dual_expression_statement')(produce_conjure_bookcase_dual_twig)


    export(
        'produce_dual_expression_statement',    produce_dual_expression_statement,
    )
