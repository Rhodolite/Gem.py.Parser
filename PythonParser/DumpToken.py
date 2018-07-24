#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('PythonParser.DumpToken')
def gem():
    require_gem('PythonParser.Tree')


    class TokenOutput(StringOutput):
        __slots_ = (())


        def token_result(f, r, newline):
            if (r) and (newline):
                f.line('>')
                return false

            f.partial('>')
            return r


    @share
    def create_TokenOutput(f = none):
        return TokenOutput((f) or (create_SimpleStringOutput()))


    @share
    def dump_token(name, token):
        with create_TokenOutput() as f:
            f.line('===  %s  ===', name)
            token.dump_token(f)

            if f.position:
                f.line()

        partial(f.result)
