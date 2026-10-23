# Beach House with Python Turtle

## Description

This project uses Python's `turtle` graphics library to draw a peaceful beach house scene.

The drawing includes a flat-roofed house with large windows and a wooden section, mountains, a sun, an ocean, a sandy beach, a small pond, stepping stones, and a tree.

The program demonstrates basic Python concepts, including:

- Using functions and parameters to reuse drawing code
- Using `for` loops and `range()` to repeat shapes and lines
- Positioning shapes with coordinates
- Drawing filled shapes, straight lines, and dots
- Using variables and arithmetic to space repeated details

## Code Overview

The program is organized into three functions:

- `draw_rectangle(t, x, y, width, height, colour)` – Draws a filled rectangle starting at its bottom-left corner. This is used for the house, windows, door, beach, ocean, and other rectangular features.
- `draw_mountain(t, x, y, colour)` – Draws a filled triangular mountain.
- `main()` – Sets up the screen and turtle, then draws the complete scene.

Loops repeat the wooden boards, windows, stepping stones, and waves. The background is drawn first so the house and smaller details appear in front of it.

## Example Output

![Beach house drawing](Final%20Drawing.png)

## How to Run

1. Clone or download this repository.
2. Make sure Python 3 is installed with Turtle/Tk support.
3. Open `DrawingProject.py` in your Python IDE, or open a terminal in the project folder and run:

   ```bash
   python DrawingProject.py
   ```

4. A Turtle graphics window will open and draw the scene.
5. Click anywhere in the drawing window to close it.
