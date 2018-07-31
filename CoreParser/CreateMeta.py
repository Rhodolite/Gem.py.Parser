#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.CreateMeta')
def module():
    adjusted_meta_cache  = {}
    lookup_adjusted_meta = adjusted_meta_cache.get
    store_adjusted_meta  = adjusted_meta_cache.__setitem__


    @export
    def conjure_ActionWord_WithNewlines(Meta, constructor):
        ActionWord_WithNewlines = lookup_adjusted_meta(Meta)

        if ActionWord_WithNewlines is none:
            class ActionWord_WithNewlines(Meta):
                __slots__ = ((
                    'ends_in_newline',                          #   Boolean
                    'newlines',                                 #   Integer > 0
                ))


                __init__ = constructor


                def count_newlines(t):
                    assert t.ends_in_newline is (t.s[-1] == '\n')
                    assert t.line_marker is false
                    assert t.newlines == t.s.count('\n')

                    return t.newlines


            if python_debug_mode:
                ActionWord_WithNewlines.__name__ = intern_arrange('%s_WithNewlines', Meta.__name__)

            store_adjusted_meta(Meta, ActionWord_WithNewlines)

        return ActionWord_WithNewlines


    if python_debug_mode:
        @share
        def dump_newline_meta_cache():
            for k in iterate_values_sorted_by_key({ k.__name__ : k   for k in adjusted_meta_cache }):
                line('%s:', k.__name__)
                line('    %s', adjusted_meta_cache[k].__name__)


    export(
        'lookup_adjusted_meta',     lookup_adjusted_meta,
        'store_adjusted_meta',      store_adjusted_meta,
    )
