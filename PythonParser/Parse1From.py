#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.Parse1From')
def module():
    require_module('PythonParser.BookcaseKeywordDualStatement')


    def parse1_statement_from_module(index):
        s = qs()

        #
        #<name1>
        #
        m1 = name_match(s, index)

        if m1 is none:
            raise_unknown_line()

        module = conjure_name(m1.group())
        #</name1>

        #
        #<module: name ||| ['.' name] ... 'import'>
        #
        while true:
            m2 = from_module_match1(s, m1.end())

            if m2 is none:
                raise_unknown_line()

            operator = m2.group('operator')

            if operator is not '.':
                break

            operator_dot = conjure_dot(m2.group())

            #
            #<name2>
            #
            m1 = name_match(s, m2.end())

            if m1 is none:
                raise_unknown_line()
            #</name2>

            module = conjure_member_expression(module, conjure_dot_name(operator_dot, conjure_name(m1.group())))

        wj(m2.end())
        wk(conjure_keyword_import(m2.group()))

        return module
        #</module>


    def parse1_statement_from_as():
        s = qs()

        #
        #<name>
        #
        m1 = name_match(s, qj())

        if m1 is none:
            raise_unknown_line()

        imported = conjure_name(m1.group())
        #</name>

        #
        #<as>
        #
        m2 = from_as_match1(s, m1.end())

        if m2 is none:
            raise_unknown_line()

        operator = m2.group('operator')
        #</as>

        if operator is none:
            wk(conjure_line_marker(m2.group()))

            return imported

        if operator is ',':
            wj(m2.end())
            wk(conjure_comma(m2.group()))

            return imported

        keyword_as = conjure_keyword_as(m2.group())

        #
        #<name2>
        #
        m3 = name_match(s, m2.end())

        if m3 is none:
            raise_unknown_line()

        imported = conjure_as_fragment(imported, keyword_as, conjure_name(m3.group()))
        #</name2>

        #
        #<comma-or-newline>
        #
        m4 = comma_or_newline_match1(s, m3.end())

        if m4 is none:
            raise_unknown_line()
        #</comma-or-newline>

        if m4.start('comma') is -1:
            wk(conjure_line_marker(m4.group()))

            return imported

        wj(m4.end())
        wk(conjure_comma(m4.group()))

        return imported


    @share
    def parse1_statement_from(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_from(m.end('indented'), j)

        #
        #<module ... 'import'>
        #
        module = parse1_statement_from_module(j)

        keyword_import = qk()

        wk(none)
        #</module>

        #
        #<imported ... (, | newline)>
        #
        imported = parse1_statement_from_as()

        operator = qk()

        wk(none)
        #<imported/>

        if operator.line_marker:
            return conjure_from_statement(indented_keyword, module, keyword_import, imported, operator)

        if not operator.is_comma:
            raise_unknown_line()

        #
        #<imported ... (, | newline)>
        #
        imported_2 = parse1_statement_from_as()

        operator_2 = qk()

        wk(none)
        #<imported/>

        if operator_2.line_marker:
            return conjure_from_statement(
                       indented_keyword,
                       module,
                       keyword_import,
                       conjure_comma_expression_1(imported, operator, imported_2),
                       operator_2,
                   )

        if not operator_2.is_comma:
            raise_unknown_line()

        many       = [imported, imported_2]
        many_frill = [operator, operator_2]

        while 7 is 7:
            many.append(parse1_statement_from_as())

            operator_7 = qk()

            wk(none)

            if operator_7.line_marker:
                return conjure_from_statement(
                           indented_keyword,
                           module,
                           keyword_import,
                           conjure_comma_expression_many(many, many_frill),
                           operator_7,
                       )

            if not operator_7.is_comma:
                raise_unknown_line()

            many_frill.append(operator_7)
