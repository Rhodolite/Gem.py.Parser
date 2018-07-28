#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.BookcaseManyFrill')
def module():
    require_module('PythonParser.ManyExpression')


    bookcase_many_frill_cache = create_cache('bookcase-many-frill', conjure_nub)


    #
    #   NOTE:
    #       This is pretty similiar to 'TripleFrill', but the code is clearer with making
    #       this is a seperate class and using .begin, .many & .end for the members
    #       (instead of .a, .b, & .c as in TripleFrill)
    #
    class BookcaseManyFrill(Object):
        __slots__ = ((
            'begin',                    #   ParserToken+
            'many',                     #   ManyFrill
            'end',                      #   ParserToken+
        ))


        class_order   = CLASS_ORDER__BOOKCASE_MANY_FRILL
        display_name  = 'bookcase-*-frill'
        herd_estimate = 0
        is_herd       = false


        __init__       = construct__123
        count_newlines = count_newlines__123
        __repr__       = portray__123
        display_token  = display_token__123
        order          = order__abc


    BookcaseManyFrill.a = BookcaseManyFrill.begin
    BookcaseManyFrill.b = BookcaseManyFrill.many
    BookcaseManyFrill.c = BookcaseManyFrill.end

    BookcaseManyFrill.k1 = BookcaseManyFrill.begin
    BookcaseManyFrill.k2 = BookcaseManyFrill.many
    BookcaseManyFrill.k3 = BookcaseManyFrill.end


    conjure_bookcase_many_frill__213 = produce_conjure_unique_triple__312(
                                           'bookcase_many_frill__213',
                                           BookcaseManyFrill,
                                           bookcase_many_frill_cache,
                                       )

    BookcaseManyFrill.transform = produce_transform__abc('bookcase_many_frill', conjure_bookcase_many_frill__213)


    @share
    def conjure_bookcase_many_frill(begin, list, end):
        return conjure_bookcase_many_frill__213(begin, conjure_many_frill(list), end)
