# Week 6 Assignment - Future Proof With Python

## Files

- `safe_tools.py` - Three functions (`safe_divide`, `safe_number`, `get_field`) that use try/except so they return a message instead of crashing.
- `unbreakable.py` - A program that keeps asking for an age and never crashes on bad or unwise input.
- `README.md` - This file, describing the project and answering the question below.

## Why can the `if` check not catch `abc` on its own?

An `if` check can only compare a value that already exists, but `int("abc")` fails with a `ValueError` before the `if` ever runs. A `try`/`except` is needed to catch input that cannot be converted to a number at all.
