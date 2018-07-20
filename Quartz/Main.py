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

    module_path.insert(0, path_absolute(path_join(path_0, '../../Gem')))
    module_path.insert(1, path_absolute(path_join(path_0, '../')))
    module_path.insert(2, path_absolute(path_join(path_0, '../../Tremolite')))


    import Gem


@gem('Quartz.Main')
def gem():
    require_gem('Quartz.Core')
    require_gem('Quartz.Pattern')


    @share
    def main(arguments):
        create_quartz_match()

        require_gem('Quartz.Parse1')                            #   Must be after 'create_quartz_match'

        parse1_mysql_from_path('test.sql')
