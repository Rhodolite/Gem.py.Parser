#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.BookcaseManyExpression')
def module():
    require_module('PythonParser.BookcaseManyFrill')


    @share
    def dump_token__X__many(t, f):
        frill = t.frill
        many  = t.many

        frill_many = frill.many

        frill_estimate = frill_many.frill_estimate

        if frill_estimate is 1:
            assert length(many) is 2

            many   [0].dump_token(f)
            frill_many.dump_token(f)
            many   [1].dump_token(f)

            return

        if frill_estimate is 2:
            assert length(many) is 3

            many      [0].dump_token(f)
            frill_many.v .dump_token(f)
            many      [1].dump_token(f)
            frill_many.w .dump_token(f)
            many      [2].dump_token(f)

            return

        if frill_estimate is 3:
            assert length(many) is 4

            many      [0].dump_token(f)
            frill_many.v .dump_token(f)
            many      [1].dump_token(f)
            frill_many.w .dump_token(f)
            many      [2].dump_token(f)
            frill_many.x .dump_token(f)
            many      [3].dump_token(f)

            return

        if frill_estimate is 4:
            assert length(many) is 5

            many      [0].dump_token(f)
            frill_many.v .dump_token(f)
            many      [1].dump_token(f)
            frill_many.w .dump_token(f)
            many      [2].dump_token(f)
            frill_many.x .dump_token(f)
            many      [3].dump_token(f)
            frill.many.y .dump_token(f)
            many      [4].dump_token(f)

            return

        iterator   = iterate(many)
        next_frill = next_method(iterate(frill_many))

        next_method(iterator)().dump_token(f)

        for v in iterator:
            next_frill().dump_token(f)
            v           .dump_token(f)


    @export
    def write__X__many_end(t, w):
        frill = t.frill
        many  = t.many

        frill_many = frill.many

        frill_estimate = frill_many.frill_estimate

        if frill_estimate is 1:
            assert length(many) is 2

            many[0].write(w)
            w(frill_many.s)
            many[1].write(w)
            w(frill.end.s)
            return

        if frill_estimate is 2:
            assert length(many) is 3

            many[0].write(w)
            w(frill_many.v.s)
            many[1].write(w)
            w(frill_many.w.s)
            many[2].write(w)
            w(frill.end.s)
            return

        if frill_estimate is 3:
            assert length(many) is 4

            many[0].write(w)
            w(frill_many.v.s)
            many[1].write(w)
            w(frill_many.w.s)
            many[2].write(w)
            w(frill_many.x.s)
            many[3].write(w)
            w(frill.end.s)
            return

        if frill_estimate is 4:
            assert length(many) is 5

            many[0].write(w)
            w(frill_many.v.s)
            many[1].write(w)
            w(frill_many.w.s)
            many[2].write(w)
            w(frill_many.x.s)
            many[3].write(w)
            w(frill.many.y.s)
            many[4].write(w)
            w(frill.end.s)
            return

        iterator         = iterate(many)
        write_frill_many = next_method(frill_many.iterate_write(w))

        next_method(iterator)().write(w)

        for v in iterator:
            write_frill_many()
            v.write(w)

        w(frill.end.s)


    @share
    class BookcaseManyExpression(ParserTrunk):
        __slots__ = ((
            'frill',                    #   BookcaseManyFrill
            'many',                     #   TupleOfExpression+
        ))


        def __init__(t, frill, many):
            t.frill = frill
            t.many  = many


        def __repr__(t):
            return arrange('<%s %s %r>', t.__class__.__name__, t.frill, ' '.join(portray(v)   for v in t.many))


        def count_newlines(t):
            return t.many.count_newlines() + t.frill.count_newlines()


        def display_token(t):
            return arrange('<%s %s %s>',
                           t.display_name,
                           t.frill.display_token(),
                           ' '.join(v.display_token()   for v in t.many))


        def dump_token(t, f, newline = true):
            frill = t.frill

            f.partial('<%s ', t.display_name)
            frill.begin.dump_token(f)
            dump_token__X__many(t, f)
            r = frill.end.dump_token(f, false)

            return f.token_result(r, newline)


        order = order__frill_many


        def write(t, w):
            w(t.frill.begin.s)

            write__X__many_end(t, w)


    #BookcaseManyExpression.k1 = BookcaseManyExpression.frill
    BookcaseManyExpression.k2 = BookcaseManyExpression.many


    @share
    def produce_conjure_bookcase_many_expression(
            name, Meta,

            produce_conjure_with_frill = true,
    ):
        assert (produce_conjure_with_frill is true) or (produce_conjure_with_frill is 1)

        cache = {}

        conjure_dual = produce_conjure_dual(name + '__X2', Meta, cache)


        @rename('conjure_%s', name)
        def conjure_bookcase_many_expression(begin, many, frill_many, end):
            return conjure_dual(
                       conjure_bookcase_many_frill(begin, frill_many, end),
                       conjure_tuple_of_many_expression(many),
                   )


        if python_debug_mode:
            append_cache(name, cache)

        if produce_conjure_with_frill == 1:
            if python_debug_mode:
                conjure_dual = rename('conjure_%s__with_frill', name)(conjure_dual)

            return ((
                       conjure_bookcase_many_expression,
                       conjure_dual,
                   ))

        return ((
                   conjure_bookcase_many_expression,
                   static_method(conjure_dual),
               ))


    class Arguments_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = 'arguments-*'


        def first_argument(t):
            return t.many[0]


        scout_variables = scout_variables__many


    class ListExpression_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = '[*]'
        
        is_CRYSTAL_atom                       = true
        is_PYTHON__atom__or__special_operator = true
        is_PYTHON_special_operator            = false


        scout_variables = scout_variables__many
        write_variables = write_variables__many


    class MapExpression_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = '{:*:}'
       
        is_CRYSTAL_atom                       = true
        is_PYTHON__atom__or__special_operator = true
        is_PYTHON_special_operator            = false


        scout_variables = scout_variables__many


    class Parameters_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = 'parameter-(*)'


        def add_parameters(t, art):
            for v in t.many:
                v.add_parameters(art)


        def parameter_1_named(t, name):
            return 0


        def scout_variables(t, many):
            for v in t.many:
                v.scout_default_values(many)


    class TupleExpression_Many(BookcaseManyExpression):
        __slots__    = (())
        class_order  = CLASS_ORDER__BOOKCASE_MANY_EXPRESSION
        display_name = '{,*,}'

        is_CRYSTAL_atom                       = true
        is_PYTHON__atom__or__special_operator = true
        is_PYTHON_special_operator            = false


        scout_variables = scout_variables__many


    [
        conjure_arguments_many, conjure_arguments_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'arguments-*',
            Arguments_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_list_expression_many, conjure_list_expression_many__with_frill
    ] = produce_conjure_bookcase_many_expression(
            'list-expression-*',
            ListExpression_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_map_expression_many, conjure_map_expression_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'map-expression-*',
            MapExpression_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_parameters_many, conjure_parameters_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'parameter-*',
            Parameters_Many,

            produce_conjure_with_frill = 1,
        )

    [
        conjure_tuple_expression_many, conjure_tuple_expression_many__with_frill,
    ] = produce_conjure_bookcase_many_expression(
            'tuple-expression-*',
            TupleExpression_Many,

            produce_conjure_with_frill = 1,
        )


    #
    #   .mutate
    #
    Arguments_Many.mutate = produce_mutate__frill__many(
                                'arguments_many',
                                PRIORITY_ASSIGN,
                                PRIORITY_ASSIGN,
                                PRIORITY_ASSIGN,
                                conjure_arguments_many__with_frill,
                            )

    ListExpression_Many.mutate = produce_mutate__frill__many(
                                     'list_expression_many',
                                     PRIORITY_COMPREHENSION,
                                     PRIORITY_TERNARY,
                                     PRIORITY_TERNARY,
                                     conjure_list_expression_many__with_frill,
                                 )

    MapExpression_Many.mutate = produce_mutate__frill__many(
                                    'list_expression_many',
                                    PRIORITY_COMPREHENSION,
                                    PRIORITY_MAP_ELEMENT,
                                    PRIORITY_MAP_ELEMENT,
                                    conjure_map_expression_many__with_frill,
                                )

    TupleExpression_Many.mutate = produce_mutate__frill__many(
                                    'tuple_expression_many',
                                    PRIORITY_TERNARY,
                                    PRIORITY_TERNARY,
                                    PRIORITY_TERNARY,
                                    conjure_tuple_expression_many__with_frill,
                                )

    #
    #   .mutate
    #
    Parameters_Many.transform = produce_transform__frill__many(
                                    'parameters_many',
                                    PRIORITY_ASSIGN,
                                    conjure_parameters_many__with_frill,
                                )


    share(
        'conjure_arguments_many',           conjure_arguments_many,
        'conjure_list_expression_many',     conjure_list_expression_many,
        'conjure_map_expression_many',      conjure_map_expression_many,
        'conjure_parameters_many',          conjure_parameters_many,
        'conjure_tuple_expression_many',    conjure_tuple_expression_many,
    )
