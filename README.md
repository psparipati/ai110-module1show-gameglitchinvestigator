# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [✅] Describe the game's purpose.
- [✅] Detail which bugs you found.
- [✅] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Pick a difficulty (Easy: 11 attempts, Medium: 8 attempts, Hard: 5 attempts).
2. Click ```New Game``` to generate a number to guess.
3. From now on, just play until you get the number.
   * If you get the number, balloons will fly from the screen to congratulate you (like below).
   * If you overshot the number, you will get a message saying "📉 Go LOWER!".
   * If you undershoot the number, you will get a message saying "📈 Go HIGHER!"

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```bash
============================= test session starts =============================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\pspar\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\pspar\VSCode\Projects\Codepath\AI110\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collecting ... collected 21 items

tests/test_game_logic.py::test_difficulty_easy 
  input='Easy'  ->  range=(1, 20)
PASSED
tests/test_game_logic.py::test_difficulty_normal 
  input='Normal'  ->  range=(1, 100)
PASSED
tests/test_game_logic.py::test_difficulty_hard 
  input='Hard'  ->  range=(1, 50)
PASSED
tests/test_game_logic.py::test_difficulty_unknown_defaults_to_normal_range 
  input='Unknown'  ->  range=(1, 100)
PASSED
tests/test_game_logic.py::test_parse_guess_valid_integer 
  input='42'  ->  ok=True, value=42, err=None
PASSED
tests/test_game_logic.py::test_parse_guess_valid_float_truncates 
  input='3.9'  ->  ok=True, value=3, err=None
PASSED
tests/test_game_logic.py::test_parse_guess_none_returns_error 
  input=None  ->  ok=False, value=None, err='Enter a guess.'
PASSED
tests/test_game_logic.py::test_parse_guess_empty_string_returns_error 
  input=''  ->  ok=False, value=None, err='Enter a guess.'
PASSED
tests/test_game_logic.py::test_parse_guess_non_numeric_returns_error 
  input='abc'  ->  ok=False, value=None, err='That is not a number.'
PASSED
tests/test_game_logic.py::test_parse_guess_negative_number 
  input='-5'  ->  ok=True, value=-5, err=None
PASSED
tests/test_game_logic.py::test_check_guess_correct 
  guess=50, secret=50  ->  outcome='Win', message='? Correct!'
PASSED
tests/test_game_logic.py::test_check_guess_too_high 
  guess=60, secret=50  ->  outcome='Too High', message='? Go LOWER!'
PASSED
tests/test_game_logic.py::test_check_guess_too_low 
  guess=40, secret=50  ->  outcome='Too Low', message='? Go HIGHER!'
PASSED
tests/test_game_logic.py::test_check_guess_secret_as_string 
  guess=50, secret='50' (str)  ->  outcome='Win', message='? Correct!'
PASSED
tests/test_game_logic.py::test_check_guess_returns_message_string 
  guess=50, secret=50  ->  message type=str, value='? Correct!'
PASSED
tests/test_game_logic.py::test_update_score_win_early 
  score=0, outcome='Win', attempt=1  ->  new_score=80
PASSED
tests/test_game_logic.py::test_update_score_win_clamps_to_minimum 
  score=0, outcome='Win', attempt=9  ->  new_score=10  (clamped to min 10)
PASSED
tests/test_game_logic.py::test_update_score_too_high_even_attempt_adds_points 
  score=100, outcome='Too High', attempt=2 (even)  ->  new_score=105
PASSED
tests/test_game_logic.py::test_update_score_too_high_odd_attempt_deducts_points 
  score=100, outcome='Too High', attempt=3 (odd)  ->  new_score=95
PASSED
tests/test_game_logic.py::test_update_score_too_low_deducts_points 
  score=100, outcome='Too Low', attempt=1  ->  new_score=95
PASSED
tests/test_game_logic.py::test_update_score_unknown_outcome_unchanged 
  score=100, outcome='Unknown', attempt=1  ->  new_score=100
PASSED

============================= 21 passed in 0.09s ==============================
```