# ThoughtfulAI Package Sorting Challenge

## Problem Statement

Imagine you work in Thoughtful’s robotic automation factory. Your task is to write a function that directs packages into one of three stacks — **STANDARD**, **SPECIAL**, or **REJECTED** — based on their volume and mass.

### Rules

- A package is **bulky** if its volume (width × height × length) is **at least 1,000,000 cm³** or if any single dimension is **150 cm or more**.
- A package is **heavy** if its mass is **20 kg or more**.
- Packages that are **both bulky and heavy** are **REJECTED**.
- Packages that are **either bulky or heavy (but not both)** are **SPECIAL**.
- Packages that are **neither bulky nor heavy** are **STANDARD**.

The function `sort(width, height, length, mass)` returns the correct stack name as a string.

## Solution Overview

This repository contains a Python implementation of the sorting function along with test cases that cover normal and edge scenarios to ensure correctness.

## Getting Started

### Prerequisites

- Python 3.10 or higher

### Running the Code

1. Clone the repository:

   ```bash
   git clone
   cd thoughtfulai-fde-challenge
2. Run the tests:
    python main.py

Testing
The main.py file includes a run_tests() function with predefined test cases. You can extend this to add more tests if needed.
