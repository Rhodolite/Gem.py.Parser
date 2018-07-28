#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('CoreParser.Core')
def module():
    require_module('Capital.Absent')
    require_module('Capital.Cache')
    require_module('Capital.Cache2')
    require_module('Capital.Cadence')
    require_module('Capital.DelayedFileOutput')
    require_module('Capital.Exception')
    require_module('Capital.Global')
    require_module('Capital.Method')
    require_module('Capital.Path')
    require_module('Capital.SimpleStringIO')
    require_module('Capital.StringOutput')
    require_module('Capital.System')


    from Capital import cadence_constructing, cadence_entered, cadence_exception, cadence_exited, cadence_initialized
    from Capital import cadence_reuse, caller_frame_1, create_cache, create_DelayedFileOutput
    from Capital import create_SimpleStringOutput, create_StringOutput, Exception, capital_global
    from Capital import path_basename, produce_cache_functions, produce_conjure_by_name, produce_conjure_dual
    from Capital import produce_conjure_dual__21, produce_conjure_triple, produce_conjure_unique_dual
    from Capital import produce_conjure_unique_triple
    from Capital import produce_conjure_unique_triple__312
    from Capital import return_self, slice_all, StringOutput


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
        'caller_frame_1',                       caller_frame_1,
        'create_cache',                         create_cache,
        'create_DelayedFileOutput',             create_DelayedFileOutput,
        'create_SimpleStringOutput',            create_SimpleStringOutput,
        'create_StringOutput',                  create_StringOutput,
        'path_basename',                        path_basename,
        'produce_cache_functions',              produce_cache_functions,
        'produce_conjure_by_name',              produce_conjure_by_name,
        'produce_conjure_dual__21',             produce_conjure_dual__21,
        'produce_conjure_dual',                 produce_conjure_dual,
        'produce_conjure_triple',               produce_conjure_triple,
        'produce_conjure_unique_dual',          produce_conjure_unique_dual,
        'produce_conjure_unique_triple__312',   produce_conjure_unique_triple__312,
        'produce_conjure_unique_triple',        produce_conjure_unique_triple,
        'return_self',                          return_self,


        #
        #   Values
        #
        'cadence_constructing',         cadence_constructing,
        'cadence_entered',              cadence_entered,
        'cadence_exception',            cadence_exception,
        'cadence_exited',               cadence_exited,
        'cadence_initialized',          cadence_initialized,
        'cadence_reuse',                cadence_reuse,
        'capital_global',               capital_global,
        'slice_all',                    slice_all,
    )
