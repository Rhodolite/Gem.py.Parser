#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.Atom')
def module():
    require_module('CoreParser.ClassOrder')
    require_module('CoreParser.Method')
    require_module('CoreParser.ParserToken')
    require_module('CoreParser.TokenCache')


    lookup_atom  = lookup_normal_token
    provide_atom = provide_normal_token


    @export
    class DoubleQuote(ParserToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = '"'


        if capital_global.crystal_parser:
            is__atom__or__special_operator = true


        if capital_global.python_parser:
            is_atom                 = true
            is_colon                = false
            is_right_brace          = false
            is_right_parenthesis    = false
            is_right_square_bracket = false
            is_special_operator     = false


        def display_token(t):
            return arrange('<%s>', t.s)


        if capital_global.python_parser:
            mutate          = mutate__self
            scout_variables = scout_variables__0


    @export
    class TokenName(ParserToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = 'token-name'


        if capital_global.crystal_parser:
            is__atom__or__special_operator = true


        if capital_global.python_parser:
            is_atom             = true
            is_colon            = false
            is_identifier       = true
            is_right_brace      = false
            is_special_operator = false


        if capital_global.python_parser:
            def add_parameters(t, art):
               art.add_parameter(t)


        def display_token(t):
            return t.s


        if capital_global.python_parser:
            find_identifier = return_self


        if capital_global.python_parser:
            def is_name(t, s):
                return t.s == s


        if capital_global.python_parser:
            mutate = mutate__self


        if capital_global.python_parser:
            scout_default_values = scout_default_values__0


        if capital_global.python_parser:
            def scout_variables(t, art):
                art.fetch_variable(t)


        if capital_global.python_parser:
            transform = transform__self


        def write_variables(t, art):
            art.write_variable(t)


        write_import = write_variables


    @export
    class SingleQuote(ParserToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = "'"


        if capital_global.crystal_parser:
            is__atom__or__special_operator = true


        if capital_global.python_parser:
            is_atom                 = true
            is_colon                = false
            is_right_brace          = false
            is_right_parenthesis    = false
            is_right_square_bracket = false
            is_single_quote         = true
            is_special_operator     = false


        def display_token(t):
            return arrange('<%s>', t.s)


        if capital_global.python_parser:
            find_atom       = return_self
            mutate          = mutate__self
            scout_variables = scout_variables__0


    @export
    def produce_conjure_atom(name, Meta):
        assert type(name) is String
        assert type(Meta) is Type


        @rename('conjure_%s', name)
        def conjure_atom(s):
            r = lookup_atom(s)

            if r is not none:
                return r

            assert s.count('\n') is 0

            s = intern_string(s)

            return provide_atom(s, Meta(s))


        return conjure_atom


    conjure_double_quote = produce_conjure_atom('double-quote', DoubleQuote)
    conjure_name         = produce_conjure_atom('name', TokenName)
    conjure_single_quote = produce_conjure_atom('single-quote', SingleQuote)


    export(
        'conjure_double_quote',     conjure_double_quote,
        'conjure_name',             conjure_name,
        'conjure_single_quote',     conjure_single_quote,
    )


    if capital_global.sql_parser:
        export(
            'lookup_name',  lookup_atom,                                #   lookup_name = lookup_atom [on purpose]
        )
