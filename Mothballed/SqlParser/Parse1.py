#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('SqlParser.Parse1')
def gem():
    require_gem('SqlParser.Comment')
    require_gem('SqlParser.ConjureTreeComment')
    require_gem('SqlParser.Match')


    show = true


    @share
    def parse1_mysql_from_path(path):
        data = read_text_from_path(path)

        parse_context = z_initialize(path, data)

        many   = []
        append = many.append

        for s in parse_context.iterate_lines:
            m1 = mysql_line_match(s)

            if m1 is none:
                raise_unknown_line()

            identifier_s = m1.group('identifier')

            if identifier_s is not none:
                identifier = lookup_name(identifier_s)

                if identifier is none:
                    lower = identifier_s.lower()

                    line('lower: %s', lower)

                identifier_start = m1.start('identifier')

                line('identifier_start: %d', identifier_start)
                line('identifier: %r', identifier)
                line('identifier_s: %r', identifier)

            comment_start = m1.end('pound_sign')

            if comment_start is -1:
                #
                #   '+ 1' due to the required space after --.
                #
                comment_start = m1.end('dash_dash') + 1

                if comment_start is 0:                          #   '0' instead of '-1' due to the '+ 1' above.
                    append(conjure_empty_line(s))
                    continue

                comment_end = m1.end('dash_dash_comment')

                if comment_end is -1:
                    append(conjure_comment_newline(s))
                    continue

                append(conjure_tree_comment(s[:comment_start], s[comment_start : comment_end], s[comment_end:]))
                continue

            comment_end = m1.end('pound_sign_comment')

            if comment_end is -1:
                append(conjure_comment_newline(s))
                continue

            append(conjure_tree_comment(s[:comment_start], s[comment_start : comment_end], s[comment_end:]))
            continue

        if show:
            for v in many:
                line('%r', v)

        with create_StringOutput() as f:
            w = f.write

            for v in many:
                v.write(w)

        if data != f.result:
            with create_DelayedFileOutput('oops.txt') as oops:
                oops.write(f.result)

            raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')
