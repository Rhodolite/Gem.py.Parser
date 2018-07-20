#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.Development')
def gem():
    adorn = 7
    dump  = 0
    show  = 7


    require_gem('Sapphire.Cache')
    require_gem('Sapphire.SymbolTable')


    @share
    def development():
        path = 'test.py'

        require_gem('Sapphire.Pattern')

        create_sapphire_match()

        require_gem('Sapphire.Parse')                       #   Must be after 'create_sapphire_match'

        tree = parse_python(path, test = 7, show = 0)

        if show is 7:
            for v in tree:
                dump_token('v', v)

        if adorn is 7:
            [art, tree] = build_global_symbol_table(tree)

            f = create_TokenOutput()
            art.dump_global_symbol_table(f)

            partial(f.finish())


        if dump is 7:
            dump_caches__OLD('cell_function_parameter')
            dump_caches__OLD('cell_local')
            dump_caches__OLD('function_parameter')
            dump_caches__OLD('free_variable')
            dump_caches__OLD('local_variable')
            dump_caches__OLD('global_variable')
