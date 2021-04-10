# Exam01 Coding: Flatten Json

This is the practical section of the first exam.

## Instructions

1. Run the [sync process](https://hackmd.io/@credit-risk-iteso/Sy5g9U_E_#Github-Sync) to get the latest changes into your repo.
2. Create a branch called: `EX01-FLATTEN`
3. Add your implementation and push the changes.
4. Create the PR from `EX01-FLATTEN` into `master`.
    * DO NOT MERGE!
    
## Grading

**Total points**: 40 points

* (3 pts) The python application is correctly configured on the `exam01` folder (e.g., `main.py`, `__main__.py`, `__init__.py`).
* (6 pts) Your solution contains a **recursive function** called `flat_dictionary` in the `exam01/utils.py` script. This function should receive a dictionary as an input and return a flat version of the dictionary as the output (see the examples).
* (6 pts) Create a `show` command on the `Main` class  (defined on `exam01/main.py`) that allows you to display the dictionary in the terminal. It should have the following arguments:
    * `filename`: the name of the file (e.g., `ex-1.json`, `ex-2.json`, `ex-3.json`, `ex-4.json`, `ex-5.json`)

```commandline
$ python -m exam01 show --filename ex-1.json
```

* (25 pts) Create a `flatten` command that shows the flat version of the json file. Consider the following:
    * This command also has the `filename` argument.
    * This command should use the `flat_dictionary` function.
    * Should be defined as a method licated on the `Main` class (defined on `exam01/main.py`).
    * 4 points per tests (5 tests) if the output is correct.
    * 5 points for correct execution of secret tests.

## Flat Dictionary Explanation

Consider the following dictionary:

```python
example_input = {
    "a": 1,
    "b": {
        "c": 2
    }
}
```

The `flat_dictionary` function located at `exam01/utils.py` should be able to transform that dictionary (`target`) into
a flat version. The definition of "flat dictionary" is one were it doesn't contain any nested dictionaries of lists.

```python
from .utils import flat_dictionary, display

example_output = flat_dictionary(target=example_input)
display(example_output)
```
Example output should contain the following:

```text
{
    "a": 1,
    "b.c": 2
}
```

Note that the keys get merged into the first top-level dictionary, separated by a `.` (dot).

We can apply this same principles for dictionaries with multiple nested dictionaries and lists.
For the `list` case we should add the position of the element (index) as part of the key.

```python
example_input_with_nested_dictionaries = {
    "a": {
      "b": 1,
      "c": 2
    },
    "d": {
      "e": 3,
      "f": 4
    }
}
```

```python
example_input_with_lists = {
  "a": ["b", "c", "d"]
}
```

## Grading for flatten command execution

#### EX-1

Your solution should be able to flatten a dictionary that contains another dictionary (e.g., dictionaries with dictionaries)

* (2 pts) Your solution works using the `flat_dictionary` function (see test in notebook).
* (2 pts) Your solution works in the commandline.

```commandline
$ python -m exam01 show --filename ex-1.json
{
    "a": 1,
    "b": 2,
    "c": {
        "d": 5,
        "e": 6
    }
}
```

```commandline
$ python -m exam01 flatten --filename ex-1.json
{
    "a": 1,
    "b": 2,
    "c.d": 5,
    "c.e": 6
}
```

#### EX-2

Consider that the dictionary can contain an arbitrary number of nested levels.

* (2 pts) Your solution works using the `flat_dictionary` function (see test in notebook).
* (2 pts) Your solution works in the commandline.

```commandline
$ python -m exam01 show --filename ex-2.json
{
    "a": 1,
    "b": 2,
    "c": {
        "d": 5,
        "e": 6
    },
    "f": {
        "g": 7,
        "h": {
            "i": {
                "j": 8
            }
        }
    }
}
```

```commandline
$ python -m exam01 flatten --filename ex-2.json
{
    "a": 1,
    "b": 2,
    "c.d": 5,
    "c.e": 6,
    "f.g": 7,
    "f.h.i.j": 8
}
```

#### EX-3

If the dictionary contains a list with values, the flat version should use the "index" as a key.

* (2 pts) Your solution works using the `flat_dictionary` function (see test in notebook).
* (2 pts) Your solution works in the commandline.

```commandline
$ python -m exam01 show --filename ex-3.json
{
    "a": 1,
    "b": 2,
    "c": [
        3,
        4,
        5
    ]
}
```

```commandline
$ python -m exam01 flatten --filename ex-3.json
{
    "a": 1,
    "b": 2,
    "c.0": 3,
    "c.1": 4,
    "c.2": 5
}
```

### EX-4

Note that a list can contain more dictionaries and/or more lists. Everything should be flatten out in the final result.

* (2 pts) Your solution works using the `flat_dictionary` function (see test in notebook).
* (2 pts) Your solution works in the commandline.

```commandline
$ python -m exam01 show --filename ex-4.json
{
    "a": 1,
    "b": [
        {
            "c": 2
        },
        {
            "d": 3,
            "e": {
                "f": 4,
                "g": 5
            }
        }
    ]
}
```

```commandline
$ python -m exam01 flatten --filename ex-4.json
{
    "a": 1,
    "b.0.c": 2,
    "b.1.d": 3,
    "b.1.e.f": 4,
    "b.1.e.g": 5
}
```

#### EX-5

* (2 pts) Your solution works using the `flat_dictionary` function (see test in notebook).
* (2 pts) Your solution works in the commandline.

```commandline
$ python -m exam01 show --filename ex-5.json
{
    "a": 1,
    "b": [
        {
            "c": 2
        },
        {
            "d": 3,
            "e": [
                4,
                5,
                {
                    "f": {
                        "g": 6
                    }
                }
            ]
        }
    ]
}

```

```commandline
$ python -m exam01 flatten --filename ex-5.json
{
    "a": 1,
    "b.0.c": 2,
    "b.1.d": 3,
    "b.1.e.0": 4,
    "b.1.e.1": 5,
    "b.1.e.2.f.g": 6
}
```