from enum import Enum

CODEGEN_TYPE_COMMON = 'common'
CODEGEN_TYPE_IMPL = 'impl'

CODEGEN_CLASSTYPE_PARSER = 'parsers'
CODEGEN_CLASSTYPE_TRANSLATOR = 'translators'

TRANS  = 'trans'
PARSER = 'parser'

NODE_REFERENCE           = 'node'
NODE_DEFAULT             = 'node_default'
NODE_SPACENAME           = 'node_spacename'
NODE_CLASSNAME           = 'node_classname'
NODE_IMPL_CLASSNAME      = 'node_classname_impl'
NODE_VARNAME             = 'node_varname'
NODE_DATAPATH            = 'node_path'
NODE_DATACAST            = 'node_type_cast'
NODE_CONTNODE_CHILDREN   = 'node_sub_container_nodes'
NODE_LISTNODE_CHILDREN   = 'node_sub_list_nodes'
NODE_LEAFFAMILY_CHILDREN = 'node_sub_remained_nodes'

LISTNODE_KEYS = 'listnode_keys'

PARSER_ELEMENT_EXTRACT_PATH    = 'parser_element_extract_path'
PARSER_LEAFFAMILY_EXTRACT_PATH = 'parser_leaffamily_extract_path'
PARSER_USE_ROOT_NATIVE = 'parser_root_native'

CLI_HAS_SUBMODE = 'cli_has_submode'

TRANS_CLI_INDENT_1 = 'translator_cli_indent'
TRANS_CLI_INDENT_2 = 'translator_cli_submode_indent'

TRANS_LISTNODE_CLI_FMT        = 'trans_listnode_cli_format'
TRANS_LISTNODE_UNDO_CLI_FMT   = 'trans_listnode_undo_cli_format'
TRANS_LISTNODE_CLI_IS_ONELINE = 'is_one_line_command'


TRANS_LEAFFAMILY_CLI_FMT      = 'trans_leaffamily_cli_fmt'
TRANS_LEAFFAMILY_CLI_PREFIX   = 'trans_leaffamily_cli_prefix'
TRANS_CLI_TYPE = 'cli_type'
TRANS_CLI_TYPE_SUBMODE = 'SUB_MODE'
TRANS_CLI_TYPE_NONE    = 'NONE'
TRANS_LEAFFAMILY_UNDO_CLI_FMT = 'trans_leaffamily_undo_cli_fmt'



CLI_INDENT_BETWEEN_MODE = ' ' * 2
CLI_INDENT_MODE_CONFIG  = ' ' * 0
DEBUG = 0

