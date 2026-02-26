# Python ABC and OOP Tasks (0-5)

This directory contains the `python-abc` project tasks focused on abstract classes, inheritance, and object-oriented design in Python.

## Project Objective

Build clean, modular Python classes by applying:
- Abstract Base Classes (`abc`)
- Method implementation in subclasses
- Progressive OOP concepts across Tasks 0 through 5

## Directory

- `task_00_abc.py`: Abstract `Animal` class and concrete subclasses

## Prerequisites

- Python 3.8+

## How to Run Task 0

From the `python-abc` directory:

```bash
python3 task_00_abc.py
```

Or use a checker/main file like:

```python
from task_00_abc import Animal, Dog, Cat

print(Dog().sound())
print(Cat().sound())
```

Expected behavior:
- `Dog().sound()` returns `"Bark"`
- `Cat().sound()` returns `"Meow"`
- Instantiating `Animal()` raises `TypeError` (abstract class)

## Task Breakdown (0-5)

### Task 0: Abstract Animal Class and its Subclasses

File: `task_00_abc.py`

What it does:
- Declares abstract class `Animal` using `ABC`
- Defines abstract method `sound()`
- Implements `Dog.sound()` returning `"Bark"`
- Implements `Cat.sound()` returning `"Meow"`

Status: Completed

### Task 1

File: `task_01_*.py` (to be added)

What it does:
- Will be documented once Task 1 is implemented.

Status: Pending

### Task 2

File: `task_02_*.py` (to be added)

What it does:
- Will be documented once Task 2 is implemented.

Status: Pending

### Task 3

File: `task_03_*.py` (to be added)

What it does:
- Will be documented once Task 3 is implemented.

Status: Pending

### Task 4

File: `task_04_*.py` (to be added)

What it does:
- Will be documented once Task 4 is implemented.

Status: Pending

### Task 5

File: `task_05_*.py` (to be added)

What it does:
- Will be documented once Task 5 is implemented.

Status: Pending

## Suggested Commit Structure

Use one commit per task so history stays clear:
- `Task 0: add abstract Animal class with Dog and Cat subclasses`
- `Task 1: ...`
- `Task 2: ...`
- `Task 3: ...`
- `Task 4: ...`
- `Task 5: ...`
- `Docs: update python-abc README for tasks 0-5`
