#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.MemberExpression')
def gem():
    require_gem('Sapphire.PostfixExpression')


    member_expression_cache = {}


    @share
    class MemberExpression(SapphireTrunk):
        __slots__ = ((
            'left',                     #   Expression
            'postfix',                  #   DotName
        ))


        class_order = CLASS_ORDER__MEMBER_EXPRESSION


        def __init__(t, left, postfix):
            t.left    = left
            t.postfix = postfix


        def __repr__(t):
            return arrange('<%s %r %r>', t.__class__.__name__, t.left, t.postfix)


        def count_newlines(t):
            return t.left.count_newlines() + t.postfix.count_newlines()


        def display_token(t):
            return arrange('<member %s %s>', t.left.display_token(), t.postfix.display_token())


        def dump_token(t, f, newline = true):
            f.partial('<member ')

            t    .left   .dump_token(f)
            r = t.postfix.dump_token(f, false)

            return f.token_result(r, newline)


        is_name = is_name__0
        order   = order__ab


        def scout_variables(t, art):
            t.left.scout_variables(art)

            #
            #   t.postfix - not relevant yet -- relevant later when tracking class members
            #


        def write_import(t, art):
            t.left.write_import(art)


        def write_variables(t, art):
            t.left.scout_variables(art)

            #
            #   t.postfix - not relevant yet -- relevant later when tracking class members
            #


        def write(t, w):
            t.left.write(w)
            w(t.postfix.s)


    MemberExpression.a = MemberExpression.left
    MemberExpression.b = MemberExpression.postfix


    #MemberExpression.k1 = MemberExpression.left
    MemberExpression.k2 = MemberExpression.postfix


    static_conjure_call_expression = static_method(conjure_call_expression)


    MemberExpression.call_expression = static_method(conjure_method_call_expression)
    PearlToken      .call_expression = static_conjure_call_expression
    SapphireTrunk   .call_expression = static_conjure_call_expression


    conjure_member_expression = produce_conjure_dual('member-expession', MemberExpression, member_expression_cache)


    MemberExpression.mutate = produce__mutate__ab__priority(
                                  'member-expression',
                                  conjure_member_expression,
                                  PRIORITY_POSTFIX,
                                  PRIORITY_POSTFIX,
                              )

    append_cache('member-expression', member_expression_cache)


    share(
        'conjure_member_expression',    conjure_member_expression,
    )
