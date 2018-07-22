#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CoreParser.Core')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Cache')
    require_gem('Gem.Cache2')
    require_gem('Gem.Cadence')
    require_gem('Gem.Exception')
    require_gem('Gem.Global')
    require_gem('Gem.Method')
    require_gem('Gem.Path')
    require_gem('Gem.System')


    from Gem import cadence_constructing, cadence_entered, cadence_exception, cadence_exited, cadence_initialized
    from Gem import cadence_reuse, caller_frame_1, create_cache, Exception, gem_global
    from Gem import path_basename, produce_cache_functions, produce_conjure_by_name, return_self, slice_all


    share(
        #
        #   Exception
        #
        'Exception',                    Exception,

        #
        #   Functions
        #
        'caller_frame_1',               caller_frame_1,
        'create_cache',                 create_cache,
        'path_basename',                path_basename,
        'produce_cache_functions',      produce_cache_functions,
        'produce_conjure_by_name',      produce_conjure_by_name,
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
