# Python Inheritance

This project practices Python inheritance, type checking, and basic geometry class hierarchies.

## Tasks

### 0. Lookup
- **File:** `0-lookup.py`
- **Goal:** Return the list of available attributes and methods of an object using `dir()`.

### 1. My list
- **File:** `1-my_list.py`
- **Goal:** Create `MyList` that inherits from `list` and adds `print_sorted()` to print a sorted copy.

### 2. Exact same object
- **File:** `2-is_same_class.py`
- **Goal:** Return `True` if the object is exactly an instance of the specified class (no subclasses).

### 3. Same class or inherit from
- **File:** `3-is_kind_of_class.py`
- **Goal:** Return `True` if the object is an instance of the class or any subclass.

### 4. Only sub class of
- **File:** `4-inherits_from.py`
- **Goal:** Return `True` only if the object is an instance of a subclass (not the class itself).

### 5. Geometry module
- **File:** `5-base_geometry.py`
- **Goal:** Define an empty `BaseGeometry` class.

### 6. Improve Geometry
- **File:** `6-base_geometry.py`
- **Goal:** Add `area()` that raises `Exception("area() is not implemented")`.

### 7. Integer validator
- **File:** `7-base_geometry.py`
- **Goal:** Add `integer_validator(name, value)` to enforce positive integers with clear errors.

### 8. Rectangle
- **File:** `8-rectangle.py`
- **Goal:** Create `Rectangle` inheriting `BaseGeometry` with validated private `__width` and `__height`.

### 9. Full rectangle
- **File:** `9-rectangle.py`
- **Goal:** Implement `area()` and `__str__` to return `[Rectangle] <width>/<height>`.

### 10. Square #1
- **File:** `10-square.py`
- **Goal:** Create `Square` inheriting `Rectangle` with validated size and `area()`.

### 11. Square #2
- **File:** `11-square.py`
- **Goal:** Extend `Square` with `__str__` returning `[Square] <width>/<height>`.

## Tests
- **Folder:** `tests/`
- **Doctests:** `1-my_list.txt`, `7-base_geometry.txt`
- **Run:** `python3 -m doctest ./tests/*`
