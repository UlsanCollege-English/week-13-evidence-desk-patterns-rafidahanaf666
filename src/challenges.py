"""Week 1 Homework: Evidence Desk Patterns.

Complete each function using the data structure pattern named in the docstring.

Rules:
- Python 3.11+
- Standard library only
- Do not change function names or parameters
- Run tests with: pytest -q
"""

from collections import deque


# -----------------------------------------------------------------------------
# Required Problem 1
# -----------------------------------------------------------------------------

def count_evidence(evidence: list[str]) -> dict[str, int]:
    """Return a dictionary counting how many times each evidence label appears.

    Pattern: frequency counting
    Data structure: dictionary

    Examples:
        >>> count_evidence(["phone", "receipt", "phone"])
        {'phone': 2, 'receipt': 1}
        >>> count_evidence([])
        {}

    Args:
        evidence: A list of evidence labels.

    Returns:
        A dictionary where each key is an evidence label and each value is the
        number of times that label appears.
    """
    # TODO: Create an empty dictionary.
    # TODO: Loop through evidence.
    # TODO: Update the count for each item.
    # TODO: Return the dictionary.
    pass


# -----------------------------------------------------------------------------
# Required Problem 2
# -----------------------------------------------------------------------------

def first_repeated_id(ids: list[str]) -> str | None:
    """Return the first suspect ID that appears a second time.

    Pattern: seen before
    Data structure: set

    Examples:
        >>> first_repeated_id(["A17", "B22", "C91", "B22"])
        'B22'
        >>> first_repeated_id(["A17", "B22", "C91"])
        None

    Args:
        ids: A list of suspect ID strings.

    Returns:
        The first ID that appears again, or None if there are no repeats.
    """
    # TODO: Create an empty set named seen.
    # TODO: Loop through ids.
    # TODO: If the current ID is already in seen, return it.
    # TODO: Otherwise, add it to seen.
    # TODO: Return None if no repeated ID is found.
    pass


# -----------------------------------------------------------------------------
# Required Problem 3
# -----------------------------------------------------------------------------

def valid_tags(tags: str) -> bool:
    """Return True if all bracket-style evidence tags are balanced.

    Pattern: stack matching
    Data structure: list used as a stack

    Valid tag characters are (), [], and {}.
    Ignore all other characters.

    Examples:
        >>> valid_tags("{[()]}")
        True
        >>> valid_tags("{[(])}")
        False
        >>> valid_tags("case-{A17}[photo]")
        True

    Args:
        tags: A string that may contain bracket characters.

    Returns:
        True if brackets are balanced correctly, otherwise False.
    """
    # TODO: Create an empty stack.
    # TODO: Create a dictionary of closing brackets to opening brackets.
    # TODO: Push opening brackets onto the stack.
    # TODO: For closing brackets, check whether the stack top matches.
    # TODO: Return True only if the stack is empty at the end.
    pass


# -----------------------------------------------------------------------------
# Required Problem 4
# -----------------------------------------------------------------------------

def lookup_alias(aliases: dict[str, str], alias: str) -> str | None:
    """Return the real name connected to an alias.

    Pattern: lookup table
    Data structure: dictionary

    Examples:
        >>> aliases = {"Big Red": "Marco Silva", "Ghostline": "Eli Brooks"}
        >>> lookup_alias(aliases, "Ghostline")
        'Eli Brooks'
        >>> lookup_alias(aliases, "Unknown")
        None

    Args:
        aliases: A dictionary mapping alias names to real names.
        alias: The alias to search for.

    Returns:
        The real name if the alias exists, otherwise None.
    """
    # TODO: Return the matching real name if the alias exists.
    # TODO: Return None if the alias is not in the dictionary.
    pass


# -----------------------------------------------------------------------------
# Optional Challenge 1
# -----------------------------------------------------------------------------

def process_reports(reports: list[str]) -> list[str]:
    """Return case reports in first-in, first-out processing order.

    Pattern: queue processing
    Data structure: collections.deque

    This function is optional for the homework unless your instructor tells you
    otherwise.

    Examples:
        >>> process_reports(["burglary", "traffic stop", "noise complaint"])
        ['burglary', 'traffic stop', 'noise complaint']

    Args:
        reports: A list of report labels in arrival order.

    Returns:
        A list of report labels in the order they were processed.
    """
    # TODO: Create a deque from reports.
    # TODO: Repeatedly popleft from the queue and append to processed.
    # TODO: Return processed.
    queue = deque(reports)
    pass


# -----------------------------------------------------------------------------
# Optional Challenge 2
# -----------------------------------------------------------------------------

def largest_time_gap(times: list[int]) -> int:
    """Return the largest gap between neighboring event times after sorting.

    Pattern: sorting + scan
    Data structure: list

    This function is optional for the homework unless your instructor tells you
    otherwise.

    Treat times as simple integer timestamps for this exercise. For example,
    915 means 9:15 and 1300 means 13:00. You do not need to convert minutes.

    Examples:
        >>> largest_time_gap([1300, 915, 1600, 945])
        355
        >>> largest_time_gap([1200])
        0

    Args:
        times: A list of integer event times.

    Returns:
        The largest difference between neighboring sorted times. Return 0 if
        there are fewer than two times.
    """
    # TODO: Return 0 when there are fewer than two times.
    # TODO: Sort the times. Hint: sorted(times) avoids changing the input list.
    # TODO: Scan neighboring pairs and track the largest gap.
    pass
