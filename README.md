# 2048 Console Game — OOP Coursework Report

---

## 1. Introduction

### a. Application Overview

This project is a console-based implementation of the 2048 sliding tile puzzle game, developed in Python as coursework for the Object-Oriented Programming course at Vilnius Tech.

The game features customizable board sizes (4×4 up to 16×16), two difficulty modes (Easy and Hard), multiple user profiles, score tracking, and a persistent save/load system backed by JSON files.

### b. Running the Program

From the project root directory, run:

```bash
python main.py
```

### c. How to Play

| Key | Action |
|-----|--------|
| `W` | Move tiles Up |
| `A` | Move tiles Left |
| `S` | Move tiles Down |
| `D` | Move tiles Right |
| `Q` | Quit and save progress |

The game accepts real-time keyboard input — no Enter key required. On startup, the player selects a board size and difficulty mode. Each player profile tracks its own best score across sessions.

---

## 2. Body / Analysis

### a. Implementation of Functional Requirements

The program is built around a clean object-oriented architecture. All major functionality is encapsulated in dedicated classes with well-defined responsibilities.

#### Core Classes

| Class | Responsibility |
|-------|----------------|
| `Game` | Orchestrates overall game flow; composes `Board`, `User`, `SaveManager`, and `Difficulty` |
| `Board` | Manages the 2D grid, tile movement, merging logic, and win/loss detection |
| `Difficulty` | Abstract base class defining a shared interface for difficulty modes |
| `EasyMode` / `HardMode` | Concrete subclasses with mode-specific tile generation behaviour |
| `DifficultyFactory` | Creates the appropriate `Difficulty` object via the Factory Method pattern |
| `User` | Manages player profiles and best scores |
| `SaveManager` | Handles reading and writing best score to JSON file |
| `InputHandler` | Captures real-time keyboard input |

#### OOP Principles Applied

**Encapsulation** — `Board` stores its state in private attributes (`__grid`, `__score`, etc.), exposing data only through controlled methods.

**Inheritance** — `EasyMode` and `HardMode` both extend the abstract `Difficulty` base class, sharing a common interface while differing in behaviour.

**Polymorphism** — The `get_new_tile_value()` method is overridden in each difficulty subclass, allowing the game engine to call it uniformly regardless of the active mode.

**Abstraction** — The `Difficulty` class defines a contract that all difficulty implementations must follow, hiding internal details from the rest of the system.

**Composition** — The `Game` class assembles complex behaviour by combining smaller, independent components rather than inheriting from them.

#### Design Pattern

The **Factory Method** pattern is implemented in `DifficultyFactory`, which instantiates the correct difficulty object based on user input. This decouples the game logic from concrete difficulty classes, making it straightforward to add new modes in the future.

#### Testing

The project includes a full suite of unit tests using Python's built-in `unittest` framework, covering board logic, tile movement, difficulty selection, and save/load operations. All tests pass.

---

## 3. Results and Summary

### a. Results

The application is fully functional and satisfies all specified requirements:

- Smooth tile sliding and merging mechanics
- Correct Easy and Hard difficulty behaviour
- Real-time W/A/S/D controls
- Working save and load system via JSON
- Multiple user profiles with persistent best-score tracking
- All unit tests pass

### b. Conclusions

This project demonstrates the practical application of core OOP principles in Python. The modular design, proper use of the Factory Method pattern, and clear separation of concerns produce code that is both maintainable and easy to extend. The implementation reflects a solid understanding of encapsulation, inheritance, polymorphism, abstraction, and composition.

### c. Possible Extensions

The application could be extended in several directions:

- **Advanced Save & Load system** — Allow players to save the current board state and continue later
- **GUI** — Add a graphical interface using Pygame or Tkinter
- **Undo** — Implement a move-history stack to support undoing moves
- **Leaderboard** — Introduce a global or online high-score system
- **New mechanics** — Add special tile types or power-ups
- **More difficulty levels** — Expand beyond Easy and Hard
- **Statistics & achievements** — Track player milestones over time
- **AI solver** — Develop an automated agent to play the game

---

## 4. References

- [Python 3 Documentation](https://docs.python.org/3/)
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- Original 2048 game by Gabriele Cirulli
- OOP and design patterns best practices
