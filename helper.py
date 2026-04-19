import requests
import csv

from classes.Dog import Dog, SexEnum
from classes.WuffException import WuffException


def get_dogs(year: int, mock: bool = False) -> list[Dog]:
    try:
        res = requests.get(
            "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv", timeout=15)
        res.raise_for_status()
        res.encoding = 'utf-8-sig'
        reader = csv.DictReader(res.text.splitlines(), delimiter=',')
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout, requests.exceptions.ConnectionError,
            requests.exceptions.RequestException) as err:
        raise WuffException("Oops! We encountered a error while fetching the Dogs.", err)

    out: list[Dog] = []

    for row in reader:
        name = row['HundenameText']
        birth_year = int(row['GebDatHundJahr'])
        record_year = int(row['StichtagDatJahr'])
        sex = SexEnum(row['SexHundLang'])
        if record_year == year:
            for _ in range(int(row['AnzHunde'])):
                d = Dog(name=name, birth_year=birth_year, sex=sex)
                out.append(d)
    return out
