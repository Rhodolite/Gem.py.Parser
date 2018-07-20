#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.Parse')
def gem():
    require_gem('Sapphire.Parse1')
    require_gem('Sapphire.Parse3')


    def show_indentation(data_many):
        for v in data_many:
            indentation = v.indentation

            if indentation is none:
                line(v.display_token())
                continue

            line('+%d %s', indentation.total, v.display_token())


    def show_tree(tree_many, vary):
        with create_TokenOutput() as f:
            f.line('===  show_tree  ===')

            for v in tree_many:
                if vary is not 0:
                    v = v.transform(vary)

                    if v is 0:
                        continue

                r = v.dump_token(f)

                assert not r

        partial(f.result)


    def test_count_newlines(data_lines, tree_many):
        total = 0

        for v in tree_many:
            total += v.count_newlines()

        if total != length(data_lines):
            raise_runtime_error('mismatch on counted lines (counted: %d; expected: %d)',
                                total, length(parse_context.data_lines))

        line('Passed#2: Total counted lines %d matches input', total)


    def test_identical_output(path, data, data_many, tree_many):
        with create_StringOutput() as f:
            w = f.write

            for v in tree_many:
                v.write(w)

        if data != f.result:
            with create_DelayedFileOutput('oops.txt') as oops:
                oops.write(f.result)

            raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')

        line('Passed#1: Identical dump from parse tree.  Total: %d line%s',
             length(tree_many), (''   if length(data_many) is 0 else   's'))


    @share
    def parse_python(path, vary = 0, show = 0, test = 0):
        #line("parse_python(path<%s>, vary<%d>, show<%d>, test<%d>)", path, vary, show, test);

        [data, data_lines, data_many] = parse1_python_from_path(path)

        if show is 5:
            show_indentation(data_many)

        tree_many = parse3_python(path, data, data_lines, data_many)

        if show is 7:
            show_tree(tree_many, vary)

        if test is 7:
            test_identical_output(path, data, data_many, tree_many)
            test_count_newlines(data_lines, tree_many)

        #dump_newline_meta_cache()
        #dump_caches__OLD('dual-twig')

        return tree_many
