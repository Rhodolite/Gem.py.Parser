#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@boot('Boot')
def boot():
    #
    #   This really belongs in Gem.Core, but is here since we need it during Boot
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
    #   Gem_name
    #
    Gem_name = intern_string('Gem')


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
    Gem = create_module('Gem')

    Gem.fast_cache = fast_cache = {}

    store_fast = fast_cache.__setitem__


    def gem(module_name):
        def execute(f):
            store_fast(module_name, f)

            return gem


        return execute


    __import__(__name__).gem = gem


    def boot():
        fast_cache.pop('Gem.Boot')()

        produce_export_and_share = Gem.Shared.produce_export_and_share
        store_gem_module         = Gem.Shared.store_gem_module

        del Gem.Shared.produce_export_and_share, Gem.Shared.store_gem_module

        for module_name in ['Pearl', 'Sapphire', 'Tremolite']:
            module = create_module(module_name)

            produce_export_and_share(module)
            store_gem_module(module_name, module)

        f        = fast_cache.pop('Sapphire.Main')
        gem_main = __import__('__main__').gem('Sapphire.Main')

        gem_main(f)


    return boot
