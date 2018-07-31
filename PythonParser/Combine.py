#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Combine')
def module():
    require_module('PythonParser.Parse')
    require_module('PythonParser.Path')
    require_module('PythonParser.SymbolTable')


    variables = [
                    0,                  #   0 = copyright
                ]

    query = variables.__getitem__
    write = variables.__setitem__

    qc = Method(query, 0)
    wc = Method(write, 0)

    wc0 = Method(wc, 0)


    #
    #   Tokens
    #
    empty_indentation__function = conjure_indented_token(empty_indentation, FUNCTION__W)

    #def module_function():
    module_function__function_header = conjure_function_header(
            empty_indentation__function,
            conjure_name('module'),
            conjure_parameters_0(LP, RP),
            COLON__LINE_MARKER,
        )


    class Copyright(Object):
        __slots__ = ((
            'year',                     #   String+
            'author',                   #   String+
        ))


        def __init__(t, year, author):
            t.year   = year
            t.author = author


        def write(t, f):
            copyright = qc()

            if t is not copyright:
                if copyright is not 0:
                    close_copyright(f)

                wc(t)

                f.blank2()
                f.line('#<Copyright (c) %s %s.  All rights reserved.>', t.year, t.author)
                f.blank_suppress()


    Copyright.k1 = Copyright.year
    Copyright.k2 = Copyright.author


    copyright_cache = {}

    conjure_copyright__X__dual = produce_conjure_dual('copyright', Copyright, copyright_cache)


    def conjure_copyright(year, author):
        return conjure_copyright__X__dual(intern_string(year), intern_string(author))


    def close_copyright(f):
        if qc() is not 0:
            wc0()

            f.blank_suppress()
            f.line('#</Copyright>')
            f.blank2()


    class TwigCode(Object):
        __slots__ = ((
            'path',                     #   String+
            'part',                     #   String
            'copyright',                #   Copyright
            'twig',                     #   Any
            'symbol_table',             #   GlobalSymbolTable
            'transformed_twig',         #   Any
        ))


        def __init__(t, path, part, copyright, twig, symbol_table, transformed_twig):
            t.path             = path
            t.part             = part
            t.copyright        = copyright
            t.twig             = twig
            t.symbol_table     = symbol_table
            t.transformed_twig = transformed_twig


        def write(t, f, tree = false):
            t.copyright.write(f)

            f.blank2()
            f.line(arrange("#<source %r %s>", t.path, t.part))

            if tree:
                f2 = create_TokenOutput(f)

                with f2.change_prefix('#', '#   '):
                    f2.line()
                    r = t.twig.dump_token(f2)
                    f2.line()

                    assert not r

                    t.symbol_table.dump_global_symbol_table(f2)

                    f2.flush()

            t.transformed_twig.write(f.write)
            f.line('#</source>')
            f.blank2()


    def create_twig_code(path, part, copyright, twig, vary):
        [art, transformed_twig] = build_global_symbol_table(twig, vary)

        return TwigCode(path, part, copyright, twig, art, transformed_twig)


    class RequireMany(Object):
        __slots__ = ((
            'vary',                     #   PythonParserTransform

            'latest_many',              #   List of String
            '_append_latest',           #   Method

            'twig_many',                #   List of Twig
            '_append_twig',             #   Method

            'processed_set',            #   LiquidSet of String
            '_add_processed',           #   Method
            '_contains_processed',      #   Method
        ))


        def __init__(t, vary):
            t.vary = vary

            t.latest_many    = many        = []
            t._append_latest = many.append

            t.twig_many    = many        = []
            t._append_twig = many.append

            t.processed_set       = processed = LiquidSet()
            t._add_processed      = processed.add
            t._contains_processed = processed.__contains__

            #
            #   Ignore these file, pretend we already saw them
            #
            t._add_processed('Capital.Path2')
            t._add_processed('PythonParser.Boot')
            t._add_processed('PythonParser.Parse2')


        def add_require_module(t, module_argument):
            module_name = module_argument.find_atom()

            assert module_name.is_single_quote

            s = module_name.s[1:-1]

            if t._contains_processed(s):
                return

            t._append_latest(s)


        def loop(t):
            contains_processed = t._contains_processed
            latest_many        = t.latest_many
            process_module     = t.process_module

            append_latest = t._append_latest
            extend_latest = latest_many.extend
            length_latest = latest_many.__len__
            index_latest  = latest_many.__getitem__
            delete_latest = latest_many.__delitem__

            index_latest_0  = Method(index_latest, 0)
            index_latest_1  = Method(index_latest, 1)
            delete_latest_0 = Method(delete_latest, 0)
            zap_latest      = Method(delete_latest, slice_all)

            while 7 is 7:
                total = length_latest()

                if total is 0:
                    break

                first = index_latest_0()

                if contains_processed(first):
                    ##line('Already processed %s', first)
                    delete_latest_0()
                    continue

                line('Total %d - Process %s', total, first)

                if total is 1:
                    zap_latest()
                    process_module(first)
                    continue

                if total is 2:
                    other = index_latest_1()
                    zap_latest()
                    process_module(first)
                    append_latest(other)
                    continue

                other = t.latest_many[1:]
                zap_latest()
                process_module(first)
                extend_latest(other)


        def process_module(t, module):
            t._add_processed(module)

            if module.startswith('CoreParser.'):
                parent = '../Parser'
            elif module.startswith('Capital.'):
                parent = '../Capital'
            elif module.startswith('PythonParser.'):
                parent = '../Parser'
            elif module.startswith('Restructure.'):
                parent = '../Tremolite'
            elif module.startswith('Rex.'):
                parent = '../Tremolite'
            else:
                line('module: %s', module)

            path = path_join(parent, arrange('%s.py', module.replace('.', '/')))

            module_function = extract_module_function(module, path, t.vary)

            t._append_twig(module_function)

            module_function.twig.find_require_module(t)


    def conjure__module_function__decorator_header(module):
        #@module_function('Capital.Something')
        return conjure_decorator_header(
                   empty_indentation__at_sign,
                   conjure_call_expression(
                       conjure_name('module'),
                       conjure_arguments_1(LP, conjure_single_quote(portray(module)), RP),
                   ),
                   LINE_MARKER,
               )

    def extract_boot(path, tree, index, copyright, vary):
        boot_code = tree[index]

        #@boot('Boot')
        boot_code__decorator_header = conjure_decorator_header(
                                          empty_indentation__at_sign,
                                          conjure_call_expression(
                                              conjure_name('boot'),
                                              conjure_arguments_1(LP, conjure_single_quote("'Boot'"), RP),
                                          ),
                                          LINE_MARKER,
                                      )

        assert boot_code.is_decorated_definition
        assert boot_code.a is boot_code__decorator_header

        return create_twig_code(
                   path,
                   arrange('[%d]', index),
                   extract_copyright(tree),
                   boot_code,
                   vary,
               )


    def extract_boot_decorator(function_name, path, tree, copyright, vary = 0):
        boot_decorator = tree[0]

        #def boot(module_name):
        boot_decorator__function_header = conjure_function_header(
                                              empty_indentation__function,
                                              conjure_name(function_name),
                                              conjure_parameters_1(LP, conjure_name('module_name'), RP),
                                              COLON__LINE_MARKER,
                                          )

        assert boot_decorator.is_function_definition
        assert boot_decorator.a is boot_decorator__function_header
        assert boot_decorator.b.is_statement_suite

        return create_twig_code(path, '[0]', copyright, boot_decorator, vary)


    def extract_copyright(tree):
        copyright = tree[0].prefix

        if not copyright.is_comment_suite:
            dump_token('copyright', copyright)

        assert copyright.is_comment_suite
        assert length(copyright) is 3
        assert copyright[0] == empty_comment_line
        assert copyright[1].is_comment_line
        assert copyright[2] == empty_comment_line

        m = copyright_match(copyright[1])

        if m is none:
            raise_runtime_error('failed to extract copyright from: %r', copyright[1])

        return conjure_copyright(m.group('year'), m.group('author'))


    def extract_module_function(module, path, vary):
        tree = parse_python(path)

        assert length(tree) is 1

        copyright = extract_copyright(tree)

        module_function = tree[0]

        #if module_function.a is not conjure__module_function__decorator_header(module):
        #    dump_token('module_function.a', module_function.a)
        #    dump_token('other', conjure__module_function__decorator_header(module))

        assert module_function.is_decorated_definition
        assert module_function.a is conjure__module_function__decorator_header(module)
        assert module_function.b.is_function_definition
        assert module_function.b.a is module_function__function_header

        return create_twig_code(path, '[0]', copyright, module_function, vary)


    def extract__single_python_file_boot(vary):
        path = path_join(source_path, 'Parser/Assets/SinglePythonFileBoot.py')

        tree = parse_python(path)

        assert length(tree) is 1

        return extract_boot(path, tree, 0, extract_copyright(tree), vary)


    def extract_capital_boot(vary):
        module_name = 'Capital.Boot'
        path        = path_join(source_path, 'Capital/Capital/Boot.py')
        #path       = 'b2.py'

        tree = parse_python(path)

        assert length(tree) is 3

        copyright = extract_copyright(tree)

        #
        #    [0]
        #       def boot(module_name):
        #           ...
        #
        boot_decorator = extract_boot_decorator('module', path, tree, copyright)

        del boot_decorator  #   We don't really want this, but just extracted it for testing purposes

        #
        #   [1]: empty lines
        #
        assert tree[1].is_empty_line_suite

        #
        #   [2]:
        #       @module('Capital.Boot')
        #       def module():
        #           ...
        #
        module_function = tree[2]

        assert module_function.is_decorated_definition
        assert module_function.a is conjure__module_function__decorator_header(module_name)
        assert module_function.b.is_function_definition
        assert module_function.b.a is module_function__function_header
        assert module_function.b.b.is_statement_suite

        return create_twig_code(path, '[2]', copyright, module_function, vary)


    def extract_python_parser_main(vary):
        module_name = 'PythonParser.Main'
        path        = path_join(source_path, 'Parser/PythonParser/Main.py')

        tree = parse_python(path)

        assert length(tree) is 5

        copyright = extract_copyright(tree)


        #
        #   [0]:
        #       def boot(module_name):
        #           ...
        #
        boot_decorator = extract_boot_decorator('boot', path, tree, copyright, vary)



        #
        #   [1]: empty lines
        #
        assert tree[1].is_empty_line_suite


        #
        #   [2]:
        #       @boot('Boot')
        #       def boot():
        #           ...
        #
        boot = extract_boot(path, tree, 2, copyright, vary)

        del boot        #   We don't really want this, but just extracted it for testing purposes


        #
        #   [3]
        #
        assert tree[3].is_empty_line_suite


        #
        #   [4]:
        #       @module('PythonParser.Main')
        #       def module():
        #           ...
        #
        main = tree[4]

        assert main.is_decorated_definition
        assert main.a is conjure__module_function__decorator_header(module_name)
        assert main.b.is_function_definition
        assert main.b.a is module_function__function_header
        assert main.b.b.is_statement_suite


        #
        #   Result
        #
        return ((
                   boot_decorator,
                   create_twig_code(path, '[4]', copyright, main, vary),
               ))


    @share
    def command_combine__X(module_name, vary, tree = true):
        [boot_decorator, main_code] = extract_python_parser_main(vary)

        single_python_file_boot__code = extract__single_python_file_boot(vary)
        capital_boot_code             = extract_capital_boot(vary)

        require_many = RequireMany(vary)

        require_many.process_module('Capital.Core')
        main_code.twig.find_require_module(require_many)
        require_many.loop()

        output_path = path_join(binary_path, arrange('.pyxie/%s.py', module_name))

        with create_DelayedFileOutput(output_path) as f:
            boot_decorator               .write(f, tree)
            single_python_file_boot__code.write(f, tree)

            for v in require_many.twig_many:
                v.write(f, tree)

            capital_boot_code.write(f, tree)
            main_code        .write(f, tree)

            close_copyright(f)

        #partial(read_text_from_path(output_path))
        #for name in ['cell-function-parameter']:
        #    print_cache(name)
        #print_cache()
