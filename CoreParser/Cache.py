#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('CoreParser.Cache')
def gem():
    cache_many        = []
    append_cache_many = cache_many.append


    if __debug__:
        @share
        def append_cache(name, cache):
            append_cache_many( ((name, cache)) )
    else:
        @share
        def append_cache(name, cache):
            pass


    if __debug__:
        def dump_single_cache__OLD(name, cache):
            line('===  %s  ===', name)

            for [k, v] in iterate_items_sorted_by_key(cache):
                if not v.__class__ is Map:
                    line('%s: %s',
                         (
                            portray_string(k)  if k.__class__ is String  else
                            k                  if k.__class__ is Integer else
                            k.display_token()
                         ),
                         v.display_token())

                    continue

                line('%s:',
                     (
                        portray_string(k)  if k.__class__ is String  else
                        k                  if k.__class__ is Integer else
                        k.display_token()
                     ))

                for [k2, w] in iterate_items_sorted_by_key(v):
                    if not w.__class__ is Map:
                        line('  %s: %s',
                             (
                                portray_string(k2)  if k2.__class__ is String  else
                                k2                  if k2.__class__ is Integer else
                                k2.display_token()
                             ),
                             w.display_token())

                        continue

                    line('  %s:',
                         (
                            portray_string(k2)  if k2.__class__ is String  else
                            k2                  if k2.__class__ is Integer else
                            k2.display_token()
                         ))

                    for [k3, x] in iterate_items_sorted_by_key(w):
                        if not x.__class__ is Map:
                            line('    %s: %s', k3.display_token(), x.display_token())
                            continue

                        line('    %s:', k3.display_token())

                        for [k4, y] in iterate_items_sorted_by_key(x):
                            line('      %s:', k4.display_token())
                            line('        %s', y.display_token())


        @export
        def dump_caches__OLD(use_name = none):
            if use_name is none:
                for [name, cache] in cache_many:
                    line('%s: %d', name, length(cache))

                return

            for [name, cache] in cache_many:
                if use_name == name:
                    dump_single_cache__OLD(name, cache)
                    break
            else:
                raise_runtime_error('did not find cache named %r', portray_string(use_name))
    else:
        @export
        def dump_caches__OLD(use_name = none):
            pass
