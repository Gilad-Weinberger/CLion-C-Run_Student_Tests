# CLion C Run_Student_Tests Tool

A lightweight, automated test runner for C assignments in CLion. This tool was specifically designed for Technion students to bypass the tedious loop of repeatedly uploading files to GradeScope just to run basic tests. It automatically locates CLion's internal CMake compiler, builds your current project, and validates your executable's output against a suite of JSON-defined test cases locally.

## Features
* **GradeScope Workflow Bypass:** Test your code instantly on your own machine without waiting for GradeScope server queues or manually uploading `main.c` after every minor change.
* **Zero-Configuration Build:** Automatically finds and runs CLion's bundled CMake. 
* **Global Integration:** Designed to be set up once as a CLion External Tool and used across all future assignments (like CS Intro 02340114).
* **Timeout Protection:** Detects infinite loops (`scanf` waiting endlessly) and safely terminates the test.
* **Whitespace Resiliency:** Strips trailing whitespace and newlines before comparison to prevent formatting-based failures.

## 1. Setup (One-Time Only)

You only need one copy of the Python script on your machine. It does not need to be inside your C project folders. 

1. Save `run_student_tests.py` anywhere on your computer (e.g., `C:\scripts\run_student_tests.py` or inside a dedicated GitHub repository folder).
2. Open CLion and go to **File > Settings > Tools > External Tools**.
3. Click the `+` icon to add a new tool:
   * **Name:** `Run Student Tests`
   * **Program:** `python` *(or the absolute path to your python.exe)*
   * **Arguments:** `"C:\absolute\path\to\your\run_student_tests.py"` *(Make sure this matches exactly where you saved the file in Step 1, enclosed in quotes)*
   * **Working directory:** `$ProjectFileDir$`
4. Click **OK** to save.

### Optional: Create a Keyboard Shortcut
To make testing even faster, you can map this tool to a keyboard shortcut:
1. Go to **File > Settings > Keymap**.
2. In the search box at the top, type `Run Student Tests`.
3. Right-click the tool in the search results and select **Add Keyboard Shortcut**.
4. Press your desired key combination (e.g., `Ctrl + Alt + T` or `Shift + F10`) and click **OK**.

## 2. Usage Per Project

For each new assignment or project:

1. Write your C code in CLion.
2. Place a `student_tests.json` file in the root of your project directory (the same level as `main.c`).
3. To test your code, simply click **Tools > External Tools > Run Student Tests** from the top menu, or use your custom keyboard shortcut.

The script will automatically compile your C code, execute it with the inputs defined in your JSON file, and output the results directly in the CLion console. Once all tests pass locally, you only need to upload to GradeScope once for your final submission.

## 3. JSON Test Format & Example

### If your `main.c` looks like this:
```c
#include <stdio.h>

int main() {
    int a, b;
    if (scanf("%d %d", &a, &b) == 2) {
        printf("Result: %d\n", a + b);
    }
    return 0;
}
```

### Then your `student_tests.json` should look like this:
```json
{
  "tests": [
    {
      "name": "Test 1: Simple Addition",
      "input": "1 2\n",
      "output": "Result: 3"
    },
    {
      "name": "Test 2: Negative Numbers",
      "input": "-5 10\n",
      "output": "Result: 5"
    }
  ]
}
```
