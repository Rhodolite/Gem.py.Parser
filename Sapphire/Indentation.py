#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.Indentation')
def gem():
    require_gem('Sapphire.Atom')
    require_gem('Sapphire.TokenCache')


    next_indentation_cache   = {}
    lookup_next_indentation  = next_indentation_cache.get
    provide_next_indentation = next_indentation_cache.setdefault


    class Indentation(PearlToken):
        __slots__ = ((
            'total',                    #   Integer {> 0}
        ))


        comment = 0


        class_order    = CLASS_ORDER__INDENTATION
        is_indentation = true


        def __init__(t, s):
            t.s     = intern_string(s)
            t.total = length(s)


        def count_newlines(t):
            assert (t.ends_in_newline is t.line_marker is false) and (t.newlines is 0)
            assert '\n' not in t.s

            return 0


        def display_short_token(t):
            return arrange('{+%d}', t.total)


        def display_token(t):
            if t.total is 0:
                return '{+0}'

            return arrange('{+%d %s}', t.total, portray_string(t.s))


        def mutate(t, vary, priority):
            if vary.remove_indentation:
                return vary.indentation

            return t


        order = order__s


        def transform(t, vary):
            if vary.remove_indentation:
                return vary.indentation

            return t


    def conjure_indentation(s):
        r = lookup_indentation(s)

        if r is not none:
            return r

        s = intern_string(s)

        return provide_indentation(s, Indentation(s))


    empty_indentation = conjure_indentation('')


    def next_indentation(indentation):
        return (
                      lookup_next_indentation(indentation)
                   or provide_next_indentation(indentation, conjure_indentation(indentation.s + ' '))
               )


    share(
        'conjure_indentation',  conjure_indentation,
        'empty_indentation',    empty_indentation,
        'next_indentation',     next_indentation,
    )
