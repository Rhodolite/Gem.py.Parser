#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CoreParser.Core')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Cache')
    require_gem('Gem.Cache2')
    require_gem('Gem.Cadence')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Global')
    require_gem('Gem.Method')
    require_gem('Gem.Path')
    require_gem('Gem.SimpleStringIO')
    require_gem('Gem.StringOutput')
    require_gem('Gem.System')


    from Gem import cadence_constructing, cadence_entered, cadence_exception, cadence_exited, cadence_initialized
    from Gem import cadence_reuse, caller_frame_1, create_cache, create_DelayedFileOutput, create_SimpleStringOutput
    from Gem import create_StringOutput, Exception, gem_global
    from Gem import path_basename, produce_cache_functions, produce_conjure_by_name, produce_conjure_dual
    from Gem import produce_conjure_dual__21
    from Gem import return_self, slice_all, StringOutput


    share(
        #
        #   Exception
        #
        'Exception',                    Exception,


        #
        #   Types
        #
        'StringOutput',     StringOutput,


        #
        #   Functions
        #
        'caller_frame_1',               caller_frame_1,
        'create_cache',                 create_cache,
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_SimpleStringOutput',    create_SimpleStringOutput,
        'create_StringOutput',          create_StringOutput,
        'path_basename',                path_basename,
        'produce_cache_functions',      produce_cache_functions,
        'produce_conjure_by_name',      produce_conjure_by_name,
        'produce_conjure_dual',         produce_conjure_dual,
        'produce_conjure_dual__21',     produce_conjure_dual__21,
        'return_self',                  return_self,


        #
        #   Values
        #
        'cadence_constructing',         cadence_constructing,
        'cadence_entered',              cadence_entered,
        'cadence_exception',            cadence_exception,
        'cadence_exited',               cadence_exited,
        'cadence_initialized',          cadence_initialized,
        'cadence_reuse',                cadence_reuse,
        'gem_global',                   gem_global,
        'slice_all',                    slice_all,
    )
