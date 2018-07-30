#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Path')
def module():
    path_0 = module_path[0]

    if path_0.endswith('/Gems'):
        root_path   = path_0
        source_path = path_join(root_path, 'py')
    else:
        source_path = path_normalize(path_join(path_0,      '..'))
        root_path   = path_normalize(path_join(source_path, '..'))

    binary_path = path_join(root_path, 'bin')

    if false:
        line('root_path: %s', root_path)
        line('binary_path: %s', binary_path)
        line('source_path: %s', source_path)


    share(
        'binary_path',          binary_path,
        'source_path',          source_path,
    )
