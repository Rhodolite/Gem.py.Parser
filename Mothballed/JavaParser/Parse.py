#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('JavaParser.Parse')
def gem():
    require_gem('JavaParser.Core')
    require_gem('JavaParser.Parse1')


    @share
    def parse_java(path, show = 0, test = 0):
        #line("parse_java(path<%s>, show<%d>, test<%d>)", path, show, test);

        [data, data_lines, data_many] = parse_java_from_path(path)
