import pytest
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- get_range_for_difficulty ---

def test_difficulty_easy():
    result = get_range_for_difficulty("Easy")
    print(f"\n  input='Easy'  ->  range={result}")
    assert result == (1, 20)

def test_difficulty_normal():
    result = get_range_for_difficulty("Normal")
    print(f"\n  input='Normal'  ->  range={result}")
    assert result == (1, 100)

def test_difficulty_hard():
    result = get_range_for_difficulty("Hard")
    print(f"\n  input='Hard'  ->  range={result}")
    assert result == (1, 50)

def test_difficulty_unknown_defaults_to_normal_range():
    result = get_range_for_difficulty("Unknown")
    print(f"\n  input='Unknown'  ->  range={result}")
    assert result == (1, 100)


# --- parse_guess ---

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    print(f"\n  input='42'  ->  ok={ok}, value={value}, err={err}")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float_truncates():
    ok, value, err = parse_guess("3.9")
    print(f"\n  input='3.9'  ->  ok={ok}, value={value}, err={err}")
    assert ok is True
    assert value == 3
    assert err is None

def test_parse_guess_none_returns_error():
    ok, value, err = parse_guess(None)
    print(f"\n  input=None  ->  ok={ok}, value={value}, err='{err}'")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_empty_string_returns_error():
    ok, value, err = parse_guess("")
    print(f"\n  input=''  ->  ok={ok}, value={value}, err='{err}'")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_non_numeric_returns_error():
    ok, value, err = parse_guess("abc")
    print(f"\n  input='abc'  ->  ok={ok}, value={value}, err='{err}'")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_negative_number():
    ok, value, err = parse_guess("-5")
    print(f"\n  input='-5'  ->  ok={ok}, value={value}, err={err}")
    assert ok is True
    assert value == -5
    assert err is None


# --- check_guess ---

def _safe(s):
    return s.encode("ascii", "replace").decode()

def test_check_guess_correct():
    outcome, message = check_guess(50, 50)
    print(f"\n  guess=50, secret=50  ->  outcome='{outcome}', message='{_safe(message)}'")
    assert outcome == "Win"

def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    print(f"\n  guess=60, secret=50  ->  outcome='{outcome}', message='{_safe(message)}'")
    assert outcome == "Too High"

def test_check_guess_too_low():
    outcome, message = check_guess(40, 50)
    print(f"\n  guess=40, secret=50  ->  outcome='{outcome}', message='{_safe(message)}'")
    assert outcome == "Too Low"

def test_check_guess_secret_as_string():
    outcome, message = check_guess(50, "50")
    print(f"\n  guess=50, secret='50' (str)  ->  outcome='{outcome}', message='{_safe(message)}'")
    assert outcome == "Win"

def test_check_guess_returns_message_string():
    outcome, message = check_guess(50, 50)
    print(f"\n  guess=50, secret=50  ->  message type={type(message).__name__}, value='{_safe(message)}'")
    assert isinstance(message, str)
    assert len(message) > 0


# --- update_score ---

def test_update_score_win_early():
    new_score = update_score(0, "Win", 1)
    print(f"\n  score=0, outcome='Win', attempt=1  ->  new_score={new_score}")
    assert new_score == 80

def test_update_score_win_clamps_to_minimum():
    new_score = update_score(0, "Win", 9)
    print(f"\n  score=0, outcome='Win', attempt=9  ->  new_score={new_score}  (clamped to min 10)")
    assert new_score == 10

def test_update_score_too_high_even_attempt_adds_points():
    new_score = update_score(100, "Too High", 2)
    print(f"\n  score=100, outcome='Too High', attempt=2 (even)  ->  new_score={new_score}")
    assert new_score == 105

def test_update_score_too_high_odd_attempt_deducts_points():
    new_score = update_score(100, "Too High", 3)
    print(f"\n  score=100, outcome='Too High', attempt=3 (odd)  ->  new_score={new_score}")
    assert new_score == 95

def test_update_score_too_low_deducts_points():
    new_score = update_score(100, "Too Low", 1)
    print(f"\n  score=100, outcome='Too Low', attempt=1  ->  new_score={new_score}")
    assert new_score == 95

def test_update_score_unknown_outcome_unchanged():
    new_score = update_score(100, "Unknown", 1)
    print(f"\n  score=100, outcome='Unknown', attempt=1  ->  new_score={new_score}")
    assert new_score == 100
