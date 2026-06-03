"""Tests for Week 1 Homework: Evidence Desk Patterns.

Run from the repository root:
    pytest -q
"""
from __future__ import annotations

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from challenges import (  # noqa: E402
    count_evidence,
    first_repeated_id,
    largest_time_gap,
    lookup_alias,
    process_reports,
    valid_tags,
)


# -----------------------------------------------------------------------------
# Required Problem 1: count_evidence
# -----------------------------------------------------------------------------

def test_count_evidence_counts_multiple_labels():
    evidence = ["phone", "receipt", "phone", "cash", "receipt", "phone"]

    assert count_evidence(evidence) == {
        "phone": 3,
        "receipt": 2,
        "cash": 1,
    }


def test_count_evidence_empty_list():
    assert count_evidence([]) == {}


def test_count_evidence_single_item():
    assert count_evidence(["keycard"]) == {"keycard": 1}


def test_count_evidence_is_case_sensitive():
    assert count_evidence(["phone", "Phone", "phone"]) == {
        "phone": 2,
        "Phone": 1,
    }


# Custom test: all identical labels collapse to one key with correct count
def test_count_evidence_all_same_label():
    assert count_evidence(["knife", "knife", "knife"]) == {"knife": 3}


# -----------------------------------------------------------------------------
# Required Problem 2: first_repeated_id
# -----------------------------------------------------------------------------

def test_first_repeated_id_returns_first_id_that_repeats():
    ids = ["A17", "B22", "C91", "B22", "A17"]

    assert first_repeated_id(ids) == "B22"


def test_first_repeated_id_returns_none_when_no_repeat():
    assert first_repeated_id(["A17", "B22", "C91"]) is None


def test_first_repeated_id_handles_empty_list():
    assert first_repeated_id([]) is None


def test_first_repeated_id_repeat_can_be_first_item():
    assert first_repeated_id(["X01", "X01", "A17"]) == "X01"


# Custom test: only two items, both the same
def test_first_repeated_id_two_identical_items():
    assert first_repeated_id(["Z99", "Z99"]) == "Z99"


# -----------------------------------------------------------------------------
# Required Problem 3: valid_tags
# -----------------------------------------------------------------------------

@pytest.mark.parametrize(
    "tags",
    [
        "",
        "{[()]}",
        "((()))",
        "[]{}()",
        "case-{A17}[photo](verified)",
    ],
)
def test_valid_tags_returns_true_for_balanced_tags(tags):
    assert valid_tags(tags) is True


@pytest.mark.parametrize(
    "tags",
    [
        "{[(])}",
        "(()",
        ")(",
        "case-{A17[photo]",
        "([)]",
    ],
)
def test_valid_tags_returns_false_for_unbalanced_tags(tags):
    assert valid_tags(tags) is False


# Custom test: closing bracket with nothing on stack
def test_valid_tags_lone_closing_bracket():
    assert valid_tags("}") is False


# -----------------------------------------------------------------------------
# Required Problem 4: lookup_alias
# -----------------------------------------------------------------------------

def test_lookup_alias_returns_real_name_for_known_alias():
    aliases = {
        "Big Red": "Marco Silva",
        "The Accountant": "Nina Park",
        "Ghostline": "Eli Brooks",
    }

    assert lookup_alias(aliases, "The Accountant") == "Nina Park"


def test_lookup_alias_returns_none_for_unknown_alias():
    aliases = {"Big Red": "Marco Silva"}

    assert lookup_alias(aliases, "Unknown") is None


def test_lookup_alias_handles_empty_dictionary():
    assert lookup_alias({}, "Ghostline") is None


# Custom test: alias with spaces
def test_lookup_alias_alias_with_spaces():
    aliases = {"The Fox": "Dana Lee"}
    assert lookup_alias(aliases, "The Fox") == "Dana Lee"


# -----------------------------------------------------------------------------
# Optional Challenge 1: process_reports
# -----------------------------------------------------------------------------

def test_process_reports_returns_reports_in_arrival_order():
    reports = ["burglary", "traffic stop", "missing wallet", "noise complaint"]

    assert process_reports(reports) == reports


def test_process_reports_handles_empty_list():
    assert process_reports([]) == []


# -----------------------------------------------------------------------------
# Optional Challenge 2: largest_time_gap
# -----------------------------------------------------------------------------

def test_largest_time_gap_sorts_and_finds_largest_neighbor_gap():
    assert largest_time_gap([1300, 915, 1600, 945]) == 355


def test_largest_time_gap_handles_short_lists():
    assert largest_time_gap([]) == 0
    assert largest_time_gap([1200]) == 0


def test_largest_time_gap_does_not_mutate_input():
    times = [1300, 915, 1600, 945]

    largest_time_gap(times)

    assert times == [1300, 915, 1600, 945]
