#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.DefinitionHeader')
def gem():
    require_gem('Sapphire.Method')
    require_gem('Sapphire.Tree')


    class DefinitionHeader(SapphireTrunk):
        __slots__ = ((
            'frill',                    #   XY_Frill | Commented_VW_Frill
            'name',                     #   String
            'parameters',               #   Parameter_0 | Parameter_1 | Parameter_Many
        ))


        class_order                           = CLASS_ORDER__DEFINITION_HEADER
        is_any_else                           = false
        is_any_except_or_finally              = false
        is_class_decorator_or_function_header = true
        is_else_header_or_fragment            = false
        is_statement_header                   = true
        is_statement                          = false
        split_comment                         = 1


        __init__       = construct__123
        __repr__       = portray__123
        add_comment    = 0
        count_newlines = count_newlines__123


        def display_token(t):
            frill          = t.frill
            indented_token = frill.v

            return arrange('<%s +%d %s %s %s %s>',
                           t                         .display_name,
                           indented_token.indentation.total,
                           indented_token.token      .display_token(),
                           t             .name       .display_token(),
                           t             .parameters .display_token(),
                           frill         .b          .display_token())



        def dump_token(t, f, newline = true):
            assert newline is true

            frill          = t.frill
            indented_token = frill.v

            f.partial('<%s +%d ', t.display_name, indented_token.indentation.total)

            indented_token.token     .dump_token(f)
            t             .name      .dump_token(f)
            t             .parameters.dump_token(f)
            r = frill     .w         .dump_token(f, false)

            return f.token_result(r, newline)


        @property
        def indentation(t):
            return t.frill.v.indentation


        order = order__frill_ab


        def scout_variables(t, art):
            t.parameters.scout_variables(art)

            #
            #   t.name is handled elsewhere (add comment explaining where).
            #


        def write(t, w):
            frill = t.frill

            w(frill.v.s + t.name.s)
            t.parameters.write(w)
            w(frill.w.s)


    DefinitionHeader.a = DefinitionHeader.name
    DefinitionHeader.b = DefinitionHeader.parameters

    DefinitionHeader.k1 = DefinitionHeader.frill
    DefinitionHeader.k2 = DefinitionHeader.name
    DefinitionHeader.k3 = DefinitionHeader.parameters


    def produce_conjure_definition_header(name, Meta):
        cache          = create_cache(name, conjure_nub)
        conjure_triple = produce_conjure_unique_triple(name, Meta, cache)


        @rename('conjure_%s', name)
        def conjure_definition_header(indented_keyword, name, parameters, colon_newline):
            return conjure_triple(
                       conjure_vw_frill(indented_keyword, colon_newline),
                       name,
                       parameters,
                   )


        return ((
                   conjure_definition_header,
                   conjure_triple,
               ))


    @share
    class ClassHeader(DefinitionHeader):
        __slots__    = (())
        display_name = 'class-header'
        display_type = 'class'

        scout_variables = scout_variables__ab


    @share
    class FunctionHeader(DefinitionHeader):
        __slots__          = (())
        display_name       = 'function-header'
        display_type       = 'function'
        is_function_header = true


        if 0:
            def adorn(t, art):
                parameters = t.parameters

                parameters__2 = parameters.adorn(art)

                if parameters is parameters__2:
                    return t

                return conjure_function_header__with_frill(t.frill, t.name, parameters__2)


        def function_header_with_1_parameter(t, function_name, parameter_1_name):
            return (t.name.s == function_name) and (t.parameters.parameter_1_named(parameter_1_name))


    [
        conjure_class_header, conjure_class_header__with_frill,
    ] = produce_conjure_definition_header('class-header', ClassHeader)

    [
        conjure_function_header, conjure_function_header__with_frill,
    ] = produce_conjure_definition_header('function-header', FunctionHeader)


    ClassHeader.transform = produce_transform__frill__a__b_with_priority(
                                'class_header',
                                PRIORITY_TERNARY_LIST,
                                conjure_class_header__with_frill,
                            )


    FunctionHeader.transform = produce_transform__frill_ab('function_header', conjure_function_header__with_frill)


    share(
        'conjure_class_header',     conjure_class_header,
        'conjure_function_header',  conjure_function_header,
    )
