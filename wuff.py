import typer
from rich.panel import Panel
from typer import Option
from datetime import date
from rich import print
from typing_extensions import Annotated

import helper
from classes.WuffException import WuffException
from create import create_dog
from find import find_dogs
from stats import get_stats

app = typer.Typer()


@app.command()
def find(name: Annotated[str, typer.Argument(help="Name of the Dog to find.")],
         year: int = Option(date.today().year, help="Record year on which to filter the dogs.")
         ) -> None:
    try:
        dogs = helper.get_dogs(year=year)
        find_dogs(dogs=dogs, name=name)
    except WuffException as e:
        print(Panel(f"[red]{e}[/red]", title="Error"))


@app.command()
def create(year: int = Option(date.today().year, help="Record year on which to filter the dogs"),
           o: str = Option("./", "-o", "--output-dir", help="Directory to save the image to.")) -> None:
    try:
        dogs = helper.get_dogs(year=year)
        create_dog(dogs=dogs, output_directory=o)
    except WuffException as e:
        print(Panel(f"[red]{e}[/red]", title="Error"))


@app.command()
def stats(year: int = Option(date.today().year, help="Record year on which to filter the dogs")) -> None:
    try:
        dogs = helper.get_dogs(year=year)
        get_stats(dogs)
    except WuffException as e:
        print(Panel(f"[red]{e}[/red]", title="Error"))


if __name__ == "__main__":
    app()
