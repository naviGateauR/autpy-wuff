# wuff.py - CLI mit Wuff und Wau

## Usage

```bash
    # Find a dog by name
    wuff.py find <name> [--year <year>]
    # Get statistics about the dogs for a year
    wuff.py stats [--year <year>]
    # Create a new dog
    wuff.py create [-o <output_dir>] [--year <year>]
 ```

## Authors

- Benedict Schönenberger
- [Noel Stammbach](https://noel-stammbach.ch)

## AI Usage

### Copilot:

Copilot has been used while writing the code for this project. It has been used to generate some code snippets, which
have been modified and integrated into the project.

### ChatGPT

ChatGPT has been used to get a starting point or inspiration for some of the functionality. All the code has than been
rewritten and adapted to make sure it fits the requirements and best practices.
ChatGPT has as well been used to explain code snippets in a more understandable way.

### Brave Search

Brave Search AI has been used to find information about the different libraries and tools that have been used in this
project.

# Project Instructions

## Introduction

For the final block in the AutPy course, you will need to write a small command-line tool. In contrary to the previous
labs, this will be something you need to do on your local machine, as the notebooks aren't a good fit to develop
reusable "real-world" projects.

The main part of the project will explore topics you learned about in the labs: Flow control, data structures, creating
a command-line application and using APIs.

Additionally, there are a couple of new topics being introduced:

- You will be required to use the [Git version control](https://git-scm.com/) to track your work.
- We have various different **additional topics** which we didn't cover so far. You will need to pick and implement *
  *two** of those. You can optionally implement more, but **only two will be graded**.

The project is intended to be solved in **groups of two people**. Working alone or in groups of 3 is possible if you
contact Florian Bruhin beforehand and convince him it's a good idea.

## Grading

- The deadline for the project is **Monday, December 23rd, 18:00**.
- You submit your **Git URL** at the bottom of this notebook, and then run the `!submit` command to submit that
  information. Make sure you also **invite us to your repository** and **select your optional topics**.
- Your Git repositories will be downloaded shortly after the deadline.
- The four blocks of labs together make up 1/3 of the final grade. This project **results in the remaining 2/3 of the
  final grade**.
- To ensure consistent grading, we are unfortunately unable to accomodate for custom project ideas. Sorry!

We will grade various aspects of your work, such as functionality, adherence to best practices, possible bugs/issues,
completeness, etc.

## Setup

To get started, you will need to have two things set up on your machine:

1. Python itself, at least version 3.9. The labs use Python 3.11.x, thus it's recommended to install that, or use the
   more recent Python 3.12 or (very new) 3.13. Both 3.12 and 3.13 contain various improvements to Python's error
   messages, which will make development easier.
2. A suitable development environment (editor/IDE). We recommend PyCharm or VS Code.

The first lab (Python Basics) contained instructions for setting things up. If you haven't followed those at the start
of the semester, do that now.

If you're on macOS, make sure you did follow the instructions shown by the Python installer at the end: Go to the Python
folder in "Applications", then double click on "Install Certificates.command" file.

## Version control with git

Use the [`git` project](http://git-scm.com/) to track changes while you are working on your project. Git allows you to
create a so-called "repository" from your project folder, and then track changes by creating a "commit" for every
change. Later, it's easy to go back to older versions of your code or view the changes between different versions - no
more `my_script_v3_final_REALLYFINAL.py`!

Git also allows for easier collaboration. Instead of sending files around, you use commands like `git push` to push
changes to a host like GitHub or GitLab, and your team partner uses `git pull` to get your latest changes. Just make
sure to not work on the same areas/files at the same time, or things might get a little complex with "merge conflicts".

**Note:** Git is a very powerful but also complex tool. Mastering it will be very useful for your studies (and your
job!), but for this project you will only need a very basic understanding. You will learn more advanced features of git
in the "Software Engineering" classes.

Also note: Git can be used via the command-line, but in the beginning a graphical tool can help understanding git
concepts. There are several free git GUIs available, one of those is for
example [SmartGit](https://www.syntevo.com/smartgit/) (free for educational use if
you [apply for a license](https://www.syntevo.com/register-non-commercial/#academic)). Many IDEs (such as VS Code or
PyCharm) also offer git integration. You're free to use whatever you feel most comfortable with.

Requirements:

- Create a repository on either the OST GitLab, or GitHub. **Make sure the repository is set to private**.
- You are **not allowed to set the repository to public**, even after the AutPy module ended.
- **Invite Florian Bruhin and Timon Erhart** as outlined at the end of the lab.
- **All team members** are required to make commits to the repository. It's expected that all team members put in some
  work for the project, without people just getting "dragged along".
- You do not need to use branches (but you can if you prefer).
- Make multiple commits while working on your project and write descriptive commit messages for your changes.

Resources:

- Real Python has a good
  first [Introduction to Git and GitHub for Python Developers](https://realpython.com/python-git-github-intro/).
- The [GitHub Git Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet/) provides a quick overview
  of the most important commands
- The [official Git Book](http://git-scm.com/book/en/v2) provides a more in-depth look at various topics. Note that you
  will only need the first and parts of the second chapter (until around 2.5) for this course.
- [Oh Shit, Git!?!](https://ohshitgit.com/) and [Flight rules for git](https://github.com/k88hudson/git-flight-rules)
  for when things go wrong, and you need to "undo" something.
- [GIT PURR! Git Commands Explained with Cats!](https://girliemac.com/blog/2017/12/26/git-purr/) for some more advanced
  features.

## Project: "CLI mit Wuff und Wau"

The aim of the project is to write a command-line tool which does various operations based on
the [registered dogs in the city of Zurich](https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002). This
information is made available as "Open Data" and is thus freely accessible.

Your CLI should have three major features, which are detailed in the sections further down below:

- Search for dogs using a given name
- Perform data analysis based on the entire data set
- Make up new dogs

You are free on how to structure these different functionalities. Some possible approaches:

- Use [argparse sub-commands](https://docs.python.org/3/library/argparse.html#sub-commands) to have e.g. a
  `wuff.py find Luna`, `wuff.py stats` and `wuff.py create`.
- Write multiple scripts, e.g. a `wuff_find.py`, `wuff_stats.py` and `wuff_create.py`. Make sure you don't copy-paste
  code between them.
- Implement a single command-line interface which does different things based on how it is invoked, similarly to what we
  did with the drink generator CLI. For example, you could use `wuff.py` to show statistics, `wuff.py Luna` to search
  for a dog and `wuff.py --create` to create a new dog.

General requirements:

- **Download the data** from the Open Data Stadt Zürich website using the `requests` library.
    - Download URL: `https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen_od1002/download/KUL100OD1002.csv` (you
      can assume the URL/filename stays stable)
    - Use the data in-memory, **don't store it** in a file.
    - Don't unnecessarily download the data multiple times.
    - ...or in other words: Every time the tool is started, the data should be downloaded (but only once).
    - **Don't filter/sanitize** (säubern) the data, unless explicitly requested in the requirements.
    - When the `AnzHunde` column contains e.g. `2`, handle this in your code as if there were **two exact lines** like
      this in the file. It's easiest to handle this where you read in the data.
- The files contain data from all years from 2015 to 2024.
    - This leads to a lot of duplicates (if a dog was born in 2015, it will be in the file 9 times).
    - Thus, **for all commands below, first filter the data** based on the year in the first column, and only look at
      one year at a time.
    - Every command **should have a `--year` flag** to select the year to use.
    - If no `--year` argument is given, **use the latest year** for which data is available.
    - Write your code in a way that it will continue to work when new data is published in 2025.
- **Handle errors** in an appropriate way, e.g. by showing a useful error message to the user.
    - Make sure you follow best practices while catching exceptions (also
      see [The Most Diabolical Python Antipattern – Real Python](https://realpython.com/the-most-diabolical-python-antipattern/)).
    - As a rule of thumb, consider invalid values or other possible issues for data coming either from the user, or from
      the internet.
- Make sure it's **clear to a user how to use your tool** without having to read the code.
    - For example, make sure the scripts have sensible names and/or show an appropriate `--help` output (`argparse` or
      the other CLI toolkits will help you with that).
    - If you choose to write multiple scripts, you can also provide a "readme" file that explains how to invoke them.
- If you choose to write multiple scripts, make sure you **don't copy-paste code** between them.
- Use the **best practices** you've learned about.
    - Don't reinvent the wheel where Python offers a straightforward way to do things.

Additional hints:

- **Consider getting the basic functionality to work first** (e.g. having no error handling), and then revisiting the
  requirements.
- `requests` will give you a string with the downloaded data - use [
  `.splitlines()`](https://docs.python.org/3/library/stdtypes.html#str.splitlines) to turn them into a list of strings,
  which you can then pass to the CSV reader.
- Consider using a [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader) for easy access to the
  data. You should not specify `fieldnames`, as they are contained in the first row of the file.
- You're allowed to use [Pandas](https://pandas.pydata.org/) instead of `csv` if you're familiar with it. If you do so,
  it's expected that you **use its features** for handling the data, and not just use it to read the CSV file.
- Unfortunately, the format of the data is weird in two ways:
    - The data starts with a (non-standard) [UTF-8 Byte Order Mark](https://en.wikipedia.org/wiki/Byte_order_mark),
      which means the first column will be read incorrectly as `ï»¿"StichtagDatJahr"`. **You can fix this** by doing
      `r.encoding = "utf-8-sig"` (with `r` being the return value of `requests.get(...)`).
    - The sex (== (biologisches)
      Geschlecht; [!= gender](https://www.merriam-webster.com/grammar/sex-vs-gender-how-they2019re-different)) of the
      dogs is redundant in the data: `SexHundCd`, `SexHundLang` and `SexHundSort`. They all contain the same
      information, consistently use one of them in your code.

### Search for dogs

When your tool gets called with the name of a dog, it shows the birth year and sex (male/female) of the dog (or dogs, if
there are multiple with the same name).

Sample output (your invocation and output may vary):

```console
$ wuff find Luna 
Luna 2014 f
Luna 2016 f
# ... more results omitted ...
```

### Perform data analysis

Your tool finds and prints various interesting aspects about the given data. Those are:

- Which is the longest dog name? (if there is a tie, it's okay to print only one, or all of them, whatever you prefer --
  also note that the names are cut off unfortunately, you can ignore that)
- Which is the shortest one? (same as above; also, `?` in the data should not count as the shortest name)
- Which are the top 10 most common names...
    - ...overall?
    - ...for male dogs?
    - ...for female dogs?
    - Also show the count for each of those
    - Hint: a [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) makes this
      easier.
    - You don't need to preprocess names or e.g. merge similar names, i.e. "Luna" and "Luna-Verena (Mona Lisa)" are two
      different dogs.
- How many dogs are male vs. female?

Your tool should print all this information in a single run. How the output looks exactly is up to you, as long as all
this information is visible.

Sample output (your invocation and output may vary):

```console
$ wuff stats    
Shortest Name: Bo
Longest Name:  Zar-Lorcan vom Franzosenkeller
# ... more output omitted ...
```

### Make up new dogs

The third functionality in your tool is to make up a new dog from the existing data. To do so, it should collect the
following attributes:

- Random sex (`m` or `f`)
- A random dog name from the data, only considering data of the matching sex
- A random birth year from the data, only considering data of the matching sex
- A random dog media file (picture/video) downloaded from [random.dog](https://random.dog/)
    - Use either the [JSON API](https://random.dog/woof.json) or [plain text URL](https://random.dog/woof) to find the
      download URL.
    - The downloaded file should be named following the pattern `dogname_birthyear.extension` (for example
      `Bello_2010.jpg`), based on the data collected above.
    - Note that dog names can contain characters which **aren't allowed in filenames** (e.g. `Pippi/Burni` is in the
      data).
        - Any printable/"visible" character that's **not allowed in a filename on Windows** should be replaced by `_` as
          a placeholder.
        - You can ignore maximum filename lengths (they are truncated in the data anyways) as well as special
          filenames (if I get a dog, I'll name it `NUL`!)
    - Downloading binary files via `requests` is a bit harder than downloading text, see the example below for some
      guidance.
    - Additionally, the command should have an `-o` / ` --output-dir` argument which allows specifying a directory where
      the downloaded file should be put. By default, the file should end up in the current directory.

Example code to download binary data:

```python
response = requests.get(url, stream=True)
with open('mydata.bin', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
```

*(By using `stream=True` and `shutil.copyfileobj`, we avoid first copying the entire data into RAM -- instead it is "
streamed" directly from the web server into the file. While this doesn't make a big difference for image files, it's
still considered best practice to avoid wasting RAM, especially for bigger files.)*

When all required data has been gathered, print the properties of the new dog (name, birth year, sex, media filename).

Sample output (your invocation and output may vary):

```console
$ wuff create -o ~/Downloads
Here's your new dog!
Name: Noizy
Birth year: 2013
Sex: m
The image of the new dog can be found here: /home/alice/Downloads/Noizy_2013.png
```

## Additional topics

As outlined above, you are required to use git and implement **two** additional topics. They use third-party libraries
or tools you haven't used so far.

These projects and third-party libraries can be installed via `pip install ...`.
See [Installing Python Modules](https://docs.python.org/3/installing/index.html) for details.

Optional but recommended: Try using a virtualenv (if you're not using `uv` as additional topic), so that you don't need
to mess with your system-wide Python installation for just one project.
See [Installing Packages - Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
and [Python Virtual Environments in Five Minutes | Chris Warrick](https://chriswarrick.com/blog/2018/09/04/python-virtual-environments/).

**Note:** Depending on your setup and/or operating system, you will not be able to run Python tools (like `pip`, etc.)
in your terminal. The easiest way around this is to prefix the command with `py -m` (Windows) or `python3 -m` (
Linux/macOS), e.g. `py -m pip install ...`. In case you still run into trouble, please ask us for help!

You can select from the following topics:

### Type annotations

You might already have noticed that in many other programming languages you need to specify the types of arguments,
return values or variables (so called "static typing"), while in Python, you don't need to do so ("dynamic typing").

However, Python still provides syntax for optional type annotations (or "type hints"). The language itself ignores those
annotations, but separate tools can read them and warn the developer if the code doesn't conform to the annotations.

Tools like VS Code or PyCharm also benefit from those annotations, as they will be able to provide better
auto-completion and other guidance based on them. The by far most common tool used to verify the annotations
is [mypy](https://mypy.readthedocs.io/). For this topic, you set up mypy and annotate your code with type annotations.

Requirements:

- Run mypy on your code and make sure that type checking succeeds.
- Make sure all your functions are fully type annotated, including the "inner type" for containers like lists or dicts.
  You can annotate types with `Any` where really needed, but don't leave them unannotated.
- Configure mypy to turn on its "strict mode", which will turn unannotated or partially annotated functions into errors.
- You can disable warnings from mypy with appropriate comment directives, if needed, but make sure you explain why you
  did so.
- Use [modern typing usability improvements](https://mypy-lang.blogspot.com/2021/01/mypy-0800-released.html). In
  particular:
    - Use the builtins like `list` and `dict` for annotations, not the `List` and `Dict` equivalents from `typing`. For
      details, see [PEP 585 – Type Hinting Generics In Standard Collections](https://peps.python.org/pep-0585/). It's
      fine to use `typing` for cases where there is no builtin name (e.g. `Any` or `Callable`)
    - Use `|` for union types, in particular, use e.g. `str | None` instead of `Optional[None]`. For details,
      see [PEP 604 – Allow writing union types as X | Y](https://peps.python.org/pep-0604/).
    - Add `from __future__ import annotations` to your files, so that type annotations have no runtime performance costs
      and you can use those features above even with older Python versions (3.7+).
      See [mypy: Future annotations import](https://mypy.readthedocs.io/en/latest/runtime_troubles.html#future-annotations-import-pep-563),
      and for more details, [PEP 563 – Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/).

Resources:

- [mypy documentation](https://mypy.readthedocs.io/en/stable/index.html)
- Python reference for the [`typing` module](https://docs.python.org/3/library/typing.html)
- [Python Type Checking (Guide) – Real Python](https://realpython.com/python-type-checking/)
- [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/), the PEP (Python Enhancement Proposal) originally
  introducing this concept.

### Using rich for beautiful output

The [rich library](https://github.com/willmcgugan/rich) provides beautiful formatting for terminal output. It provides
you with a Python API to easily output things like emoji, tables, etc. to the terminal.

Requirements:

- Use `rich` to beautify your output.
- Use colors and emojis (e.g. dogs?).
- For the "list dogs by name" functionality, output the data as a table.

Resources:

- [rich documentation](https://rich.readthedocs.io/en/latest/)
- [rich README in Swiss German](https://github.com/willmcgugan/rich/blob/master/README.de-ch.md) ;-)

## Selected additional topics

In the cell below, please select the **two** additional topics which should be graded (by editing the markdown and
changing `[ ]` to `[x]`):