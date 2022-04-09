from xonsh.completers import completer, tools
from xonsh.parsers.completion_context import CommandContext


@tools.contextual_command_completer_for("python")
def django_manage_py_completer(ctx: CommandContext):
    """Xonsh history completer for sqlite backend."""
    args = [arg.raw_value for arg in ctx.args[: ctx.arg_index]]
    if ctx.arg_index > 1 and args[1] != "manage.py":
        return

    return tools.comp_based_completer(ctx, start_index=1, DJANGO_AUTO_COMPLETE="1")


completer.add_one_completer("django", django_manage_py_completer, "<xompleter")
