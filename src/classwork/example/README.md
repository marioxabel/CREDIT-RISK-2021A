# Example

Create a simple commandline application that
can reverse a string.

## Instructions

Create the `Main` class defined on `src/classwork/example/main.py`.

1. Create a branch named `CW-EXAMPLE`
2. Add your implementation and push the changes.
3. Create the PR from `CW-EXAMPLE` into `master`.
    * DO NOT MERGE!
    
### Command: Hello

Create the classic default `hello` command:
* Has an argument called `name` that defaults to `world`.

Usage:

```commandline
$ python -m example hello --name student
```

Expected output: `Hello, student!`

### Command: Reverse

Create a `reverse` command with a single argument: `string`

Usage:

```commandline
python -m example reverse --string student
```

Expected output: `tneduts`