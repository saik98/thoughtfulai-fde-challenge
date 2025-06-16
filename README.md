# thoughtfulai-fde-challenge
Python solution for Thoughtful AI's FDE technical screen, package classification logic based on size and weight.
# Thoughtful AI - Package Sorting Challenge

## Overview
This is a Python challenge I completed for Thoughtful AI. The goal was to create a function that sorts packages in a robotic factory based on their size and weight.

## The Problem
A package is:

- **Bulky** if its volume is 1,000,000 cm³ or more, or if any dimension is 150 cm or larger.
- **Heavy** if its mass is 20 kg or more.

The sorting rules are:
- `"STANDARD"` if the package is neither bulky nor heavy.
- `"SPECIAL"` if the package is bulky or heavy (but not both).
- `"REJECTED"` if the package is both bulky and heavy.

## My Solution

I implemented a function `sort(width, height, length, mass)` that returns the correct category as a string. The code avoids ternary operators (per the instructions) and includes test cases covering various scenarios, including edge cases.

## How to Run

Run the script with:
```bash
python main.py
