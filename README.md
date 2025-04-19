# GoIT Algo HW 03

This repository contains solutions for Homework #3 of the GoIT Algorithms course. It includes:

- `homework_3-1.py`: Recursively scans a source directory, classifies files by extension, and copies them into corresponding subdirectories under a destination folder.
- `homework_3-2.py`: Draws a Koch snowflake fractal using Python's `turtle` module, with an interactive prompt for recursion depth.

## Requirements

- Python 3.6 or higher
- For `homework_3-2.py`: the standard `turtle` module (included in the Python standard library).

## Installation

```bash
git clone https://github.com/<your-username>/go-it-algo-hw-03.git
cd go-it-algo-hw-03
```

## Usage

### homework_3-1.py

```bash
python3 homework_3-1.py source_dir [destination_dir]
```

- `source_dir`: Path to the directory to scan.
- `destination_dir`: (Optional) Base directory for copied files (defaults to `dist`).

The script creates subfolders named by file extension (e.g., `txt`, `py`) inside the destination and copies each file accordingly.

### homework_3-2.py

```bash
python3 homework_3-2.py
```

When prompted, enter the recursion level (e.g., `2`). A window will open and draw the Koch snowflake fractal.

## File Descriptions

- **homework_3-1.py**

  - Checks if the destination exists; creates it if necessary.
  - Recursively iterates through `source_dir`, classifying files by extension and copying them.
  - Handles errors gracefully with a try/except block.

- **homework_3-2.py**
  - `koch_snowflake(t, order, size)`: Recursively draws one side of the snowflake.
  - The `main()` function initializes the Turtle screen, prompts for recursion level, and draws a three-sided fractal.

## Customization

- **homework_3-1.py**: Modify the classification logic to group by file size, date, or other metadata.
- **homework_3-2.py**: Change the `size` or default `order` for different fractal scales, or adjust the turtle’s color and speed.
