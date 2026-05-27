# Homework Brief
## Case File Portfolio 01: Evidence Desk Patterns

## Overview

This week, you will solve four small interview-style data structure problems. Each problem is a fictional investigation case file. Your job is to recognize the pattern, choose the correct data structure, write the function, and explain your reasoning.

This assignment is not just about making tests pass. You also need to explain the pattern and complexity in your `README.md`.

## Learning Goals

By the end of this homework, you should be able to:

1. Use a dictionary for frequency counting.
2. Use a set to detect repeated values.
3. Use a list as a stack for matching open/close symbols.
4. Use a dictionary as a lookup table.
5. Explain basic time and space complexity.
6. Check common edge cases with tests.

## Repo Structure

```text
src/challenges.py
tests/test_challenges.py
README.md
```

Only `src/challenges.py`, `tests/test_challenges.py`, and `README.md` are graded.

## Rules

- Use Python 3.11+.
- Use standard library only.
- Do not use notebooks for graded work.
- Do not rename the required functions.
- Do not change the test function names unless you are adding your own tests.
- Run `pytest -q` before submitting.
- Update `README.md` before submitting.

## Required Problems

### Problem 1: Evidence Counter

Function:

```python
def count_evidence(evidence: list[str]) -> dict[str, int]:
```

Given a list of evidence labels, return a dictionary counting how many times each label appears.

Example:

```python
count_evidence(["phone", "receipt", "phone", "cash"])
```

Expected result:

```python
{"phone": 2, "receipt": 1, "cash": 1}
```

Required pattern:

- Frequency counting

Required data structure:

- Dictionary

---

### Problem 2: Repeat Suspect ID

Function:

```python
def first_repeated_id(ids: list[str]) -> str | None:
```

Given a list of suspect IDs, return the first ID that appears a second time. If no ID repeats, return `None`.

Example:

```python
first_repeated_id(["A17", "B22", "C91", "B22", "A17"])
```

Expected result:

```python
"B22"
```

Required pattern:

- Seen before

Required data structure:

- Set

---

### Problem 3: Evidence Tag Validator

Function:

```python
def valid_tags(tags: str) -> bool:
```

Return `True` if all bracket-style evidence tags are balanced. Return `False` otherwise.

Valid bracket types:

```text
() [] {}
```

Ignore non-bracket characters.

Examples:

```python
valid_tags("{[()]}")              # True
valid_tags("{[(])}")              # False
valid_tags("case-{A17}[photo]")   # True
```

Required pattern:

- Stack matching

Required data structure:

- List used as a stack

---

### Problem 4: Alias Directory

Function:

```python
def lookup_alias(aliases: dict[str, str], alias: str) -> str | None:
```

Given a dictionary mapping aliases to real names, return the real name for a given alias. If the alias is not found, return `None`.

Example:

```python
aliases = {
    "Big Red": "Marco Silva",
    "The Accountant": "Nina Park",
}

lookup_alias(aliases, "The Accountant")
```

Expected result:

```python
"Nina Park"
```

Required pattern:

- Lookup table

Required data structure:

- Dictionary

## Optional Challenges

These are extra practice unless your instructor says otherwise.

### Optional Challenge 1: Dispatch Queue

Function:

```python
def process_reports(reports: list[str]) -> list[str]:
```

Use `collections.deque` to process reports in first-in, first-out order.

Pattern:

- Queue processing

Data structure:

- `deque`

---

### Optional Challenge 2: Timeline Gap Finder

Function:

```python
def largest_time_gap(times: list[int]) -> int:
```

Sort event times and return the largest difference between neighboring times.

Example:

```python
largest_time_gap([1300, 915, 1600, 945])
```

Sorted times:

```python
[915, 945, 1300, 1600]
```

Expected result:

```python
355
```

Pattern:

- Sorting + scan

Data structure:

- List

## Testing Requirements

You must pass the provided tests:

```bash
pytest -q
```

You should also add at least one test of your own for one required function.

Suggested edge cases:

- Empty list
- Empty string
- One item
- No repeat found
- Unknown alias
- Incorrectly nested tags

## README Requirements

Your `README.md` must include:

1. Summary
2. Approach for each required problem
3. Pattern name for each required problem
4. Data structure used for each required problem
5. Time and space complexity for each required problem
6. Edge-case checklist
7. Assistance & Sources

## Standards Targeted

- S1: Python + Testing Fundamentals
- S3: Big-O Reasoning
- S6: Hash Tables with dict/set
- S7: Stacks + Queues

## Completion Checklist

Before submitting:

- [ ] I implemented all four required functions.
- [ ] I ran `pytest -q`.
- [ ] All required tests pass.
- [ ] I added at least one test of my own.
- [ ] I completed the README.
- [ ] I included complexity for each required problem.
- [ ] I listed edge cases.
- [ ] I included Assistance & Sources.

## Revision Policy

Revisions are accepted only through a Revision Request Issue linked to a PR. Name the specific standards you want re-checked.

Recommended cap: 2 revision requests per student per week.
