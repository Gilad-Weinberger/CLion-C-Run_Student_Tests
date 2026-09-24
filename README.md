# CLion Run_Student_Tests for C

A lightweight, automated test runner for C assignments in CLion. This tool automatically locates CLion's internal CMake compiler, builds your current project, and validates your executable's output against a suite of JSON-defined test cases.

## Features
* **Zero-Configuration Build:** Automatically finds and runs CLion's bundled CMake. 
* **Global Integration:** Designed to be set up once as a CLion External Tool and used across all future assignments.
* **Timeout Protection:** Detects infinite loops (`scanf` waiting endlessly) and safely terminates the test.
* **Whitespace Resiliency:** Strips trailing whitespace and newlines before comparison to prevent formatting-based failures.

## 1. Setup (One-Time Only)

To make this script universally available for all your C projects in CLion:

1. Clone or download this repository to a permanent location on your machine (e.g., `C:\scripts\clion-c-autograder`).
2. Open CLion and go to **File > Settings > Tools > External Tools**.
3. Click the `+` icon to add a new tool:
   * **Name:** `Run Autograder`
   * **Program:** `python` *(or the absolute path to your python.exe)*
   * **Arguments:** `"C:\absolute\path\to\run_student_tests.py"`
   * **Working directory:** `$ProjectFileDir$`
4. Click **OK** to save.

### 1.1 Optional: Create a Keyboard Shortcut
To make testing even faster, you can map this tool to a keyboard shortcut:
1. Go to **File > Settings > Keymap**.
2. In the search box at the top, type `Run Student Tests`.
3. Right-click the tool in the search results and select **Add Keyboard Shortcut**.
4. Press your desired key combination (e.g., `Ctrl + Alt + T` or `Shift + F10`, Whatever is not used on you computer) and click **OK**.

## 2. Usage Per Project

For each new assignment or project:

1. Write your C code in CLion.
2. Place a `student_tests.json` file in the root of your project directory (the same level as `main.c`).
3. To test your code, simply click **Tools > External Tools > Run Autograder** from the top menu.

The script will automatically compile your C code, execute it with the inputs defined in your JSON file, and output the results directly in the CLion console.

## 3. JSON Test Format

Create a `student_tests.json` file structured like this:

```json
{
  "tests": [
    {
      "name": "Test 1: Normal execution",
      "input": "0 55 0 100\n",
      "output": "0 appears 2 times\n55 appears 1 times\n100 appears 1 times"
    },
    {
      "name": "Test 2: Edge case",
      "input": "0 0 0\n",
      "output": "0 appears 3 times"
    }
    
  ]
}
