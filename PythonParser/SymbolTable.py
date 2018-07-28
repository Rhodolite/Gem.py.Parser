#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.SymbolTable')
def module():
    require_module('PythonParser.BuildSymbolTable')


    dump = 0


    class GlobalSymbolTable(Object):
        __slots__ = ((
            'nested_headers',               #   Tuple of { Integer, ClassHeader | FunctionHeader ... }
            'global_variables',             #   List of GlobalVariable
        ))


        def __init__(t, nested_headers, global_variables):
            t.nested_headers   = nested_headers
            t.global_variables = global_variables


        def dump_global_symbol_table(t, f):
            f.blank()
            f.line('Nested Headers:')
            f.blank()

            if length(t.nested_headers) is 0:
                f.line('   none')
            else:
                iterator = iterate(t.nested_headers)
                next     = next_method(iterator)

                for nesting in iterator:
                    v = next()

                    f.partial(' ' * (4 + 4 * nesting) + v.display_type + ' ' + v.name.s)

                    if f.position:
                        f.line()

            f.blank()
            f.line('Global Variables:')
            f.blank()

            if length(t.global_variables) is 0:
                f.line('   none')
            else:
                for v in t.global_variables:
                    f.line('    %r', v)

            f.blank()


    def create_global_symbol_table(build_symbol_table):
        nested_header_many   = []
        append_nested_header = nested_header_many.append

        global_variable_many   = []
        append_global_variable = global_variable_many.append


        def add_nested_headers(nesting, build_symbol_table):
            definition_many = build_symbol_table.definition_many

            if definition_many is 0:
                return

            definition_map = build_symbol_table.definition_map

            if type(definition_many) is not List:
                append_nested_header(nesting)
                append_nested_header(definition_many.a)

                add_nested_headers(nesting + 1, definition_map)
            else:
                find_build_symbol_table = definition_map.__getitem__

                for v in definition_many:
                    append_nested_header(nesting)
                    append_nested_header(v.a)

                    add_nested_headers(nesting + 1, find_build_symbol_table(v))


        add_nested_headers(0, build_symbol_table)

        variable_map = build_symbol_table.variable_map

        if variable_map is not 0:
            for v in iterate_values_sorted_by_key(variable_map, key = Identifier.s.__get__):
                append_global_variable(v)

        return GlobalSymbolTable(Tuple(nested_header_many), Tuple(global_variable_many))


    @share
    def build_global_symbol_table(tree, vary = 0):
        art = create_build_global_symbol_table()

        for s in ['__builtins__', '__doc__', '__file__', '__name__', '__package__']:
            art.write_variable(conjure_name(s))

        if type(tree) is List:
            for v in tree:
                v.scout_variables(art)
        else:
            tree.scout_variables(art)

        art.scout_definitions()

        #first_2 = first.adorn(art)

        if dump is 7:
            art.dump_variables('globals')

        return ((
                   create_global_symbol_table(art),
                   (tree.transform(vary)   if vary else   tree),
               ))



    @share
    def build_function_symbol_table(tree, art):
        pass
