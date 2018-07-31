#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.ActionWord')
def module():
    require_module('CoreParser.CreateMeta')
    require_module('CoreParser.TokenCache')


    lookup_action_word  = lookup_normal_token
    provide_action_word = provide_normal_token


    action_word__Meta__cache = {}                   #   Map { String : Meta }

    find_action_word__Meta = action_word__Meta__cache.__getitem__


    def construct_token__with_newlines(t, s, ends_in_newline, newlines):
        t.s               = s
        t.ends_in_newline = ends_in_newline
        t.newlines        = newlines


    #
    #   conjure_action_word:
    #
    #       This version is not typically used, the more commonly used version is produced by
    #       `produce_conjure_action_word`, which is more efficient as that version is bound
    #       to the proper `Meta`.
    #
    #       This version, uses `find_action_word__Meta(full)` to find the proper `Meta`
    #       for the action word.
    #
    @export
    def conjure_action_word(full, s):
        assert s[-1] != '\n'

        r = lookup_action_word(s)

        if r is not none:
            return r

        s = intern_string(s)

        Meta     = find_action_word__Meta(full)
        newlines = s.count('\n')

        return provide_action_word(
                   s,
                   (
                       provide_action_word(s, Meta(s))
                           if newlines is 0 else
                               conjure_ActionWord_WithNewlines(
                                   Meta, construct_token__with_newlines,
                               )(s, false, newlines)
                   ),
               )


    @export
    def conjure_action_word__ends_in_newline(full, s):
        assert s[-1] == '\n'

        r = lookup_action_word(s)

        if r is not none:
            return r

        s = intern_string(s)

        Meta = find_action_word__Meta(full)

        return provide_action_word(
                   s,
                   conjure_ActionWord_WithNewlines(
                       Meta, construct_token__with_newlines,
                   )(s, true, s.count('\n'))
               )


    @export
    def initialize_action_word__Meta(many):
        provide_action_word__Meta = action_word__Meta__cache.setdefault

        for [k, Meta] in many:
            previous = provide_action_word__Meta(k, Meta)

            assert previous is Meta


    @export
    def produce_conjure_action_word(name, Meta, produce_ends_in_newline = false):
        assert type(name)                    is String
        assert type(Meta)                    is Type
        assert type(produce_ends_in_newline) is Boolean


        @rename('conjure_%s', name)
        def conjure_action_word(s):
            assert s[-1] != '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            s = intern_string(s)

            newlines = s.count('\n')

            return provide_action_word(
                       s,
                       (
                           Meta(s)
                               if newlines is 0 else
                                   conjure_ActionWord_WithNewlines(
                                       Meta, construct_token__with_newlines,
                                   )(s, false, newlines)
                       ),
                   )


        if produce_ends_in_newline is false:
            return conjure_action_word


        @rename('conjure_%s__ends_in_newline', name)
        def conjure_action_word__ends_in_newline(s):
            assert s[-1] == '\n'

            r = lookup_action_word(s)

            if r is not none:
                return r

            s = intern_string(s)

            return provide_action_word(
                       s,
                       conjure_ActionWord_WithNewlines(
                           Meta, construct_token__with_newlines,
                       )(s, true, s.count('\n'))
                   )


        return ((conjure_action_word, conjure_action_word__ends_in_newline))
