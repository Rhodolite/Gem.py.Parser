#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.DualStatement')
def gem():
    @share
    def dump_token__ab(t, f, newline = true):
        assert newline is true

        with f.indent(arrange('<%s +%d', t.display_name, t.a.indentation.total), '>'):
            t.a.dump_token(f)
            t.b.dump_token(f)


    def find_require_gem__ab(t, e):
        t.a.find_require_gem(e)
        t.b.find_require_gem(e)


    @property
    def indentation__a_indentation(t):
        return t.a.indentation


    class DualStatement(DualTwig):
        __slots__                  = (())
        class_order                = CLASS_ORDER__DUAL_TWIG
        display_name               = 'dual-statement'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true

        dump_token       = dump_token__ab
        find_require_gem = find_require_gem__ab
        indentation      = indentation__a_indentation
        scout_variables  = scout_variables__ab


    class CommentedStatement(DualTwig):
        __slots__                  = (())
        class_order                = CLASS_ORDER__DUAL_TWIG
        display_name               = '#statement'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_statement_header        = false
        is_statement               = true


        def dump_token(t, f, newline = true):
            assert newline is true

            with f.indent(arrange('<%s +%d', t.display_name, t.b.indentation.total), '>'):
                t.a.dump_token(f)
                t.b.dump_token(f)


        find_require_gem = find_require_gem__b


        @property
        def indentation(t):
            return t.b.indentation


        def scout_variables(t, art):
            #
            #   t.a: comment - no need to scout
            #
            t.b.scout_variables(art)


        def transform(t, vary):
            a = t.a
            b = t.b

            a__2 = a.transform(vary)
            b__2 = b.transform(vary)

            if (a is a__2) and (b is b__2):
                return t

            if a__2 is 0:
                return b__2

            return conjure_commented_statement(a__2, b__2)



    conjure_commented_statement = produce_conjure_dual_twig('#statement',     CommentedStatement)
    conjure_dual_statement      = produce_conjure_dual_twig('dual-statement', DualStatement)


    DualStatement.transform = produce_transform__ab('dual-statement', conjure_dual_statement)


    share(
        'conjure_commented_statement',  conjure_commented_statement,
        'conjure_dual_statement',       conjure_dual_statement,
        'indentation__a_indentation',   indentation__a_indentation,
    )
