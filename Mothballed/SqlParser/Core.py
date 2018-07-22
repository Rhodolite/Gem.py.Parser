#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('SqlParser.Core')
def gem():
    require_gem('CoreParser.ConjureTreeComment')
    require_gem('CoreParser.Line')
    require_gem('CoreParser.Token')
    require_gem('CoreParser.Tokenizer')
    require_gem('Gem.Cache')
    require_gem('Gem.DelayedFileOutput')
    require_gem('Gem.Exception')
    require_gem('Gem.Path')
    require_gem('Gem.StringOutput')


    from CoreParser import conjure_comment_newline, conjure_token_newline, conjure_tree_comment
    from CoreParser import EmptyLine, lookup_identifier
    from CoreParser import qj, qk, qs, raise_unknown_line, Token, wj, wk, z_initialize
    from Gem import create_DelayedFileOutput, create_StringOutput, module_path, path_join, read_text_from_path


    share(
        #
        #   Classes
        #
        'EmptyLine',    EmptyLine,
        'Token',        Token,


        #
        #   Functions
        #
        'conjure_comment_newline',      conjure_comment_newline,
        'conjure_token_newline',        conjure_token_newline,
        'conjure_tree_comment',         conjure_tree_comment,
        'create_DelayedFileOutput',     create_DelayedFileOutput,
        'create_StringOutput',          create_StringOutput,
        'lookup_identifier',            lookup_identifier,
        'path_join',                    path_join,
        'qj',                           qj,
        'qk',                           qk,
        'qs',                           qs,
        'raise_unknown_line',           raise_unknown_line,
        'read_text_from_path',          read_text_from_path,
        'wj',                           wj,
        'wk',                           wk,
        'z_initialize',                 z_initialize,


        #
        #   Values (Gem)
        #
        'module_path',  module_path,
    )
