# Python - Exceptions

Practice handling exceptions in Python with simple utility functions.

## Tasks

0. Safe list printing: `safe_print_list(my_list=[], x=0)` prints up to `x`
   elements from a list, stopping on out-of-range access and returning the
   count printed.
1. Safe printing of an integers list: `safe_print_integer(value)` prints an
   integer with `{:d}` and returns `True` on success, `False` otherwise.
2. Print and count integers: `safe_print_list_integers(my_list=[], x=0)` prints
   only integer elements among the first `x` items and returns how many were
   printed.
3. Integers division with debug: `safe_print_division(a, b)` divides two
   integers, prints the result in a `finally` block, and returns the result or
   `None` on error.
4. Divide a list: `list_division(my_list_1, my_list_2, list_length)` returns a
   list of element-wise divisions with error handling and messages for type,
   zero division, or out-of-range cases.
5. Raise exception: `raise_exception()` raises a `TypeError`.
6. Raise a message: `raise_exception_msg(message="")` raises a `NameError` with
   the provided message.
