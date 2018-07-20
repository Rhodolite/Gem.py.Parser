#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.MosiacSymbol')
def gem():
    class CodeValue(Object):
        __slots__ = ((
            'header',                   #   FunctionHeader
            'body',                     #   Statement+
            'cell_variables',           #   None | ( CellFunctionParameter | CellLocal )
            'local_variables',          #   None | FunctionLocal | Tuple of { FunctionLocal | FunctionParameter }
                                        #       | Tuple of ( CellFunctionParameter | CellLocal )
            'free_variables',           #   None | FreeVariable | Tuple of FreeVariable
            'global_variables',         #   None | GlobalVariable | Tuple of GlobalVariable
        ))


        def __init__(t, header, body, cell_variables, local_variables, free_variables, global_variables):
            t.header           = header
            t.body             = body
            t.cell_variables   = cell_variables
            t.local_variables  = local_variables
            t.free_variables   = free_variables
            t.global_variables = global_variables
