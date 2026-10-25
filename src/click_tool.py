"""click_tool.py — утиліта на click з командою say."""
import click


@click.group()
def cli():
    """Утиліта на click. Доступна команда: say."""


@cli.command()
@click.option("--name", required=True, help="Ім'я, яке треба вивести.")
def say(name):
    """Виводить ім'я, якщо воно не починається з літери p/P."""
    if name.lower().startswith("p"):
        click.echo(f"Ім'я «{name}» не підходить: воно починається з літери P.")
    else:
        click.echo(name)


if __name__ == "__main__":
    cli()