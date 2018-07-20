#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Sapphire.Parse7')
def gem():
    require_gem('Sapphire.Core')
    require_gem('Sapphire.Expression')
    require_gem('Sapphire.Match')
    require_gem('Sapphire.Statement')


    show = false


    def parse7_expression(m):
        [
                name, left_parenthesis, single_quote, right_parenthesis,
        ] = m.group('name', 'left_parenthesis', 'single_quote', 'OLD__right_parenthesis')

        expression = conjure_identifier(name)

        if left_parenthesis is none:
            return expression

        if single_quote is none:
            return CallExpression(
                       expression,
                       Arguments_0(
                           conjure_left_parenthesis(left_parenthesis),
                           conjure_right_parenthesis(right_parenthesis),
                       ),
                   )

        return CallExpression(
                   expression,
                   Arguments_1(
                       conjure_left_parenthesis(left_parenthesis),
                       SingleQuote(single_quote),
                       conjure_right_parenthesis(right_parenthesis),
                   ),
               )


    def parse7_statement_class(m0, s):

        if m is none:
            raise_unknown_line()

        [
            name1, left_parenthesis, name2, right_parenthesis__colon, newline,
        ] = m.group('name1', 'left_parenthesis', 'name2', 'ow__right_parenthesis__colon__ow', 'newline')

        parameters = ParameterColon_1(
                         conjure_left_parenthesis(left_parenthesis),
                         conjure_identifier(name2),
                         OperatorRightParenthesisColon(right_parenthesis__colon),
                     )

        return ClassHeader(KeywordClass(m0.group('indented') + m0.group('keyword__ow')), name1, parameters, newline)


    def parse7_statement_decorator_header(m0, s):

        if m is none:
            raise_unknown_line()

        return DecoratorHeader(
                   OperatorAtSign(m0.group('indented') + m0.group('keyword__ow')),
                   parse7_expression(m),
                   conjure_token_newline(m.group('ow_comment_newline')),
               )


    def parse7_statement_define_header(m0, s):

        if m is none:
            raise_unknown_line()

        [
            name1, left_parenthesis, name2, right_parenthesis__colon, comment_newline,
        ] = m.group('name1', 'left_parenthesis', 'name2', 'ow__right_parenthesis__colon__ow', 'comment_newline')

        if name2 is none:
            parameters = ParameterColon_0(left_parenthesis + right_parenthesis__colon)
        else:
            parameters = ParameterColon_1(
                             conjure_left_parenthesis(left_parenthesis),
                             conjure_identifier(name2),
                             OperatorRightParenthesisColon(right_parenthesis__colon),
                         )

        return FunctionHeader(
                   KeywordFunction(m0.group('indented') + m0.group('keyword__ow')),
                   name1,
                   parameters,
                   conjure_token_newline(comment_newline),
               )


    def parse7_statement_from(m0, s):

        if m is none:
            raise_unknown_line()

        [
                name1, dot, name2, w_import_w, name3, w_as_w, name4, comma
        ] = m.group('name1', 'ow_dot_ow', 'name2', 'w_import_w', 'name3', 'w_as_w', 'name4', 'ow_comma_ow')

        if dot is none:
            module = conjure_identifier(name1)
        else:
            module = MemberExpression_1(conjure_identifier(name1), conjure_dot(dot), conjure_identifier(name2))

        as_fragment = FromAsFragment(conjure_identifier(name3), conjure_keyword_as(w_as_w), conjure_identifier(name4))

        if comma is none:
            return StatementFromImport(
                       KeywordFrom(m0.group('indented') + m0.group('keyword__ow')),
                       module,
                       KeywordImport(w_import_w),
                       as_fragment,
                       conjure_token_newline(m.group('ow_comment_newline')),
                   )


        if m2 is none:
            return raise_unknown_line()

        [
                name1, w_as_w, name2, comma_2
        ] = m2.group('name1', 'w_as_w', 'name2', 'ow_comma_ow')

        as_fragment_2 = FromAsFragment(conjure_identifier(name1), conjure_keyword_as(w_as_w), conjure_identifier(name2))

        if comma_2 is none:
            return StatementFromImport(
                       KeywordFrom(m0.group('indented') + m0.group('keyword__ow')),
                       module,
                       KeywordImport(w_import_w),
                       CommaExpression_1(as_fragment, conjure_comma(comma), as_fragment_2),
                       conjure_token_newline(m2.group('ow_comment_newline')),
                   )

        raise_runtime_error('parse7_statement_from: incomplete')


    def parse7_statement_import(m0, s):

        if m is none:
            raise_unknown_line()

        return StatementImport_1(
                   KeywordImport(m0.group('indented') + m0.group('keyword__ow')),
                   conjure_identifier(m.group('name1')),
                   conjure_token_newline(m.group('ow_comment_newline')),
               )


    def parse7_statement_return(m0, s):

        if m is none:
            raise_unknown_line()

        return ReturnStatement_1(
                   conjure_keyword_return(m0.group('indented') + m0.group('keyword__ow')),
                   parse7_expression(m),
                   conjure_token_newline(m.group('ow_comment_newline')),
               )


    find_parse7_line = {
                          'class'  : parse7_statement_class,
                          'def'    : parse7_statement_define_header,
                          'from'   : parse7_statement_from,
                          'import' : parse7_statement_import,
                          'return' : parse7_statement_return,
                          '@'      : parse7_statement_decorator_header,
                      }.__getitem__


    @share
    def parse7_python_from_path(path):
        data   = read_text_from_path(path)
        many   = []
        append = many.append

        iterate_lines = z_initialize(data)

        for s in iterate_lines:

            if m is none:
                raise_unknown_line()

            [keyword, name] = m.group('keyword', 'name')

            if keyword is not none:
                assert name is none

                append(find_parse7_line(keyword)(m, s))
                continue


            [indented, comment, newline_2] = m.group('indented', 'comment', 'newline_2')

            assert newline_2 is not none

            if comment is not none:
                if indented is '':
                    append(Comment(comment, newline_2))
                    continue

                append(IndentedComment(indented, comment, newline_2))
                continue

            append(EmptyLine(indented + newline_2))
            continue

        if show:
            for v in many:
                line('%r', v)

        with create_StringOutput() as f:
            w = f.write

            for v in many:
                v.write(w)

        if data != f.result:
            with FileOutput('oops.txt') as f:
                f.write(f.result)

            raise_runtime_error('mismatch on %r: output saved in %r', path, 'oops.txt')
