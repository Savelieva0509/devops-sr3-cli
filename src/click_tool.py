"""click_tool.py — утиліта на click з командою say.

Команди для запуску (Git Bash, з папки devops-sr3-cli):

python src/click_tool.py --help
python src/click_tool.py say --name Alice
python src/click_tool.py say --name peter
python src/click_tool.py say
"""
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