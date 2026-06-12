import pytest
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- get_range_for_difficulty ---

def test_difficulty_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_difficulty_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_difficulty_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_difficulty_unknown_defaults_to_normal_range():
    assert get_range_for_difficulty("Unknown") == (1, 100)


# --- parse_guess ---

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float_truncates():
    ok, value, err = parse_guess("3.9")
    assert ok is True
    assert value == 3
    assert err is None

def test_parse_guess_none_returns_error():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_empty_string_returns_error():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_non_numeric_returns_error():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None


# --- check_guess ---

def test_check_guess_correct():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_check_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_secret_as_string():
    # app.py passes secret as str on even-numbered attempts
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"

def test_check_guess_returns_message_string():
    outcome, message = check_guess(50, 50)
    assert isinstance(message, str)
    assert len(message) > 0


# --- update_score ---

def test_update_score_win_early():
    # attempt 1: 100 - 10*(1+1) = 80 points added
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

def test_update_score_win_clamps_to_minimum():
    # attempt 9: 100 - 10*10 = 0, clamped to 10
    new_score = update_score(0, "Win", 9)
    assert new_score == 10

def test_update_score_too_high_even_attempt_adds_points():
    new_score = update_score(100, "Too High", 2)
    assert new_score == 105

def test_update_score_too_high_odd_attempt_deducts_points():
    new_score = update_score(100, "Too High", 3)
    assert new_score == 95

def test_update_score_too_low_deducts_points():
    new_score = update_score(100, "Too Low", 1)
    assert new_score == 95

def test_update_score_unknown_outcome_unchanged():
    new_score = update_score(100, "Unknown", 1)
    assert new_score == 100
