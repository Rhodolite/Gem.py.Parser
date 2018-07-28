#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
def boot(module_name):
    def execute(f):
        return f()

    return execute


@boot('Boot')
def boot():
    from sys     import path    as module_path
    from os.path import abspath as path_absolute, join as path_join

    path_0 = module_path[0]

    module_path.insert(0, path_absolute(path_join(path_0, '../')))
    module_path.insert(1, path_absolute(path_join(path_0, '../../../Capital')))
    module_path.insert(2, path_absolute(path_join(path_0, '../../../Parser')))
    module_path.insert(3, path_absolute(path_join(path_0, '../../../Tremolite')))


    import Capital


@module('SqlParser.Main')
def module():
    require_module('Capital.Global')


    from Capital import capital_global


    capital_global.sql_parser = true


    require_module('SqlParser.Core')
    require_module('SqlParser.Pattern')


    @share
    def main(arguments):
        create_sql_parser_match()

        require_module('SqlParser.Parse1')                              #   Must be after `create_sql_parser_match`

        parse1_mysql_from_path('test.sql')
