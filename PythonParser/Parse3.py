#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.Parse3')
def gem():
    debug = 0


    require_gem('PythonParser.DualStatement')
    require_gem('PythonParser.MosiacDefinition')
    require_gem('PythonParser.QuadrupleStatement')
    require_gem('PythonParser.Suite')
    require_gem('PythonParser.TripleStatement')


    @share
    def parse3_python(path, data, data_lines, data_many):
        data_many.append(end_of_data)

        data_iterator = iterate(data_many)
        next_line     = next_method(data_iterator)

        tree_many   = []
        append_twig = tree_many.append

        variables = [
                        0,                  #   0 = before
                        0,                  #   1 = comment
                        1,                  #   2 = split_comment
                        0,                  #   3 = v
                    ]

        query = variables.__getitem__
        write = variables.__setitem__

        qb      = Method(query, 0)
        qc      = Method(query, 1)
        q_split = Method(query, 2)
        qv      = Method(query, 3)

        wb      = Method(write, 0)
        wc      = Method(write, 1)
        w_split = Method(write, 2)
        wv      = Method(write, 3)

        wb0       = Method(wb,      0)
        wc0       = Method(wc,      0)
        w_split_1 = Method(w_split, 1)
        w_split_2 = Method(w_split, 2)
        wv0       = Method(wv,      0)


        def create_append():
            element = q_element()

            if element is none:
                many = []
            else:
                w_element_0()
                many = [element]

            append = many.append

            w_append(many)
            w_many(many)

            return append


        #
        #   parse_blank_line:
        #
        #       This routine is "rolled-out" at least three times ... Hard to read the first time (and second time
        #       and third time!), but the code is actualy "simplier" due to the 'unrolling' ("simplier" in the sense
        #       less conditions per loop, if it was not "rolled-out")
        #
        #   NOTE:
        #       This routine is super super complicated.  It took 4+ days to right!
        #
        def parse_blank_lines(v):
            assert qb() is qc() is qv() is 0

            #
            #   At this point:
            #       v:              first comment or empty line
            #
            #   Set soon:
            #       v_impression:   indentation if 'v' is a comment, or 0 if 'v' is an empty line
            #       w:              next line
            #       w_impression:   indentation if 'w' is a comment, or 0 if 'w' is an empty line
            #
            v_impression = v.impression
            w            = next_line()

            if not w.is_comment__or__empty_line:
                if v_impression is w.indentation:
                    assert (v.is_comment_line) and (not w.is_end_of_data)

                    add_comment = w.add_comment

                    if add_comment is not 0:
                        return add_comment(v)

                    if w.split_comment is q_split():
                        wc(v)
                        return w

                wb(v)
                return w

            w_impression = w.impression

            if v_impression is w_impression:
                if v_impression is 0:
                    assert (v.is_empty_line) and (w.is_empty_line)

                    empty_line_many = [v, w]

                    while 7 is 7:
                        w = next_line()

                        if w.is_empty_line:
                            empty_line_many.append(w)
                            continue

                        v = conjure_empty_line_suite(empty_line_many)

                        if w.is_comment_line:
                            w_impression = w.impression
                            break

                        wb(v)
                        return w
                else:
                    assert (v.is_comment_line) and (w.is_comment_line)

                    comment_many = [v, w]

                    while 7 is 7:
                        w = next_line()

                        if w.is_comment__or__empty_line:
                            w_impression = w.impression

                            if v_impression is w_impression:
                                comment_many.append(w)
                                continue

                            break

                        comment = conjure_comment_suite(comment_many)

                        if v_impression is w.indentation:
                            add_comment = w.add_comment

                            if add_comment is not 0:
                                return add_comment(comment)

                            if w.split_comment is q_split():
                                wc(comment)
                                return w

                        wb(comment)
                        return w

                    v = conjure_comment_suite(comment_many)

            #
            #   At this point:
            #       v:              first comment, empty line, suite of comments, or suite of empty lines
            #       w:              current comment or empty line
            #       w_impression:   indentation if 'w' is a comment, or 0 if 'w' is an empty line
            #
            #   Set soon:
            #       x:              next line
            #       x_impression:   indentation if 'x' is a comment, or 0 if 'x' is an empty line
            #
            x = next_line()

            if not x.is_comment__or__empty_line:
                if w_impression is x.indentation:
                    assert (w.is_comment_line) and (not x.is_end_of_data)

                    add_comment = x.add_comment

                    if add_comment is not 0:
                        wb(v)
                        return add_comment(w)

                    if x.split_comment is q_split():
                        wb(v)
                        wc(w)
                        return x

                wb([v, w])
                return x

            x_impression = x.impression

            if w_impression is not x_impression:
                mixed_many = [v, w]
            elif w_impression is 0:
                assert (w.is_empty_line) and (x.is_empty_line)

                empty_line_many = [w, x]

                while 7 is 7:
                    x = next_line()

                    if x.is_empty_line:
                        empty_line_many.append(x)
                        continue

                    empty_line_suite = conjure_empty_line_suite(empty_line_many)

                    if x.is_comment_line:
                        x_impression = x.impression
                        break

                    wb([v, empty_line_suite])
                    return x

                mixed_many = [v, empty_line_suite]
            else:
                assert (w.is_comment_line) and (x.is_comment_line)

                comment_many = [w, x]

                while 7 is 7:
                    x = next_line()

                    if x.is_comment__or__empty_line:
                        x_impression = x.impression

                        if w_impression is x_impression:
                            comment_many.append(x)
                            continue

                        break

                    comment = conjure_comment_suite(comment_many)

                    if w_impression is x.indentation:
                        add_comment = x.add_comment

                        if add_comment is not 0:
                            wb(v)
                            return add_comment(comment)

                        if x.split_comment is q_split():
                            wb(v)
                            wc(comment)
                            return x

                    wb([v, comment])
                    return x

                mixed_many = [v, conjure_comment_suite(comment_many)]

            #
            #   NOTE:
            #       Although 'mixed_many' might not be complete yet (and we might append more elements to it)
            #       ... we will always return it --- so store 'mixed_many' in 'b' now
            #
            wb(mixed_many)

            #
            #   At this point:
            #       v:              no longer used
            #       w:              no longer used
            #       mixed_many:     multiple mixed (returned as 'b')
            #       x:              current comment or empty line
            #       x_impression:   indentation if 'x' is a comment, or 0 if 'x' is an empty line
            #
            #   Set soon:
            #       y:              next line
            #       y_impression:   indentation if 'y' is a comment, or 0 if 'y' is an empty line
            #
            #
            y = next_line()

            if not y.is_comment__or__empty_line:
                if x_impression is y.indentation:
                    assert (x.is_comment_line) and (not y.is_end_of_data)

                    add_comment = y.add_comment

                    if add_comment is not 0:
                        return add_comment(x)

                    if y.split_comment is q_split():
                        wc(x)
                        return y

                mixed_many.append(x)
                return y

            y_impression = y.impression

            if x_impression is not y_impression:
                mixed_append = mixed_many.append

                mixed_append(x)
            elif x_impression is 0:
                assert (x.is_empty_line) and (y.is_empty_line)

                empty_line_many = [x, y]

                while 7 is 7:
                    y = next_line()

                    if y.is_empty_line:
                        empty_line_many.append(y)
                        continue

                    empty_line_suite = conjure_empty_line_suite(empty_line_many)

                    if y.is_comment_line:
                        y_impression = y.impression
                        break

                    mixed_many.append(empty_line_suite)
                    return y

                mixed_append = mixed_many.append

                mixed_append(empty_line_suite)
            else:
                assert (x.is_comment_line) and (y.is_comment_line)

                comment_many = [x, y]

                while 7 is 7:
                    y = next_line()

                    if y.is_comment__or__empty_line:
                        y_impression = y.impression

                        if x_impression is y_impression:
                            comment_many.append(y)
                            continue

                        break

                    comment = conjure_comment_suite(comment_many)

                    if x_impression is y.indentation:
                        add_comment = y.add_comment

                        if add_comment is not 0:
                            return add_comment(comment)

                        if y.split_comment is q_split():
                            wc(comment)
                            return y

                    mixed_many.append(comment)
                    return y

                mixed_append = mixed_many.append

                mixed_append(conjure_comment_suite(comment_many))

            #
            #   At this point:
            #       v:              no longer used
            #       w:              no longer used
            #       x:              no longer used
            #       mixed_many:     multiple mixed (returned as 'b')
            #       mixed_append:   append to mixed_many
            #       y:              current comment or empty line
            #       y_impression:   indentation if 'y' is a comment, or 0 if 'y' is an empty line
            #
            #   Set soon:
            #       z:              next line
            #       z_impression:   indentation if 'z' is a comment, or 0 if 'z' is an empty line
            #
            while 7 is 7:
                z = next_line()

                if not z.is_comment__or__empty_line:
                    if y_impression is z.indentation:
                        assert (y.is_comment_line) and (not z.is_end_of_data)

                        add_comment = z.add_comment

                        if add_comment is not 0:
                            return add_comment(y)

                        if z.split_comment is q_split():
                            wc(y)
                            return z

                    mixed_append(y)
                    return z

                if y_impression is not z.impression:
                    mixed_append(y)

                    y            = z
                    y_impression = z.impression
                    continue

                if y_impression is 0:
                    assert (y.is_empty_line) and (z.is_empty_line)

                    empty_line_many = [y, z]

                    while 7 is 7:
                        y = next_line()

                        if y.is_empty_line:
                            empty_line_many.append(y)
                            continue

                        mixed_append(conjure_empty_line_suite(empty_line_many))

                        if y.is_comment_line:
                            break

                        return y

                    y_impression = y.impression
                    continue

                assert (y.is_comment_line) and (z.is_comment_line)

                comment_many = [y, z]

                while 7 is 7:
                    y = next_line()

                    if y.is_comment__or__empty_line:
                        if y_impression is y.impression:
                            comment_many.append(y)
                            continue

                        break

                    comment = conjure_comment_suite(comment_many)

                    if y_impression is y.indentation:
                        add_comment = y.add_comment

                        if add_comment is not 0:
                            return add_comment(comment)

                        if y.split_comment is q_split():
                            wc(comment)
                            return y

                    mixed_append(comment)
                    return y

                mixed_append(conjure_comment_suite(comment_many))
                y_impression = y.impression


        if debug:
            original_parse_blank_lines = parse_blank_lines

            def show_parse_blank_lines(v):
                r = original_parse_blank_lines(v)

                my_line('v: %r', v)
                my_line('b: %r', qb())
                my_line('c: %r', qc())
                my_line('=> %r', r)
                line()

                return r

            parse_blank_lines = show_parse_blank_lines


        def parse_any_else_fragment(indentation):
            v = qv()

            if v is not 0:
                if (not v.is_any_else) or (v.indentation is not indentation):
                    return 0

                wv0()
            else:
                v = next_line()

                if v.is_comment__or__empty_line:
                    w_split_2()

                    v = parse_blank_lines(v)

                    w_split_1()

                if (not v.is_any_else) or (v.indentation is not indentation):
                    wv(v)
                    return 0

            assert qc() is 0

            before = qb()

            if before is not 0:
                wb0()

                if type(before) is List:
                    before = conjure_mixed_suite(before)

                if v.is_statement_header:
                    return v.conjure_prefixed_fragment(before, v, parse_suite(v.indentation))

                return v.conjure_prefixed_fragment(before, v.a, v.b)

            if v.is_statement_header:
                return v.conjure_fragment(parse_suite(v.indentation))

            return v


        def parse_any_except_or_finally_fragment(indentation):
            v = qv()

            if v is not 0:
                if (not v.is_any_except_or_finally) or (v.indentation is not indentation):
                    return 0

                wv0()
            else:
                v = next_line()

                if v.is_comment__or__empty_line:
                    w_split_2()

                    v = parse_blank_lines(v)

                    w_split_1()

                if (not v.is_any_except_or_finally) or (v.indentation is not indentation):
                    wv(v)
                    return 0

            assert qc() is 0

            before = qb()

            if before is not 0:
                wb0()

                if type(before) is List:
                    before = conjure_mixed_suite(before)

                if v.is_statement_header:
                    return v.conjure_prefixed_fragment(before, v, parse_suite(v.indentation))

                return v.conjure_prefixed_fragment(before, v.a, v.b)

            if v.is_statement_header:
                return v.conjure_fragment(parse_suite(v.indentation))

            return v


        def parse_class_header(header):
            comment = qc()

            if comment is not 0:
                wc0()

                return conjure_prefixed_class_definition(comment, header, parse_suite(header.indentation))

            return conjure_class_definition(header, parse_suite(header.indentation))


        def parse_decorator_header(header):
            prefix = qc()

            if prefix is not 0:
                wc0()

            v = qv()

            if v is 0:
                v = next_line()

                if v.is_comment__or__empty_line:
                    w_split_2()

                    v = parse_blank_lines(v)

                    w_split_1()

                    before = qb()

                    if before is not 0:
                        wb0()

                        wc(conjure_mixed_suite(before)   if type(before) is List else   before)
            else:
                assert qb() is 0

                wv0()

            if not v.is_class_decorator_or_function_header:
                raise_runtime_error('decorator_header must be followed by class, decorator, or function header: %r',
                                    decorator_header)

            if header.indentation is not v.indentation:
                raise_runtime_error('decorator_header (with indentation %d) followed by'
                                        + ' class, decorator, or function header with different indentation: %d',
                                    header.indentation.total,
                                    v.indentation.total)

            if prefix is 0:
                return conjure_decorated_definition(header, v.parse_header())

            return conjure_prefixed_decorated_definition(prefix, header, v.parse_header())


        def produce_parse_header__with_optional_else(name, conjure_statement, conjure_prefixed_statement):
            @rename(name)
            def parse_header__with_optional_else(v):
                indentation = v.indentation

                comment = qc()

                if comment is not 0:
                    wc0()

                    v = conjure_prefixed_statement(comment, v, parse_suite(indentation))
                else:
                    v = conjure_statement(v, parse_suite(indentation))

                w = qv()

                if w is not 0:
                    if (not w.is_else_header_or_fragment) or (indentation is not w.indentation):
                        return v

                    wv0()
                else:
                    w = next_line()

                    if w.is_comment__or__empty_line:
                        w_split_2()

                        w = parse_blank_lines(w)

                        w_split_1()

                    if (not w.is_else_header_or_fragment) or (indentation is not w.indentation):
                        wv(w)
                        return v

                before = qb()

                if before is not 0:
                    wb0()

                    if type(before) is List:
                        before = conjure_mixed_suite(before)

                    if w.is_statement_header:
                        w = conjure_prefixed_else_fragment(before, w, parse_suite(indentation))
                    else:
                        w = conjure_prefixed_else_fragment(before, w.a, w.b)
                else:
                    if w.is_statement_header:
                        w = conjure_else_fragment(w, parse_suite(indentation))

                return conjure_dual_statement(v, w)


            return parse_header__with_optional_else


        def parse_function_header(header):
            comment = qc()

            if comment is not 0:
                wc0()

                return conjure_prefixed_function_definition(comment, header, parse_suite(header.indentation))

            return conjure_function_definition(header, parse_suite(header.indentation))


        def parse_if_header(v):
            comment = qc()

            if comment is not 0:
                wc0()

                v = conjure_prefixed_if_definition(comment, header, parse_suite(v.indentation))
            else:
                v = conjure_if_statement(v, parse_suite(v.indentation))

            return parse_if_statement__X(v)


        def parse_if_statement__X(v):
            indentation = v.indentation

            w = parse_any_else_fragment(indentation)

            if w is 0:
                return v

            if w.is_else_fragment:
                return conjure_dual_statement(v, w)

            x = parse_any_else_fragment(indentation)

            if x is 0:
                return conjure_dual_statement(v, w)

            if x.is_else_fragment:
                return conjure_triple_statement(v, w, x)

            y = parse_any_else_fragment(indentation)

            if y is 0:
                return conjure_triple_statement(v, w, x)

            if y.is_else_fragment:
                return conjure_quadruple_statement(v, w, x, y)

            z = parse_any_else_fragment(indentation)

            if z is 0:
                return conjure_quadruple_statement(v, w, x, y)

            many = [v, w, x, y, z]

            #
            #   Don't need many_append yet
            #
            if z.is_else_fragment:
                return conjure_if_statement_many(many)

            v = parse_any_else_fragment(indentation)

            if v is 0:
                return conjure_if_statement_many(many)

            #
            #   Loop ...
            #
            many_append = many.append

            while 7 is 7:
                many_append(v)

                if v.is_else_fragment:
                    return conjure_if_statement_many(many)

                v = parse_any_else_fragment(indentation)

                if v is 0:
                    return conjure_if_statement_many(many)


        def parse_if_statement(v):
            assert qb() is qv() is 0

            comment = qc()

            if comment is not 0:
                wc0()

                v = conjure_prefixed_if_definition(comment, v.a, v.b)

            return parse_if_statement__X(v)


        def parse_try_header(v):
            comment = qc()

            if comment is not 0:
                wc0()

                v = conjure_prefixed_try_statement(comment, v, parse_suite(v.indentation))
            else:
                v = conjure_try_statement(v, parse_suite(v.indentation))

            return parse_try_statement__X(v)


        def parse_try_statement__X(v):
            indentation = v.indentation

            w = parse_any_except_or_finally_fragment(indentation)

            if w is 0:
                return v

            if w.is_finally_fragment:
                return conjure_dual_statement(v, w)

            x = parse_any_except_or_finally_fragment(indentation)

            if x is 0:
                return conjure_dual_statement(v, w)

            if x.is_finally_fragment:
                return conjure_triple_statement(v, w, x)

            y = parse_any_except_or_finally_fragment(indentation)

            if y is 0:
                return conjure_triple_statement(v, w, x)

            if y.is_finally_fragment:
                return conjure_quadruple_statement(v, w, x, y)

            z = parse_any_except_or_finally_fragment(indentation)

            if z is 0:
                return conjure_quadruple_statement(v, w, x, y)

            many = [v, w, x, y, z]

            #
            #   Don't need many_append yet
            #
            if z.is_finally_fragment:
                return conjure_try_statement_many(many)

            v = parse_any_except_or_finally_fragment(indentation)

            if v is 0:
                return conjure_try_statement_many(many)

            #
            #   Loop ...
            #
            many_append = many.append

            while 7 is 7:
                many_append(v)

                if v.is_finally_fragment:
                    return conjure_try_statement_many(many)

                v = parse_any_except_or_finally_fragment(indentation)

                if v is 0:
                    return conjure_try_statement_many(many)


        def parse_try_statement(v):
            assert qb() is qv() is 0

            comment = qc()

            if comment is not 0:
                wc0()

                v = conjure_prefixed_try_definition(comment, v.a, v.b)

            return parse_try_statement__X(v)


        def parse_with_header(header):
            comment = qc()

            if comment is not 0:
                wc0()

                return conjure_prefixed_with_statement(comment, header, parse_suite(header.indentation))

            return conjure_with_statement(header, parse_suite(header.indentation))


        def parse_lines():
            while 7 is 7:
                v = qv()

                if v is 0:
                    v = next_line()

                    if v.is_comment__or__empty_line:
                        v = parse_blank_lines(v)

                        before = qb()

                        if before is not 0:
                            wb0()
                            append_twig(conjure_mixed_suite(before)   if type(before) is List else   before)
                else:
                    wv0()

                    assert not v.is_comment__or__empty_line

                    before = qb()

                    if before is not 0:
                        wb0()
                        append_twig(conjure_mixed_suite(before)   if type(before) is List else   before)

                if (not v.is_end_of_data__or__unknown_line) and (v.indentation.total != 0):
                    raise_runtime_error('unexpected indentation %d (expected 0): %r', v.indentation.total, v)

                if v.is_statement_header:
                    v = v.parse_header()
                else:
                    assert qc() is 0

                    if v.is_end_of_data:
                        wv(v)
                        break

                append_twig(v)
            else:
                raise_runtime_error('programming error: loop to parse lines did not exit on %r', end_of_data)

            assert qb() is qc() is 0

            while 7 is 7:
                v = qv()

                if v is 0:
                    v = next_line()
                else:
                    wv0()

                if v.is_end_of_data:
                    break

                append_twig(v)
            else:
                raise_runtime_error('programming error: SECOND loop to parse lines did not exit on %r', end_of_data)


        def parse_suite(previous_indentation):
            assert qb() is 0
            assert qc() is 0
            assert qv() is 0

            v = next_line()

            if v.is_comment__or__empty_line:
                v = parse_blank_lines(v)

                before = qb()

                if before is not 0:
                    wb0()
            else:
                before = 0

            if v.is_end_of_data__or__unknown_line:
                raise_unknown_line()

            indentation = v.indentation

            if indentation.total <= previous_indentation.total:
                raise_runtime_error('missing indentation: %d (expected indentation greater than %d)',
                                    indentation.total, previous_indentation.total)

            if v.is_statement_header:
                v = v.parse_header()
            else:
                assert qc() is 0

            #
            #  Now look for 2nd part of suite
            #
            if before is not 0:
                suite_many = [(conjure_mixed_suite(before)   if type(before) is List else   before), v]
            else:
                w = qv()

                if w is not 0:
                    before = qb()

                    if indentation is not w.indentation:
                        if before is not 0:
                            comment = split_comment(indentation)

                            if comment is not 0:
                                return conjure_statement_suite( ((v, comment)) )

                        return v

                    wv0()

                    if before is not 0:
                        wb0()

                        if w.is_statement_header:
                            suite_many = [
                                             v,
                                             (conjure_mixed_suite(before)   if type(before) is List else   before),
                                             w.parse_header(),
                                         ]
                        else:
                            assert qc() is 0

                            suite_many = [
                                             v,
                                             (conjure_mixed_suite(before)   if type(before) is List else   before),
                                             w,
                                         ]
                    else:
                        if w.is_statement_header:
                            suite_many = [v, w.parse_header()]
                        else:
                            assert qc() is 0

                            suite_many = [v, w]
                else:
                    assert qb() is qc() is 0

                    w = next_line()

                    if w.is_comment__or__empty_line:
                        w = parse_blank_lines(w)

                        before = qb()

                        if indentation is not w.indentation:
                            wv(w)

                            if before is not 0:
                                comment = split_comment(indentation)

                                if comment is not 0:
                                    return conjure_statement_suite( ((v, comment)) )

                            return v

                        if before is not 0:
                            wb0()

                            if w.is_statement_header:
                                suite_many = [
                                                 v,
                                                 (conjure_mixed_suite(before)   if type(before) is List else   before),
                                                 w.parse_header(),
                                             ]
                            else:
                                assert qc() is 0

                                suite_many = [
                                                 v,
                                                 (conjure_mixed_suite(before)   if type(before) is List else   before),
                                                 w,
                                             ]
                        else:
                            if w.is_statement_header:
                                suite_many = [v, w.parse_header()]
                            else:
                                assert qc() is 0

                                suite_many = [v, w]
                    else:
                        if indentation is not w.indentation:
                            wv(w)

                            return v

                        if w.is_statement_header:
                            suite_many = [v, w.parse_header()]
                        else:
                            assert qc() is 0

                            suite_many = [v, w]

            #
            #   Handle 3rd part of suite -- set suite_append only if needed
            #
            x = qv()

            if x is not 0:
                before = qb()

                if indentation is not x.indentation:
                    if before is not 0:
                        comment = split_comment(indentation)

                        if comment is not 0:
                            suite_many.append(comment)

                    return conjure_statement_suite(suite_many)

                wv0()
                suite_append = suite_many.append

                if before is not 0:
                    wb0()
                    suite_append(conjure_mixed_suite(before)   if type(before) is List else   before)

                if x.is_statement_header:
                    suite_append(x.parse_header())
                else:
                    assert qc() is 0

                    suite_append(x)
            else:
                assert qb() is qc() is 0

                x = next_line()

                if x.is_comment__or__empty_line:
                    x = parse_blank_lines(x)

                    before = qb()

                    if indentation is not x.indentation:
                        wv(x)

                        if before is not 0:
                            comment = split_comment(indentation)

                            if comment is not 0:
                                suite_many.append(comment)

                        return conjure_statement_suite(suite_many)

                    suite_append = suite_many.append

                    if before is not 0:
                        wb0()
                        suite_append(conjure_mixed_suite(before)   if type(before) is List else   before)
                else:
                    if indentation is not x.indentation:
                        wv(x)

                        return conjure_statement_suite(suite_many)

                    suite_append = suite_many.append

                if x.is_statement_header:
                    suite_append(x.parse_header())
                else:
                    assert qc() is 0

                    suite_append(x)

            #
            #   Handle 4th+ part of suite -- use suite_append
            #
            while 7 is 7:
                x = qv()

                if x is not 0:
                    before = qb()

                    if indentation is not x.indentation:
                        if before is not 0:
                            comment = split_comment(indentation)

                            if comment is not 0:
                                suite_append(comment)

                        return conjure_statement_suite(suite_many)

                    wv0()

                    if before is not 0:
                        wb0()
                        suite_append(conjure_mixed_suite(before)   if type(before) is List else   before)

                    if x.is_statement_header:
                        suite_append(x.parse_header())
                    else:
                        assert qc() is 0

                        suite_append(x)
                else:
                    assert qb() is qc() is 0

                    x = next_line()

                    if x.is_comment__or__empty_line:
                        x = parse_blank_lines(x)

                        before = qb()

                        if indentation is not x.indentation:
                            wv(x)

                            if before is not 0:
                                comment = split_comment(indentation)

                                if comment is not 0:
                                    suite_append(comment)

                            return conjure_statement_suite(suite_many)

                        if before is not 0:
                            wb0()
                            suite_append(conjure_mixed_suite(before)   if type(before) is List else   before)
                    else:
                        if indentation is not x.indentation:
                            wv(x)

                            return conjure_statement_suite(suite_many)

                    if x.is_statement_header:
                        suite_append(x.parse_header())
                    else:
                        assert qc() is 0

                        suite_append(x)


        def split_comment(indentation):
            before = qb()

            assert before is not 0

            if type(before) is List:
                total_m1 = length(before) - 1

                assert total_m1 >= 1

                if indentation is before[total_m1].impression:
                    wb0()
                    return conjure_mixed_suite(before)

                j = total_m1

                while 7 is 7:
                    i = j - 1

                    v = before[i]

                    if indentation is not v.impression:
                        if j is 0:
                            wb(before)
                            return 0

                        j = i
                        continue

                    wb(before[j]   if j is total_m1 else   before[j : ])

                    if j is 1:
                        return v

                    return conjure_mixed_suite(before[ : j])

            if indentation is before.impression:
                wb0()
                return before

            wb(before)
            return 0


        ClassHeader    .parse_header = parse_class_header
        DecoratorHeader.parse_header = parse_decorator_header

        ForHeader.parse_header = produce_parse_header__with_optional_else(
                                     'parse_for_header',
                                     conjure_for_statement,
                                     conjure_prefixed_for_statement,
                                 )

        FunctionHeader               .parse_header = parse_function_header
        IfHeader                     .parse_header = parse_if_header
        IfStatement                  .parse_header = parse_if_statement

        WhileHeader.parse_header = produce_parse_header__with_optional_else(
                                       'parse_for_header',
                                       conjure_for_statement,
                                       conjure_prefixed_for_statement,
                                   )

        WithHeader_1                 .parse_header = parse_with_header
        WithHeader_2                 .parse_header = parse_with_header
        Indented_Try_Colon_LineMarker.parse_header = parse_try_header

        static_conjure_prefixed_else_fragment    = static_method(conjure_prefixed_else_fragment)
        static_conjure_prefixed_else_if_fragment = static_method(conjure_prefixed_else_if_fragment)
        static_conjure_prefixed_except_fragment  = static_method(conjure_prefixed_except_fragment)
        static_conjure_prefixed_finally_fragment = static_method(conjure_prefixed_finally_fragment)

        ElseFragment                     .conjure_fragment = conjure_else_fragment
        ElseIfFragment                   .conjure_fragment = conjure_else_if_fragment
        ElseIfHeader                     .conjure_fragment = conjure_else_if_fragment
        ExceptHeader_1                   .conjure_fragment = conjure_except_fragment
        ExceptHeader_2                   .conjure_fragment = conjure_except_fragment
        Indented_Else_Colon_LineMarker   .conjure_fragment = conjure_else_fragment
        Indented_Except_Colon_LineMarker .conjure_fragment = conjure_except_fragment
        Indented_Finally_Colon_LineMarker.conjure_fragment = conjure_finally_fragment

        ElseFragment                     .conjure_prefixed_fragment = static_conjure_prefixed_else_fragment
        ElseIfFragment                   .conjure_prefixed_fragment = static_conjure_prefixed_else_if_fragment
        ElseIfHeader                     .conjure_prefixed_fragment = static_conjure_prefixed_else_if_fragment
        ExceptHeader_1                   .conjure_prefixed_fragment = static_conjure_prefixed_except_fragment
        ExceptHeader_2                   .conjure_prefixed_fragment = static_conjure_prefixed_except_fragment
        Indented_Else_Colon_LineMarker   .conjure_prefixed_fragment = static_conjure_prefixed_else_fragment
        Indented_Except_Colon_LineMarker .conjure_prefixed_fragment = static_conjure_prefixed_except_fragment
        Indented_Finally_Colon_LineMarker.conjure_prefixed_fragment = static_conjure_prefixed_finally_fragment


        parse_lines()

        return tree_many
