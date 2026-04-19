import random
import requests
from pathlib import Path

from classes.Dog import Dog, SexEnum
import os
from rich import print
from rich.panel import Panel

from classes.WuffException import WuffException


def create_dog(dogs: list[Dog], output_directory: str) -> None:
    if len(dogs) == 0:
        raise WuffException(
            f"No dogs have been found for the selected year. Please try another year or check the data source.")

    random_sex = random.choice(list(SexEnum))
    random_sex_value_german = SexEnum(random_sex).value

    if random_sex_value_german == "männlich":
        random_sex_value_english = "male"
        sex_color = "blue"
    else:
        random_sex_value_english = "female"
        sex_color = "hot_pink"

    dog_list_matching_sex: list[Dog] = [d for d in dogs if d.sex == random_sex]

    random_dog_name: str = random.choice(dog_list_matching_sex).name
    random_dog_birth_year: int = random.choice(dog_list_matching_sex).birth_year

    forbidden_characters = r"<>:\"/|?*"
    sanitized_dog_name = random_dog_name
    for fc in forbidden_characters:
        sanitized_dog_name = sanitized_dog_name.replace(fc, "_")

    try:
        json_from_random_org = requests.get('https://random.dog/woof.json', timeout=15)
        json_from_random_org.raise_for_status()
        dog_pic_url = json_from_random_org.json()["url"]
    except requests.exceptions.HTTPError as err:
        raise WuffException("Oops! We encountered a error while fetching a dog image url.", err)
    except requests.exceptions.Timeout as err:
        raise WuffException("Oops! We encountered a error while fetching a dog image url.", err)
    except requests.exceptions.ConnectionError as err:
        raise WuffException("Oops! We encountered a error while fetching a dog image url.", err)
    except requests.exceptions.RequestException as err:
        raise WuffException("Oops! We encountered a error while fetching a dog image url.", err)
    except requests.exceptions.JSONDecodeError as err:
        raise WuffException("Oops! We encountered a error while fetching a dog image url.", err)

    if not '.' in dog_pic_url:
        raise WuffException("File type could not be determined.", f"Cannot split {dog_pic_url} due to missing period.")

    file_extension = dog_pic_url.split('.')[-1]

    picture_filename = Path(output_directory) / f"{sanitized_dog_name}_{random_dog_birth_year}.{file_extension}"

    if not os.path.isdir(output_directory):
        raise WuffException(f"{output_directory} is not a valid directory.")

    if not os.access(output_directory, os.R_OK):
        raise WuffException(f"Not a readable directory: {output_directory}")

    if not os.access(output_directory, os.W_OK):
        raise WuffException(f"Not a writable directory: {output_directory}")

    try:
        response = requests.get(dog_pic_url, stream=True)
        response.raw.decode_content = True
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise WuffException("Oops! We encountered a error while fetching the dog image.", err)
    except requests.exceptions.Timeout as err:
        raise WuffException("Oops! We encountered a error while fetching the dog image.", err)
    except requests.exceptions.ConnectionError as err:
        raise WuffException("Oops! We encountered a error while fetching the dog image.", err)
    except requests.exceptions.RequestException as err:
        raise WuffException("Oops! We encountered a error while fetching the dog image.", err)
    except requests.exceptions.JSONDecodeError as err:
        raise WuffException("Oops! We encountered a error while fetching the dog image.", err)

    try:
        with open(picture_filename, 'wb') as out_file:
            for chunk in response.iter_content(chunk_size=1024):
                out_file.write(chunk)
    except PermissionError as err:
        raise WuffException(f"No permission to access {picture_filename}", err)
    except FileExistsError as err:
        raise WuffException(f"Picture {picture_filename} already exists", err)

    print(Panel.fit('\n'.join(
        [f"Congrats! You've created a new dog!",
         f"The name is [{sex_color}]{random_dog_name}[/{sex_color}].",
         f"It was born in {random_dog_birth_year}.",
         f"It's sex is [{sex_color}]{random_sex_value_english}[/{sex_color}].",
         f"Your can find a picture here: [turquoise2][link=file://{picture_filename}]{picture_filename}[/link][/turquoise2]."
         ]
    )))
