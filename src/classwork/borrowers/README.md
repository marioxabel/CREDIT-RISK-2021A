# Borrowers

This is a simple python application that allows
you to "register" borrowers into a json file.

## Command: setup

This command creates an empty `candidates.json` file.
You can change the filename by modifying the `BORROWERS_FILENAME` environment variable 
(default value `candidates.json`). 

```commandline
$ python -m borrowers setup
```

By adding the `--replace` flag you can re-create the file.
```commandline
$ python -m borrowers setup --replace
```

Expected output similar to:

```text
File created: /home/rhdzmota/Documents/Github/CREDIT-RISK-2021A/src/classwork/borrowers/candidates.json
```

## Command: register

You can register a new borrower by calling the `register` command:

```commandline
$ python -m borrowers register \
    --email alice@example.com \
    --age 22 \
    --income 15000
```

```commandline
$ python -m borrowers register \
    --email bob@example.com \
    --age 35 \
    --income 52000
```

```commandline
$ python -m borrowers register \
    --email carol@example.com \
    --age 27 \
    --income 38000
```

The `candidates.json` file should be similar to:

```text
{
    "last_updated": "2021-03-27 14:28:04",
    "candidates": [
        {
            "email": "alice@example.com",
            "age": 22,
            "income": 15000,
            "created_at": "2021-03-27 14:27:00",
            "updated_at": "2021-03-27 14:27:00"
        },
        {
            "email": "bob@example.com",
            "age": 35,
            "income": 52000,
            "created_at": "2021-03-27 14:27:48",
            "updated_at": "2021-03-27 14:27:48"
        },
        {
            "email": "carol@example.com",
            "age": 27,
            "income": 38000,
            "created_at": "2021-03-27 14:28:04",
            "updated_at": "2021-03-27 14:28:04"
        }
    ]
}
```

Calling the `register` command with an existing email **should not** create duplicate records in the `candidates.json` file.

## Command: update

You can use the `update` command to replace a key/value of an existing record by email.

Example: Update `bob@example.com` income to `55000`.

```commandline
$ python -m borrowers update \
    --email bob@example.com \
    --field-name income \
    --field-value 55000
```

Using the `update` command with a new email should not modify the `candidates.json` file:

```commandline
$  python -m borrowers update\
     --email diana@example.com \
     --field-name income \
     --field-value 75000
```

The `candidates.json` file should be similar to:

```text
{
    "last_updated": "2021-03-27 14:30:43",
    "candidates": [
        {
            "email": "alice@example.com",
            "age": 22,
            "income": 15000,
            "created_at": "2021-03-27 14:27:00",
            "updated_at": "2021-03-27 14:27:00"
        },
        {
            "email": "bob@example.com",
            "age": 35,
            "income": 55000,
            "created_at": "2021-03-27 14:27:48",
            "updated_at": "2021-03-27 14:30:43"
        },
        {
            "email": "carol@example.com",
            "age": 27,
            "income": 38000,
            "created_at": "2021-03-27 14:28:04",
            "updated_at": "2021-03-27 14:28:04"
        }
    ]
}
```