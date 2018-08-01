#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.TokenizeOperator')
def module():
    @export
    def produce__LANGUAGE__skip_tokenize_prefix(language, next_LANGUAGE_nested_line_match):
        @rename('%s__skip_tokenize_prefix')
        def LANGUAGE__skip_tokenize_prefix():
            next = next_method(parse_context.iterate_lines)

            next()

            m = next_LANGUAGE_nested_line_match(qs())

            if m is none:
                raise_unknown_line()

            if m.group('comment_newline') is none:
                wj(m.end())
                return

            many = [qs()]

            while 7 is 7:
                next()

                s = qs()
                m = next_LANGUAGE_nested_line_match(s)

                if m is none:
                    raise_unknown_line()

                if m.group('comment_newline') is none:
                    prefix = ''.join(many)
                    total  = length(prefix)

                    ws(prefix + s)
                    wj(total + m.end())

                    return

                many.append(s)


        return LANGUAGE__skip_tokenize_prefix
