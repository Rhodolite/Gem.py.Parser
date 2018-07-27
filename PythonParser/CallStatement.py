#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.CallStatement')
def gem():
    require_gem('PythonParser.BookcaseExpression')
    require_gem('PythonParser.MemberExpression')
    require_gem('PythonParser.Method')


    class CallStatementBase(BookcaseCoupleTwig):
        __slots__ = (())


        class_order                = CLASS_ORDER__CALL_STATEMENT
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def add_comment(t, comment):
            frill = t.frill

            assert frill.comment is 0

            return t.conjure_call(
                       conjure_commented_vw_frill(comment, frill.v, frill.w),
                       t.left,
                       t.arguments,
                   )


        def find_require_gem(t, e):
            if not t.left.is_name('require_gem'):
                return

            assert t.arguments.is_arguments_1

            e.add_require_gem(t.arguments.a)


        @property
        def indentation(t):
            return t.frill.v


        def display_token(t):
            frill   = t.frill
            comment = frill.comment

            return arrange('<%s +%d%s %s %s %s>',
                           t.display_name,
                           frill.v.total,
                           (''   if comment is 0 else   comment.display_token()),
                           t.left     .display_token(),
                           t.arguments.display_token(),
                           frill.w    .display_token())


        def dump_token(t, f, newline = true):
            frill   = t.frill
            comment = frill.comment

            if comment is 0:
                f.partial('<%s +%d ', t.display_name, frill.v.total)

                t        .left     .dump_token(f)
                t        .arguments.dump_token(f)
                r = frill.w        .dump_token(f, false)

                return f.token_result(r, newline)

            with f.indent(arrange('<%s +%d', t.display_name, frill.v.total), '>'):
                comment    .dump_token(f)
                t.left     .dump_token(f)
                t.arguments.dump_token(f)
                frill.w    .dump_token(f)


        order = order__frill_ab


        def scout_variables(t, art):
            t.left     .scout_variables(art)
            t.arguments.scout_variables(art)


        def write(t, w):
            frill   = t.frill
            comment = frill.comment

            if comment is not 0:
                comment.write(w)

            w(frill.v.s)
            t.left     .write(w)
            t.arguments.write(w)
            w(frill.w.s)


    CallStatementBase.left      = CallStatementBase.a 
    CallStatementBase.arguments = CallStatementBase.b


    @share
    class CallStatement(CallStatementBase):
        __slots__    = (())
        display_name = 'call-statement'


    @share
    class MethodCallStatement(CallStatementBase):
        __slots__    = (())
        display_name = 'method-call-statement'


    conjure_call_statement        = produce_conjure_bookcase_couple_twig('call-statement',        CallStatement)
    conjure_method_call_statement = produce_conjure_bookcase_couple_twig('method-call-statement', MethodCallStatement)


    static_conjure_call_statement        = static_method(conjure_call_statement)
    static_conjure_method_call_statement = static_method(conjure_method_call_statement)

    MemberExpression.call_statement = static_conjure_method_call_statement
    ParserToken     .call_statement = static_conjure_call_statement
    ParserTrunk     .call_statement = static_conjure_call_statement

    CallStatement      .conjure_call = static_conjure_call_statement
    MethodCallStatement.conjure_call = static_conjure_method_call_statement


    CallStatement.transform = produce_transform__frill__ab_with_priority(
            'call_statement',
            PRIORITY_POSTFIX,
            PRIORITY_COMPREHENSION,
            conjure_call_statement,
        )

    MethodCallStatement.transform = produce_transform__frill__ab_with_priority(
            'method_call_statement',
            PRIORITY_POSTFIX,
            PRIORITY_COMPREHENSION,
            conjure_method_call_statement,
        )
