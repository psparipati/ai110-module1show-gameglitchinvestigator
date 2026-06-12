# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - It looked very simple and dark, and I didn't take away from that simplicity.
- List at least two concrete bugs you noticed at the start  
  - The hints were mismatched.
  - The guess number wouldn't update.

### Bug Reproduction Log

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| Easy Mode Attempts | Give more than Medium Mode attempts. | Gave less than Medium Mode attempts. | Easy mode is not easy. |
| Relevant Logic Functions are not in ```logic_utils.py``` | Logic functions should be in ```logic_utils.py```. | Logic functions are in ```app.py``` | The console sometimes outputted an error because the functions were not implemented. |
| Secret number does not change. | Secret number changes when you start a game. | Secret number stayed the exact same. | The game does not function as intended. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Claude Sonnet.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI was able to catch the failed inputs for ```check_guess()```.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - The AI suggested changing the outputs of the funciton, and I had to double check it because it was changing the original text.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I played the game with the bug and without the bug, and I used that to decide whether the bug was fixed.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - I ran a test that made sure the bounds of the game difficulties were bounded properly.
- Did AI help you design or understand any tests? How?
  - I used Claude Code to look at how effective my tests were, then used it to design new tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit looks at what the latest save of the code looks like, and if it is different, it will ask to load a new session that follows the latest save of the code.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - Finding bugs on my own before turning to AI-based tools.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Verify that I code correctly, so that the AI doesn't end up rewriting my work.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project taught me where I could use my brain to find bugs, and where the AI could help me find bugs.
