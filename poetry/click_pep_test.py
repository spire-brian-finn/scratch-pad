#!/usr/bin/python

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.option("-a", default=1)
@click.option("-b", default=2)
@click.argument("derp", nargs=-1)
@click.option("--bar",
             default="Execute end-to-end test suite. Any options listed after a double dash "
                  "'--' will be carried over to pytest ")
def foo(a, b, derp, bar):
    click.echo("%d %d %s" % (a, b, derp))
    click.echo(bar)


if __name__ == "__main__":
    foo()
