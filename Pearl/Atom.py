#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Pearl.Atom')
def gem():
    require_gem('Pearl.ClassOrder')
    require_gem('Pearl.Method')
    require_gem('Pearl.Nub')


    lookup_atom  = lookup_normal_token
    provide_atom = provide_normal_token


    def count_newlines__zero(t):
        assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
        assert (t.s is intern_string(t.s))

        return 0


    @export
    class PearlToken(Object):
        __slots__ = ((
            's',
        ))


        ends_in_newline                  = false
        herd_estimate                    = 0
        is_comma                         = false
        is_comment_line                  = false
        is_comment__or__empty_line       = false
        is_empty_line                    = false
        is_end_of_data                   = false
        is_end_of_data__or__unknown_line = false
        is_herd                          = false
        is_identifier                    = false
        is_indentation                   = false
        is_keyword                       = false
        is_keyword_return                = false
        is_right_parenthesis             = false
        is_right_square_bracket          = false
        line_marker                      = false
        newlines                         = 0


        def __init__(t, s):
            t.s = s


        def __repr__(t):
            return arrange('<%s %r>', t.__class__.__name__, t.s)


        count_newlines = count_newlines__zero


        def display_short_token(t):
            return arrange('{%s}', portray_string(t.s)[1:-1])


        def display_full_token(t):
            return arrange('<%s %s>', t.display_name, portray_string(t.s))


        def dump_token(t, f, newline = true):
            if t.ends_in_newline:
                if t.newlines is 1:
                    f.partial('{%s}', portray_string(t.s)[1:-1])
                else:
                    many = t.s.splitlines(true)

                    f.partial('{')

                    for s in many[:-1]:
                        f.line(portray_string(s)[1:-1])

                    f.partial('%s}', portray_string(many[-1])[1:-1])

                if newline:
                    f.line()
                    return false

                return true

            if t.newlines is 0:
                f.partial('{%s}', portray_string(t.s)[1:-1])
                return

            many = t.s.splitlines(true)

            f.partial('{')

            for s in many[:-1]:
                f.line(portray_string(s)[1:-1])

            f.partial('%s}', portray_string(many[-1])[1:-1])


        display_token = __repr__
        is_name       = is_name__0
        nub           = static_conjure_nub
        order         = order__s


        def write(t, w):
            w(t.s)


    @export
    class Identifier(PearlToken):
        __slots__                      = (())
        class_order                    = CLASS_ORDER__NORMAL_TOKEN
        display_name                   = 'Identifier'
        is__atom__or__special_operator = true
        is_atom                        = true
        is_colon                       = false
        is_identifier                  = true
        is_right_brace                 = false
        is_special_operator            = false


        def add_parameters(t, art):
            art.add_parameter(t)


        def display_token(t):
            return t.s


        find_identifier = return_self


        def is_name(t, s):
            return t.s == s


        mutate               = mutate__self
        scout_default_values = scout_default_values__0


        def scout_variables(t, art):
            art.fetch_variable(t)


        transform = transform__self


        def write_variables(t, art):
            art.write_variable(t)


        write_import = write_variables


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


    conjure_name = produce_conjure_atom('name', Identifier)


    export(
        'conjure_name',     conjure_name,
    )
