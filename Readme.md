# Calculator Application

## Calculator Screenshot
(You can add a screenshot of your calculator here)

## Overview
This is a simple yet fully functional Calculator Application built using Python and the `tkinter` library. It provides a graphical user interface (GUI) for performing basic arithmetic operations such as addition, subtraction, multiplication, and division. The application is designed to be user-friendly, with a clean and intuitive layout.

## Features
- **Basic Arithmetic Operations:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Decimal Support:** Allows input of decimal numbers for precise calculations.
- **Error Handling:** Displays an "Error" message for invalid expressions or operations.
- **Clear Functionality:** Includes a `C` button to clear the current input or result.
- **Responsive Design:** The calculator is designed with a fixed window size and a visually appealing layout.
- **Keyboard-Friendly:** Users can input numbers and operators using the GUI buttons.

## Installation
To run this calculator application, you need to have Python installed on your system. Follow these steps to set up and run the project:

### Clone the Repository:
```bash
git clone https://github.com/Geetavarshiny/calculator-app.git
cd calculator-app
```

### Install Dependencies:
This project uses the `tkinter` library, which is included with Python by default. No additional installation is required.

### Run the Application:
Execute the Python script to launch the calculator:
```bash
python calculator.py
```

## Usage

### Interface Layout
The calculator interface consists of the following components:
- **Display Screen:** Shows the current input or result.
- **Number Buttons (0-9):** For entering numeric values.
- **Operator Buttons (`+`, `-`, `*`, `/`):** For performing arithmetic operations.
- **Decimal Button (`.`):** For entering decimal numbers.
- **Clear Button (`C`):** Clears the current input or result.
- **Equal Button (`=`):** Computes the result of the expression.

### How to Use
1. **Enter Numbers:** Click the number buttons (`0-9`) to input numeric values.
2. **Enter Operators:** Click the operator buttons (`+`, `-`, `*`, `/`) to perform arithmetic operations.
3. **Decimal Input:** Use the `.` button to input decimal numbers.
4. **Clear Input:** Press the `C` button to clear the current input or result.
5. **Compute Result:** Press the `=` button to evaluate the expression and display the result.

## Functions

### 1. `get_data(value)`
**Purpose:** Appends the clicked button's value to the input string.

**Parameters:**
- `value`: The value (number or operator) to be appended.

**Behavior:**
- Updates the global `data` variable with the new value.
- Displays the updated input on the calculator screen.

### 2. `equal_data()`
**Purpose:** Evaluates the expression entered by the user.

**Behavior:**
- Uses Python's `eval()` function to compute the result of the expression.
- Displays the result on the calculator screen.
- If an error occurs (e.g., invalid expression), it displays "Error".
- Clears the input data after evaluation.

### 3. `clear()`
**Purpose:** Clears the current input or result.

**Behavior:**
- Resets the global `data` variable to an empty string.
- Clears the calculator screen.

## Code Structure

The project is structured as follows:

- **Main Window:** The `Tk()` object represents the main application window.
- **Global Variables:**
  - `data`: Stores the current input string.
  - `var`: A `StringVar` object linked to the display screen for dynamic updates.
- **Buttons:**
  - Number buttons (`0-9`), operator buttons (`+`, `-`, `*`, `/`), and special buttons (`.`, `C`, `=`).
- **Layout:**
  - The calculator layout is organized into rows and columns using the `place()` geometry manager.

## Example
Here's an example of how to use the calculator:

**Input:** `5 + 3 * 2`

Press `=` to compute the result.

**Output:** `11`

## Contributing
Contributions are welcome! If you'd like to improve this project, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## Acknowledgments
- Built with Python and `tkinter`.
- Inspired by simple and intuitive calculator designs.

## Contact
For questions or feedback, feel free to reach out:

- **Email:** geetavarshiny24@gmail.com
