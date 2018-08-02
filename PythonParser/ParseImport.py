#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('PythonParser.ParseImport')
def module():
    require_module('PythonParser.Elemental')
    require_module('PythonParser.Match')


    def parse_python__statement_import_module():
        s = qs()

        #
        #<name>
        #
        m = name_match(s, qj())

        if m is none:
            raise_unknown_line()

        module = conjure_name(m.group())

        j = m.end()

        wi(j)
        wj(j)
        #</name>

        #
        #<module: name ['.' name] ... ('as' | ',' | newline)
        #
        while true:
            m = import_module_match1(s, qj())

            if m is none:
                raise_unknown_line()

            j = m.end()

            wi(j)
            wj(j)

            operator = m.group('operator')

            if operator is not '.':
                break

            operator_dot = conjure_dot(m.group())

            #
            #<name>
            #
            m = name_match(s, qj())

            if m is none:
                raise_unknown_line()

            j = m.end()

            wi(j)
            wj(j)
            #</name>

            module = conjure_member_expression(module, conjure_dot_name(operator_dot, conjure_name(m.group())))

        if operator is none:
            wk(conjure_line_marker(m.group()))

            return module

        if operator is ',':
            wk(conjure_comma(m.group()))

            return module

        keyword_as = conjure_keyword_as(m.group())
        #</module>

        #
        #<name>
        #
        m = name_match(s, qj())

        if m is none:
            raise_unknown_line()

        module = conjure_as_fragment(module, keyword_as, conjure_name(m.group()))

        j = m.end()

        wi(j)
        wj(j)
        #</name>

        #
        #<comma-or-newline>
        #
        m = comma_or_newline_match1(s, qj())

        if m is none:
            raise_unknown_line()
        #</comma-or-newline>

        if m.start('comma') is -1:
            wk(conjure_line_marker(m.group()))

            return module

        wj(m.end())
        wk(conjure_comma(m.group()))

        return module


    @share
    def parse_python__statement_import(m):
        if m.end('newline') is not -1:
            raise_unknown_line()

        j = m.end()

        indented_keyword = evoke_indented_import(m.end('indented'), j)

        wi(j)
        wj(j)

        #
        #<module ... 'import'>
        #
        module   = parse_python__statement_import_module()
        operator = qk()

        wk(none)
        #</module>

        if operator.line_marker:
            return conjure_import_statement(indented_keyword, module, operator)

        if not operator.is_comma:
            raise_unknown_line()

        many       = [module]
        many_frill = [operator]

        while 7 is 7:
            many.append(parse_python__statement_import_module())

            operator = qk()

            if operator.line_marker:
                return conjure_import_statement(
                           indented_keyword,
                           conjure_comma_expression_many(many, many_frill),
                           operator,
                       )

            if not operator.is_comma:
                raise_unknown_line()

            many_frill.append(operator)
