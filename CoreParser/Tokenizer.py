#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.Tokenizer')
def module():
    tokenizer = [none, 0, 0, 0, none, none, none, 0]

    query = tokenizer.__getitem__
    write = tokenizer.__setitem__

    #
    #   NOTE:
    #       Not currently used (other than `lz`?)
    #
    #   TODO:
    #       Investigate this
    #
    line_tokens = []

    #la = line_tokens.append
    #lt = Method(Tuple, line_tokens)
    lz = Method(line_tokens.__delitem__, slice_all)

    #
    #   q = Query
    #
    qs = Method(query, 0)                   #   `s` - The line being parsed
    qd = Method(query, 1)                   #   `d` - Depth of '(', '[', & '{'
    qi = Method(query, 2)                   #   `i` - Where the current token begins
    qj = Method(query, 3)                   #   `j` - Where the current token ends
    qk = Method(query, 4)                   #   `k` - Unknown
    ql = Method(query, 5)                   #   `l` - Line number
    qn = Method(query, 6)                   #   `n` - Python Line Marker (Newline)
    qp = Method(query, 7)                   #   `p` - Unknown

    #
    #   w = write
    #
    ws = Method(write, 0)
    wd = Method(write, 1)
    wi = Method(write, 2)
    wj = Method(write, 3)
    wk = Method(write, 4)
    wl = Method(write, 5)
    wn = Method(write, 6)
    wp = Method(write, 7)

    #
    #   Very fast writes
    #
    wd0 = Method(wd, 0)                     #   `d` = 0
    wd1 = Method(wd, 1)                     #   `d` = 1
    wi0 = Method(wi, 0)                     #   `i` = 0
    wj0 = Method(wj, 0)                     #   `j` = 0


    construct_Exception = Exception.__init__


    class UnknownLineException(Exception):
        __slots__ = ((
            'unknown_line',             #   Unknown_line
        ))


        def __init__(t, message, unknown_line):
            construct_Exception(t, message)

            t.unknown_line = unknown_line


    class ParseContext(Object):
        __slots__ = ((
            'cadence',                  #   Cadence
            'data_lines',               #   Tuple of *
            'iterate_lines',            #   None | Generator
            'many',                     #   Tuple of *
            'append',                   #   Method
        ))


        def __init__(t):
            t.cadence = cadence_constructing

            t.iterate_lines = none
            t.many          = many                = []
            t.append        = many.append

            t.cadence = cadence_initialized


        def __enter__(t):
            assert t.cadence.is_initialized_exited_exception_or_reuse

            t.cadence = cadence_entered


        def __exit__(t, e_type, e, e_traceback):
            with exit_clause(e_type, e, e_traceback):
                cadence = t.cadence

                t.cadence = cadence_exception

                assert cadence is cadence_entered

                if e is none:
                   t.cadence = cadence_exited
                   return

                if type(e) is not UnknownLineException:
                    return

                lz()
                wd0()
                t.append(e.unknown_line)

                return true


        def __iter__(t):
            loop = 0

            while t.cadence is not cadence_exited:
                yield loop

                loop += 1


        def reset(t, data_lines, iterate_lines):
            assert t.cadence.is_initialized_exited_or_exception

            t.cadence = cadence_exception

            del t.many[:]

            t.data_lines    = data_lines
            t.iterate_lines = iterate_lines

            t.cadence = cadence_reuse

            return t


    class UnknownLine(String):
        __slots__                        = (())
        display_name                     = 'unknown-line'
        ends_in_newline                  = true
        indentation                      = none
        is_end_of_data__or__unknown_line = true
        is_any_else                      = false
        is_any_except_or_finally         = false
        is_comment__or__empty_line       = false
        is_end_of_data                   = false
        is_statement_header              = false
        is_statement                     = true
        line_marker                      = true
        newlines                         = 1


        def __repr__(t):
            return arrange('<UnknownLine %s>', portray_string(t))


        def count_newlines(t):
            assert (t.ends_in_newline is t.line_marker is true) and (t.newlines is 1)
            assert (t.count('\n') is 1) and (t[-1] == '\n')

            return 1


        display_token = __repr__


        def dump_token(t, f, newline = true):
            assert newline is true

            f.line(t.display_token())


        def write(t, w):
            w(t)


    parse_context = ParseContext()


    @export
    def z_initialize(path, data):
        data_lines = Tuple(data.splitlines(true))
        maximum_i  = length(data_lines)
        q_data     = data_lines.__getitem__


        def GENERATOR_next_line():
            line_number = 0

            for s in data_lines:
                line_number += 1

                ws(s)
                wi0()
                wj0()
                wl(line_number)
                wk(none)
                wn(none)

                yield s

            lz()
            wd0()
            ws(none)
            wi0()
            wj0()
            wl(none)
            wk(none)
            wn(none)
            wp(none)


        wp(path)


        return parse_context.reset(data_lines, GENERATOR_next_line())


    @export
    def raise_unknown_line():
        caller_frame = caller_frame_1()
        caller_name  = caller_frame.f_code.co_name
        basename     = path_basename(caller_frame.f_code.co_filename)

        line('??? %s#%s: %s; %s:%s', basename, caller_frame.f_lineno, caller_name, qp(), ql())

        unknown_line_error = UnknownLineException(
                                 arrange('parse incomplete: %s#%s: %s; %s:%s',
                                         basename, caller_frame.f_lineno, caller_name, qp(), ql()),
                                 UnknownLine(qs()),
                             )

        raising_exception(unknown_line_error)

        raise unknown_line_error


    export(
        'parse_context',    parse_context,

        'qd',               qd,
        'qi',               qi,
        'qj',               qj,
        'qk',               qk,
        'ql',               ql,
        'qn',               qn,
        'qs',               qs,

        'wd',               wd,
        'wd0',              wd0,
        'wd1',              wd1,
        'wi',               wi,
        'wj',               wj,
        'wk',               wk,
        'wn',               wn,
        'ws',               ws,
    )
