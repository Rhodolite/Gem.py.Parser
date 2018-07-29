#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Variable')
def module():
    require_module('PythonParser.Cache')


    cell_function_parameter_cache = create_cache('cell-function-parameter')
    cell_local_cache              = {}
    free_variable_cache           = {}
    function_parameter_cache      = {}
    global_variable_cache         = {}
    local_variable_cache          = {}


    def construct__index_name(t, index, name):
        t.index = index
        t.name  = name


    def construct__index_name__cell_index(t, index, name, cell_index):
        t.index      = index
        t.name       = name
        t.cell_index = cell_index


    def portray__index_name(t):
        return arrange('<%s#%d %s>', t.display_name, t.index, t.name.s)


    def portray__index_name__cell_index(t):
        return arrange('<%s#%d %s; cell#%d>', t.display_name, t.index, t.name.s, t.cell_index)


    class CellFunctionParameter(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   TokenName
            'cell_index',               #   Integer
        ))


        display_name       = 'cell-parameter'
        herd_estimate      = 0
        is_cell_variable   = true
        is_herd            = false
        is_global_variable = false


        __init__      = construct__index_name__cell_index
        __repr__      = portray__index_name__cell_index
        display_token = portray__index_name__cell_index


    CellFunctionParameter.k1 = CellFunctionParameter.index
    CellFunctionParameter.k2 = CellFunctionParameter.name
    CellFunctionParameter.k3 = CellFunctionParameter.cell_index


    class CellLocal(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   TokenName
            'cell_index',               #   Integer
        ))


        display_name       = 'cell-local'
        is_cell_variable   = true
        is_global_variable = false


        __init__      = construct__index_name__cell_index
        __repr__      = portray__index_name__cell_index
        display_token = portray__index_name__cell_index


    CellLocal.k1  = CellLocal.index
    CellLocal.k2  = CellLocal.name
    #CellLocal.k3 = CellLocal.cell_index


    class FreeVariable(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   TokenName
        ))


        display_name       = 'free-variable'
        is_cell_variable   = true
        is_global_variable = false


        __init__      = construct__index_name


        def __repr__(t):
            return arrange('<%s#%d %s; cell #...>', t.display_name, t.index, t.name.s)


        display_token = __repr__


    FreeVariable.k1 = FreeVariable.index
    #FreeVariable.k2 = FreeVariable.name


    @share
    class FunctionParameter(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   TokenName
        ))


        display_name       = 'parameter'
        is_cell_variable   = false
        is_global_variable = false


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    FunctionParameter.k1 = FunctionParameter.index
    #FunctionParameter.k2 = FunctionParameter.name


    class GlobalVariable(Object):
        __slots__ = ((
            'name',                     #   TokenName
        ))


        is_global_variable = true


        def __init__(t, name):
            t.name = name


        def __repr__(t):
            return arrange('<global %s>', t.name.s)


        display_token = __repr__


    @share
    class LocalVariable(Object):
        __slots__ = ((
            'index',                    #   Integer
            'name',                     #   TokenName
        ))


        display_name       = 'local'
        is_cell_variable   = false
        is_global_variable = false


        __init__      = construct__index_name
        __repr__      = portray__index_name
        display_token = portray__index_name


    LocalVariable.k1 = LocalVariable.index
    #LocalVariable.k2 = LocalVariable.name


    conjure_cell_function_parameter__X__unique = produce_conjure_unique_triple__312(
                                                     'cell_function_parameter',
                                                     CellFunctionParameter,
                                                     cell_function_parameter_cache,
                                                 )


    def conjure_cell_function_parameter(index, name, cell_index):
        #my_line('%s %s %s', index, name, cell_index)
        return conjure_cell_function_parameter__X__unique(
                    intern_integer(index),
                    name,
                    intern_integer(cell_index),
               )


    conjure_cell_local = produce_conjure_triple__312('cell_local', CellLocal, cell_local_cache)

    conjure_free_variable = produce_conjure_dual__21('free_variable', FreeVariable, free_variable_cache)

    conjure_function_parameter = produce_conjure_dual__21(
                                     'function_parameter',
                                     FunctionParameter,
                                     function_parameter_cache,
                                 )

    conjure_global_variable__X = produce_conjure_single  ('global_variable', GlobalVariable, global_variable_cache)
    conjure_local_variable     = produce_conjure_dual__21('local_variable',  LocalVariable,  local_variable_cache)


    def conjure_global_variable(name):
        #my_line('%s', name)
        return conjure_global_variable__X(name)


    append_cache('cell_function_parameter', cell_function_parameter_cache)
    append_cache('cell_local',              cell_local_cache)
    append_cache('free_variable',           free_variable_cache)
    append_cache('function_parameter',      function_parameter_cache)
    append_cache('global_variable',         global_variable_cache)
    append_cache('local_variable',          local_variable_cache)


    share(
        'conjure_cell_function_parameter',  conjure_cell_function_parameter,
        'conjure_cell_local',               conjure_cell_local,
        'conjure_free_variable',            conjure_free_variable,
        'conjure_function_parameter',       conjure_function_parameter,
        'conjure_global_variable',          conjure_global_variable,
        'conjure_local_variable',           conjure_local_variable,
    )
