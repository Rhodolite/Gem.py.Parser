#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@module('PythonParser.MosiacDefinition')
def module():
    def scout_variables__definition(t, art):
        t.a.scout_variables(art)
        art.add_definition(t)


    class ClassDefinition(DualTwig):
        __slots__                  = (())
        class_order                = CLASS_ORDER__DUAL_TWIG
        display_name               = 'class-definition'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_function_definition     = false
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#class-definition'

        dump_token          = dump_token__ab
        find_require_module = find_require_module__b
        indentation         = indentation__a_indentation
        scout_variables     = scout_variables__definition


    class FunctionDefinition(DualTwig):
        __slots__                  = (())
        class_order                = CLASS_ORDER__DUAL_TWIG
        display_name               = 'function-definition'
        is_any_else                = false
        is_any_except_or_finally   = false
        is_else_header_or_fragment = false
        is_function_definition     = true
        is_statement_header        = false
        is_statement               = true
        prefix                     = 0
        prefixed_display_name      = '#function-definition'


        if 0:
            def adorn(t, art):
                a = t.a
                b = t.b

                child_art = create_function_symbol_table(art)

                a.parameters.scout_variables(child_art)
                b           .scout_variables(child_art)

                if 7 is 7:
                    child_art.dump_variables('FunctionDefinition.adorn')

                a__2 = a#.adorn(child_art)
                b__2 = b#.adorn(child_art)

                if (a is a__2) and (b is b__2):
                    return t

                prefix = t.prefix

                if prefix is 0:
                    return conjure_function_definition(a__2, b__2)

                return conjure_prefixed_function_definition(prefix, a__2, b__2)


        dump_token          = dump_token__ab
        find_require_module = find_require_module__b
        indentation         = indentation__a_indentation
        scout_variables     = scout_variables__definition


    [
            conjure_class_definition, conjure_prefixed_class_definition,
    ] = produce_conjure_dual_twig_functions('class-definition',ClassDefinition)

    [
            conjure_function_definition, conjure_prefixed_function_definition,
    ] = produce_conjure_dual_twig_functions('function-definition', FunctionDefinition)


    #
    #   .conjure
    #
    ClassDefinition   .conjure = static_method(conjure_class_definition)
    FunctionDefinition.conjure = static_method(conjure_function_definition)


    #
    #   .conjure_prefixed_dual
    #
    FunctionDefinition.conjure_prefixed_dual = static_method(conjure_prefixed_function_definition)
    ClassDefinition   .conjure_prefixed_dual = static_method(conjure_prefixed_class_definition)


    #
    #   .transform
    #
    ClassDefinition.transform = produce_transform__a__b_with_indentation('class_definition', conjure_class_definition)

    FunctionDefinition.transform = produce_transform__a__b_with_indentation(
                                       'function_Definition',
                                       conjure_function_definition,
                                   )

    share(
        'conjure_class_definition',                 conjure_class_definition,
        'conjure_function_definition',              conjure_function_definition,

        'conjure_prefixed_class_definition',        conjure_prefixed_class_definition,
        'conjure_prefixed_function_definition',     conjure_prefixed_function_definition,
    )
