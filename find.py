from rich.layout import Layout
from rich.table import Table
from rich import print
from rich.console import Console

from classes.Dog import Dog, SexEnum


def find_dogs(dogs: list[Dog], name: str) -> None:
    table = Table(title="Your search results:")
    table.add_column("No.", style="magenta")
    table.add_column("Name", style="blue")
    table.add_column("Birth Year", style="cyan")
    table.add_column("Sex", style="red")

    counter = 0
    for dog in dogs:
        if dog.name == name:
            counter += 1
            sex = "male" if dog.sex == SexEnum.MALE else "female"
            table.add_row(str(counter), dog.name, str(dog.birth_year), str(sex))

    if counter == 0:
        print("no dog named \"" + name + "\" in database!")
    else:
        print(table)
