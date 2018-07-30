#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@boot('Boot')
def boot():
    #
    #   This really belongs in Capital.Core, but is here since we need it during Boot
    #
    PythonSystem = __import__('sys')
    PythonTypes  = __import__('types')
    PythonPath   = __import__('os.path').path


    is_python_2     = (PythonSystem.version_info.major is 2)
    is_python_3     = (PythonSystem.version_info.major is 3)


    PythonBuiltIn = __import__('__builtin__'  if is_python_2 else   'builtins')


    #
    #   Python Keywords
    #
    false = False
    none  = None
    true  = True


    #
    #   Python Functions
    #
    intern_string = (PythonBuiltIn   if is_python_2 else   PythonSystem).intern
    module_path   = PythonSystem.path
    path_absolute = PythonPath.abspath
    path_join     = PythonPath.join


    #
    #   Python Types
    #
    ModuleType = type(PythonSystem)


    #
    #   python_modules (also lookup_python_module & store_python_module)
    #
    python_modules       = PythonSystem.modules
    store_python_module  = python_modules.__setitem__


    #
    #   Capital_name
    #
    Capital_name = intern_string('Capital')


    #
    #   Calculate & store root path
    #
    root_path = intern_string(path_absolute(path_join(module_path[0], '../..')))

    module_path[0] = root_path


    #
    #   Create initial modules
    #
    def create_module(module_name):
        module_name = intern_string(module_name)
        module_path = intern_string(path_join(root_path, module_name))

        module = ModuleType(module_name)

        module.__file__ = intern_string(path_join(module_path, '__init__.py'))
        module.__path__ = [module_path]

        assert module_name not in python_modules

        store_python_module(module_name, module)

        return module


    #
    #   Set flag to indicate using fast loading mode
    #
    Capital = create_module('Capital')

    Capital.fast_cache = fast_cache = {}

    store_fast = fast_cache.__setitem__


    def module(module_name):
        def execute(f):
            store_fast(module_name, f)

            return module


        return execute


    __import__(__name__).module = module


    def boot():
        fast_cache.pop('Capital.Boot')()

        produce_export_transport_and_share = Capital.Shared.produce_export_transport_and_share
        store_capital_module               = Capital.Shared.store_capital_module

        del Capital.Shared.produce_export_transport_and_share, Capital.Shared.store_capital_module

        for module_name in ['CoreParser', 'PythonParser', 'Rex', 'Restructure']:
            module = create_module(module_name)

            produce_export_transport_and_share(module)
            store_capital_module(module_name, module)

        f           = fast_cache.pop('PythonParser.Main')
        module_main = __import__('__main__').module('PythonParser.Main')

        module_main(f)


    return boot
