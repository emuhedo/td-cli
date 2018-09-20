from sqlite3 import Error

from todo.commands.base import Command
from todo.renderers import RenderOutput, RenderOutputWithTextwrap


class Get(Command):
    def run(self, args):
        try:
            todo = self._get_todo_or_raise(args.id)
            RenderOutput("{subsequent_indent}{bold}{blue}{group_name}{reset}\n").render(
                group_name=todo[1] or "global", subsequent_indent=" " * 4
            )

            RenderOutput("{details}").render(details=todo[3])

            RenderOutputWithTextwrap(
                "\n{grey}{completed} {bold}{todo_id}{normal}: ", "{details}"
            ).render(
                details=todo[2],
                completed="✓" if todo[4] else "x",
                todo_id=todo[0],
                subsequent_indent=" " * 7,
            )
        except Error as e:
            print(u'[*] Could not get a todo due to "{}"'.format(e))
