#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.TestTree')
def module():
    if capital_global.CRYSTAL_parser:
        @export
        def test_count_newlines(data_lines, tree_many):
            total = 0

            for v in tree_many:
                total += v.count_newlines()

            if total != length(data_lines):
                raise_runtime_error('mismatch on counted lines (counted: %d; expected: %d)',
                                    total, length(parse_context.data_lines))

            line('Passed#2: Total counted lines %d matches input', total)


    if capital_global.CRYSTAL_parser:
        @export
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
