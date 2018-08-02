#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Parse')
def module():
    require_module('PythonParser.Parse1')
    require_module('PythonParser.Parse3')


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


    @share
    def parse_python(path, vary = 0, show = 0, test = 0):
        #line("parse_python(path<%s>, vary<%d>, show<%d>, test<%d>)", path, vary, show, test);

        [data, data_lines, data_many] = parse_python_from_path(path)

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
