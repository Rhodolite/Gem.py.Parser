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

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_colon         = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #<atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false

        if PYTHON_parser:
            is_colon                = false
            is_right_brace          = false
            is_right_square_bracket = false


        def display_token(t):
            return arrange('<%s>', t.s)


        if PYTHON_parser:
            mutate          = mutate__self
            scout_variables = scout_variables__0


    @export
    class SingleQuote(ParserToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = "'"

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_colon         = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #</atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false

        if PYTHON_parser:
            is_colon                = false
            is_right_brace          = false
            is_right_square_bracket = false
            is_single_quote         = true


        def display_token(t):
            return arrange('<%s>', t.s)


        if PYTHON_parser:
            find_atom       = return_self
            mutate          = mutate__self
            scout_variables = scout_variables__0


    @export
    class TokenName(ParserToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = 'token-name'

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_identifier                            = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_colon         = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #</atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false

        if PYTHON_parser:
            is_colon                                  = false
            is_right_brace                            = false
            is_PYTHON__identifier__or__star_parameter = true


        if PYTHON_parser:
            def add_parameters(t, art):
               art.add_parameter(t)


        def display_token(t):
            return t.s


        if PYTHON_parser:
            find_identifier = return_self


        if PYTHON_parser:
            def is_name(t, s):
                return t.s == s


        if PYTHON_parser:
            mutate = mutate__self


        if PYTHON_parser:
            scout_default_values = scout_default_values__0


        if PYTHON_parser:
            def scout_variables(t, art):
                art.fetch_variable(t)


        if PYTHON_parser:
            transform = transform__self


        def write_variables(t, art):
            art.write_variable(t)


        write_import = write_variables


    @export
    class TokenNumber(ParserToken):
        __slots__    = (())
        class_order  = CLASS_ORDER__NORMAL_TOKEN
        display_name = 'number'

        #<atom>
        if CRYSTAL_parser:
            is_CRYSTAL_atom                                  = true
            is_CRYSTAL_simple_atom__or__colon                = true
            is_CRYSTAL_simple_atom__or__right_brace          = true
            is_CRYSTAL_simple_atom__or__right_parenthesis    = true
            is_CRYSTAL_simple_atom__or__right_square_bracket = true

        if TREMOLITE_parser:
            is_TREMOLITE___simple_atom___or___at_colon         = true
            is_TREMOLITE___simple_atom___or___set__right_brace = true
        #</atom>

        if CRYSTAL_parser:
            is_left_parenthesis = false

        if PYTHON_parser:
            is_colon                = false
            is_right_brace          = false
            is_right_square_bracket = false


        def display_token(t):
            return t.s


        if PYTHON_parser:
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
    conjure_name         = produce_conjure_atom('token-name', TokenName)
    conjure_single_quote = produce_conjure_atom('single-quote', SingleQuote)
    conjure_token_number = produce_conjure_atom('token-number', TokenNumber)


    export(
        'conjure_double_quote',     conjure_double_quote,
        'conjure_name',             conjure_name,
        'conjure_single_quote',     conjure_single_quote,
        'conjure_token_number',     conjure_token_number,
    )


    if SQL_parser:
        export(
            'lookup_name',  lookup_atom,                                #   lookup_name = lookup_atom [on purpose]
        )
