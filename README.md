# Password Generator with Tkinter GUI

A modern, user-friendly password generator built with Python and Tkinter. Generate secure passwords with customizable length and complexity.

## Features

- **Multiple Security Levels:**

  - Basic: Uppercase and lowercase letters
  - Medium: Letters and numbers
  - Strong: Letters, numbers, and special characters

- **Customizable Length:**

  - Choose password length from 8 to 32 characters
  - Smart generation ensures at least one character from each required set

- **User-Friendly Interface:**
  - Clean, modern GUI using ttk widgets
  - Copy to clipboard functionality
  - Visual feedback for actions
  - Cross-platform compatibility (Windows, macOS, Linux)

## Installation

1. Ensure Python 3.6+ is installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```
3. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install required packages:
   ```bash
   pip install pyperclip
   ```

## Usage

Run the program:

```bash
python PassGen.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Security Features

- Ensures password complexity based on selected strength
- Guarantees minimum character requirements:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number (Medium and Strong)
  - At least one special character (Strong)

## Requirements

- Python 3.6+
- tkinter (usually comes with Python)
- pyperclip

1. Select desired password strength
2. Choose password length using the spinbox
3. Click "Generate Password" to create a new password
4. Use "Copy to Clipboard" to copy the password
