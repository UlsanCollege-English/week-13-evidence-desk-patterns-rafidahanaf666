[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cm6PS4yt)
# Week 1 Homework: Evidence Desk Patterns

## Student Name

Rafid

## Summary

This homework practices four core data structure patterns used in Python:

- **Frequency counting** with dictionaries — tallying how often each item appears
- **Duplicate detection** with sets — checking whether a value has been seen before
- **Stack matching** with lists — validating that opening and closing brackets pair up correctly
- **Lookup tables** with dictionaries — retrieving a value directly by key in constant time

Each problem is framed as a fictional investigation case file. The optional challenges add queue processing with `deque` and a sorting + scan pattern for finding the largest gap between sorted timestamps.

## How to Run Tests

From the repository root, run:

```bash
pytest -q
```

To run one test file:

```bash
pytest -q tests/test_challenges.py
```

## Required Problems

Complete these functions in `src/challenges.py`:

1. `count_evidence`
2. `first_repeated_id`
3. `valid_tags`
4. `lookup_alias`

## Optional Challenges

1. `process_reports`
2. `largest_time_gap`

Optional tests are included and enabled (the `@pytest.mark.skip` lines have been removed).

---

# Problem Notes

## 1. Evidence Counter

### Pattern

Frequency counting

### Data Structure

Dictionary (`dict`)

### Approach

- Step 1: Create an empty dictionary called `counts`.
- Step 2: Loop through each item in the `evidence` list.
- Step 3: If the item is already a key, increment its value by 1; otherwise set it to 1. Return the dictionary.

### Complexity

- Time: `O(n)`
- Space: `O(k)` where k is the number of unique labels

**Explanation:** We visit each of the n items exactly once, so time is linear. The dictionary grows only as large as the number of distinct labels (k ≤ n), so space is also linear in the worst case (all labels unique).

### Edge Cases Checked

- [x] Empty list → returns `{}`
- [x] One item → returns `{"item": 1}`
- [x] Repeated items → count increments correctly
- [x] Different labels → each gets its own key
- [x] Case sensitivity → `"phone"` and `"Phone"` are different keys

---

## 2. Repeat Suspect ID

### Pattern

Seen before

### Data Structure

Set (`set`)

### Approach

- Step 1: Create an empty set called `seen`.
- Step 2: Loop through each ID in `ids`. If it is already in `seen`, return it immediately — this is the first repeat.
- Step 3: Otherwise add the ID to `seen` and continue. Return `None` if the loop finishes without finding a repeat.

### Complexity

- Time: `O(n)`
- Space: `O(n)`

**Explanation:** In the worst case (no repeats), we visit every ID once. Set membership checks and inserts are O(1) on average, so the overall time is O(n). The set can hold up to n items in that same worst case.

### Edge Cases Checked

- [x] Empty list → returns `None`
- [x] No repeated IDs → returns `None`
- [x] First two IDs match → returns the first ID immediately
- [x] Multiple repeated IDs → returns whichever repeat comes first

---

## 3. Evidence Tag Validator

### Pattern

Stack matching

### Data Structure

List used as a stack (`list`)

### Approach

- Step 1: Create an empty list `stack` and a dictionary `matching` that maps each closing bracket to its expected opening bracket: `{")": "(", "]": "[", "}": "{"}`.
- Step 2: Loop through every character in the string. Ignore non-bracket characters. Push opening brackets (`(`, `[`, `{`) onto the stack. For a closing bracket, check whether the stack is non-empty and whether the top of the stack equals the expected opening bracket; if not, return `False`. Otherwise pop the top.
- Step 3: After the loop, return `True` only if the stack is empty (no unmatched opening brackets remain).

### Complexity

- Time: `O(n)`
- Space: `O(n)`

**Explanation:** We scan each character exactly once — O(n). In the worst case (all opening brackets), the stack holds every character — O(n) space.

### Edge Cases Checked

- [x] Empty string → `True` (no brackets to mismatch)
- [x] Correctly nested tags → `True`
- [x] Mismatched types like `([)]` → `False`
- [x] Closing bracket before any opening bracket → `False`
- [x] Unclosed opening bracket → `False`
- [x] Non-bracket characters are ignored → `True` for `"case-{A17}[photo]"`

---

## 4. Alias Directory

### Pattern

Lookup table

### Data Structure

Dictionary (`dict`)

### Approach

- Step 1: Use `aliases.get(alias, None)` to look up the alias key.
- Step 2: Return the result — the real name if found, or `None` if not.

### Complexity

- Time: `O(1)` average
- Space: `O(1)` (no extra data structure created)

**Explanation:** Dictionary key lookup is O(1) on average because Python dicts are implemented as hash tables. We do not create any new data structure, so space is constant.

### Edge Cases Checked

- [x] Known alias → returns the correct real name
- [x] Unknown alias → returns `None`
- [x] Empty dictionary → returns `None`

---

## Optional Challenge 1: Dispatch Queue

### Pattern

Queue processing (FIFO)

### Data Structure

`collections.deque`

### Approach

- Step 1: Create a `deque` from the `reports` list.
- Step 2: Loop while the queue is non-empty, calling `popleft()` each iteration and appending to `processed`.
- Step 3: Return `processed`.

### Complexity

- Time: `O(n)` — each `popleft()` is O(1) for deque (vs O(n) for a plain list).
- Space: `O(n)`

---

## Optional Challenge 2: Timeline Gap Finder

### Pattern

Sorting + scan

### Data Structure

List

### Approach

- Step 1: Return 0 immediately if fewer than two times are given.
- Step 2: Sort using `sorted(times)` to avoid mutating the input.
- Step 3: Walk neighbouring pairs, compute each difference, and track the maximum.

### Complexity

- Time: `O(n log n)` — dominated by sorting.
- Space: `O(n)` — for the new sorted list.

---

# Assistance & Sources

## AI Used?

- [x] Yes

## If yes, what did AI help with?

- Reviewing the approach for the stack-matching problem and verifying the edge case logic.
- Confirming time and space complexity explanations were correctly worded.
- Proofreading the README structure against the homework brief requirements.

## Other Sources

- Python 3.11 official documentation: `dict.get`, `set`, `collections.deque`
- Course lecture slides on Big-O notation
