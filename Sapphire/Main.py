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
    module_path.insert(1, path_absolute(path_join(path_0, '../../Gem')))
    module_path.insert(2, path_absolute(path_join(path_0, '../../Tremolite')))


    import Gem


@gem('Sapphire.Main')
def gem():
    require_gem('Sapphire.Core')


    choice = 3
    show   = 0


    def command_combine(
            module_name        = 'hma',
            remove_comments    = false,
            remove_indentation = false,
    ):
        require_gem('Sapphire.Transform')

        vary = create_sapphire_transform(
                   remove_comments    = remove_comments,
                   remove_indentation = remove_indentation,
               )

        if fast_cache is 0:
            require_gem('Sapphire.Pattern')

            create_sapphire_match()

        require_gem('Sapphire.Combine')

        command_combine__X(module_name, vary)

        if fast_cache is not 0:
            for s in sorted_list(fast_cache):
                line('Unused: %s', s)


    def command_development():
        require_gem('Sapphire.Development')

        development()


    def command_parse1(
            remove_comments    = false,
            remove_indentation = false,
            show               = 0,
    ):
        require_gem('Sapphire.Pattern')

        create_sapphire_match()

        require_gem('Sapphire.Transform')
        require_gem('Sapphire.Parse')                       #   Must be after 'create_sapphire_match'

        vary = create_sapphire_transform(
                   remove_comments    = remove_comments,
                   remove_indentation = remove_indentation,
               )

        parse_python('test.py', vary = vary, test = 7, show = show)

        #for name in ['arguments-2', 'list-expression-2', 'range-index', 'tuple-expression-2']:
        #    print_cache(name)

        #print_cache()


    def test_parse2():
        require_gem('Sapphire.Parse2')                      #   Must be after 'create_sapphire_match'

        parse2_python_from_path('test2.py')


    @share
    def main(arguments):
        try:
            total = length(arguments)

            if total is 0:
                return command_parse1(show = show)

            if total is not 1:
                raise_runtime_error('must have zero or one argument')

            option = arguments[0]

            if option == 'combine':
                return command_combine(
                           module_name        = 'hma',
                           remove_comments    = true,
                           remove_indentation = true,
                       )

            if option == 'combine2':
                return command_combine(module_name = 'hma2')

            if option == 'dev':
                if choice is 1:
                    return command_development()

                if choice is 2:
                    return command_parse1(
                               #remove_comments    = true,
                               #remove_indentation = true,
                               show               = show,
                           )

                if choice is 3:
                    return command_combine(
                               module_name        = 'hma',
                               remove_comments    = true,
                               remove_indentation = true,
                           )

                raise_runtime_error('unknown choice: %d', choice)

            if option == 'parse':
                return command_parse1(show = 7)

            raise_runtime_error('unknown option: %r', option)
        except:
            with except_any_clause() as e:
                print_exception_chain(e)
                program_exit(1)
