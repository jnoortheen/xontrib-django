import xonsh.completers.completer
from xonsh.completers.tools import (
    contextual_command_completer_for,
    comp_based_completer,
)
from xonsh.parsers.completion_context import CommandContext


@contextual_command_completer_for("python")
def django_manage_py_completer(ctx: CommandContext):
    """Xonsh history completer for sqlite backend."""
    args = [arg.raw_value for arg in ctx.args[: ctx.arg_index]]
    if ctx.arg_index > 1 and args[1] != "manage.py":
        return

    return comp_based_completer(ctx, start_index=1, DJANGO_AUTO_COMPLETE="1")


xonsh.completers.completer.add_one_completer(
    "django", django_manage_py_completer, "<xompleter"
)
