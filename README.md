# Hole em ALL

A quick casual arcade-style game built with Pygame. Move your mouse to grow a hole that "absorbs" all the red fruits on the field. Clear all fruits before time runs out to win.

## 🎮 Gameplay
- 30 fruits (red circles) are randomly scattered on a 800x600 field.
- Move the mouse: a black circular "hole" follows your cursor.
- Any fruit inside the hole disappears; each absorbed fruit increases:
  - Your score by 1
  - The hole radius by 1 (making it easier to get remaining fruits)
- Win: absorb all fruits before the time runs out.
- Lose: time threshold reached before all fruits are collected.
- After win or game over: press SPACE to restart.

## ✅ Current Features
- Simple one-file implementation (`game window.py`).
- Randomized fruit placement each round.
- Dynamic difficulty curve (hole grows as you succeed).
- Overlay end screen with WIN / GAME OVER messaging.
- Restart mechanic with spacebar.

## 🧠 Possible Improvements
These are not yet implemented but would make the game richer:
- Replace placeholder time logic (currently ends very quickly at 5 seconds due to `time_left <= 55` condition).
- Add sound effects for collecting fruits and winning.
- Add a main menu and difficulty settings (e.g., number of fruits, starting hole size, real timer duration).
- Track best time or high scores across sessions (save to a file).
- Add sprites instead of colored circles.
- Mobile/touch support.

## 🛠 Requirements
- Python 3.8+ (any modern version should work)
- Pygame (`pip install pygame`)

## 📦 Installation
```powershell
# Clone the repository
git clone https://github.com/vasu-devs/HoleEmAll.git
cd HoleEmAll/HoleEmAll

# (Optional) Create & activate a virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install pygame
```

## 🚀 Run the Game
```powershell
python "game window.py"
```

## 🎯 Controls
- Mouse: Move the hole.
- SPACE (after win/game over): Restart.
- Window close button: Quit.

## 🗂 Project Structure
```
HoleEmAll/
  game window.py    # Main game loop and logic
  README.md         # Project documentation
```

## ⚙️ Code Overview
The core loop handles:
- Event processing (quit / restart)
- Time tracking (`start_ticks`, `time_limit`)
- Collision detection via distance between cursor and fruit
- Growth mechanic (`hole_radius += 1` per collected fruit)
- State transitions: `PLAYING`, `WIN`, `GAME_OVER`

## 🔍 Known Quirks / Bugs
- The loss condition triggers when `time_left <= 55`, which effectively gives only ~5 seconds of play (time limit is set to 60). Adjusting this to a real countdown would improve playability.
- `final_time` is set but never used.
- Variable naming could be standardized (e.g., `game window.py` filename with space is unconventional — consider renaming to `game_window.py`).

## 📝 License
Add a license (e.g., MIT) to clarify usage—currently none present.

## 🤝 Contributing
Feel free to fork and submit pull requests for improvements (timing fix, assets, scoring persistence, refactoring, packaging, etc.).

## 📷 Screenshots
(You can add screenshots later; take a capture while playing and place it in a `assets/` or `docs/` folder.)

---
Enjoy the game! Suggestions welcome.
