#  Catch the Diamonds — OpenGL Game in Python

A 2D arcade-style game built using **Python** and **PyOpenGL**, where the player controls a catcher to collect falling diamonds.  
The game includes real-time animation, collision detection, score tracking, pause/play control, and an optional auto-play (cheat) mode.

---

##  Gameplay Overview

- Diamonds fall from the top of the screen at increasing speed  
- Move the catcher left/right to catch diamonds  
- Each successful catch increases the score and difficulty  
- Missing a diamond ends the game  
- UI controls allow pause, restart, and exit  
- Cheat Mode 
---

##  Features

-  **Real-time collision detection**
-  **Midpoint Line Algorithm (MPL)** for drawing shapes
-  **Play / Pause** functionality
-  **Restart game** option
-  **Auto-play (Cheat Mode)** using keyboard toggle
-  **Dynamic difficulty scaling**
-  Randomized diamond colors
-  Mouse & Keyboard interaction

---

##  Controls

### Keyboard
- **⬅ Left Arrow** → Move catcher left  
- **➡ Right Arrow** → Move catcher right  
- **`c` key** → Toggle auto-play (cheat mode)

### Mouse
- **Play / Pause Button** → Pause or resume the game  
- **Restart Button (←)** → Restart the game  
- **Exit Button (✕)** → Exit and print final score

---

## ▶️ How to Run

### 1️⃣ Install Dependencies
Make sure Python 3.9+ is installed.


```bash
pip install PyOpenGL PyOpenGL_accelerate
python catchTheDiamond.py
```
## Tested Environment

- Python: 3.9+

- OS: Windows / Linux

- Graphics: OpenGL 2.0+

- Libraries: PyOpenGL, GLUT

  
## Technical Highlights

- Custom implementation of:

  - Zone-based line drawing

  - Midpoint Line Algorithm (MPL)

- Manual viewport & orthographic projection setup

- Game loop using glutIdleFunc

- Bounding box collision detection

- Modular function design for rendering & logic

## Author

### Mejbah Uddin Bhuiyan
 BSc in Computer Science & Engineering  
 BRAC University  

## Aspiring Software Engineer | Graphics & Game Programming Enthusiast

