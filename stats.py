from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich import print, box
from rich.text import Text
from classes.Dog import Dog, SexEnum
from collections import Counter

from classes.WuffException import WuffException


def get_valid_dogs(name: str, ignore_invalid_names: bool = True) -> int:
    invalid_names = '?'
    if not ignore_invalid_names or name not in invalid_names:
        return len(name)
    else:
        return 100


def get_stats(dogs: list[Dog]) -> None:
    if len(dogs) == 0:
        raise WuffException(
            f"No dogs have been found for the selected year. Please try another year or check the data source.")
    longest_dog_name: Dog = max(dogs, key=lambda d: get_valid_dogs(d.name, ignore_invalid_names=False))
    shortest_dog_name: Dog = min(dogs, key=lambda d: get_valid_dogs(d.name, ignore_invalid_names=True))

    dog_names: list[str] = [d.name for d in dogs]
    female_dogs_names: list[str] = [d.name for d in dogs if d.sex == SexEnum.FEMALE]
    male_dogs_names: list[str] = [d.name for d in dogs if d.sex == SexEnum.MALE]

    popular_dog_names = Counter(dog_names).most_common(10)
    popular_female_dog_names = Counter(female_dogs_names).most_common(10)
    popular_male_dog_names = Counter(male_dogs_names).most_common(10)
    count_total_dogs = len(dog_names)
    count_female_dogs = len(female_dogs_names)
    count_male_dogs = len(male_dogs_names)

    stats = "\n".join(
        [
            Text(f"Total Dogs: [not bold][dark_orange]{count_total_dogs}[/dark_orange][/not bold]",
                 style="bold white").plain,
            Text(f"Total Female Dogs: [not bold][hot_pink]{count_female_dogs}[/hot_pink][/not bold]",
                 style="bold white").plain,
            Text(f"Total Male Dogs: [not bold][blue]{count_male_dogs}[/blue][/not bold]", style="bold white").plain,
            Text(f"Longest Dog Name: [not bold][dark_orange]{longest_dog_name.name}[/dark_orange][/not bold]",
                 style="bold white").plain,
            Text(f"Shortest Dog Name: [not bold][dark_orange]{shortest_dog_name.name}[/dark_orange][/not bold]",
                 style="bold white").plain,
        ]
    )
    o_stats_panel = Panel(stats, title="Overall Stats", style="bold dark_orange", box=box.ROUNDED)

    table_total = Table(title="Top Dog Names", style="dark_orange", box=box.ROUNDED)
    table_total.add_column("Name", style="magenta", justify="center")
    table_total.add_column("Total", style="cyan", justify="center")
    for name, count in popular_dog_names:
        table_total.add_row(name, str(count))

    table_female = Table(title="Top Female Dog Names", style="hot_pink", box=box.ROUNDED)
    table_female.add_column("Name", style="magenta", justify="center")
    table_female.add_column("Total", style="cyan", justify="center")
    for name, count in popular_female_dog_names:
        table_female.add_row(name, str(count))

    table_male = Table(title="Top Female Dog Names", style="blue", box=box.ROUNDED)
    table_male.add_column("Name", style="magenta", justify="center")
    table_male.add_column("Total", style="cyan", justify="center")
    for name, count in popular_male_dog_names:
        table_male.add_row(name, str(count))

    layout = Layout()
    layout.split_column(
        o_stats_panel,
        Layout(name="lower")
    )
    layout['lower'].split_row(
        table_total,
        table_female,
        table_male
    )

    print(o_stats_panel)
    print(Columns([table_total, table_female, table_male], equal=True))
