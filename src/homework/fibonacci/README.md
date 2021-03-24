# Fibonacci

Create a simple python application that:
* Can print an element from the fibonacci sequence.
* Can print an arbitrary length of the fibonacci sequence.

## Instructions

Modify the `Main` class defined on `src/homework/fibonacci/main.py`.

1. Create a branch named `HW-FIBO`
2. Add your implementation and push the changes.
3. Create the PR from `HW-FIBO` into `master`.
    * DO NOT MERGE!

### Command: Element

Complete the `element` method such that it returns the element of the fibonacci sequence at a given position.

Your solution should:
* Be a recursive function.
* Use the `method_caching` decorator.

### Command: Sequence

Complete the `sequence` method such that it returns the fibonacci sequence (list of ints) by calling the `element` method.

You solution should:
* Use for comprehension.
* Use the `timeit` metadecorator.
* Call the `element` method when needed.

## Usage & Testing

A correct implementation should run as following.

Get an element from the fibonacci sequence:

```python
$ python -m fibonacci element --position 10
```

Expected output:

```text
55
```

Get the fibonacci sequence:

```python
$  python -m fibonacci sequence --length 15
```

Expected output:
```text
2020-10-01 19:50:07,791 [WARNING] fibonacci.main: Execution time 0.0
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
```