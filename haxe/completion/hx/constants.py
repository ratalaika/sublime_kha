
COMPLETION_TRIGGER_MANUAL = 1
COMPLETION_TRIGGER_AUTO = 2

COMPILER_CONTEXT_MACRO = 1
COMPILER_CONTEXT_REGULAR = 2

COMPLETION_TYPE_REGULAR = 1 # regular compiler completion without hints
COMPLETION_TYPE_HINT = 2 # compiler hints
COMPLETION_TYPE_TOPLEVEL = 4 # include top level if useful
COMPLETION_TYPE_TOPLEVEL_FORCED = COMPLETION_TYPE_TOPLEVEL | 8 # force inclusion of top level completion

TOPLEVEL_OPTION_TYPES = 1
TOPLEVEL_OPTION_LOCALS = 2
TOPLEVEL_OPTION_KEYWORDS = 4

TOPLEVEL_OPTION_ALL = TOPLEVEL_OPTION_KEYWORDS | TOPLEVEL_OPTION_LOCALS | TOPLEVEL_OPTION_TYPES