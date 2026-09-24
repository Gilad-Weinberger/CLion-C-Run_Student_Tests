import json
import subprocess
import sys
import os
import glob
import shutil

# Force UTF-8 to support emojis in the Windows console
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.getcwd()
JSON_FILE = os.path.join(BASE_DIR, "student_tests.json")
BUILD_DIR = os.path.join(BASE_DIR, "cmake-build-debug")

def find_cmake():
    if shutil.which("cmake"):
        return "cmake"
    
    search_paths = [
        r"C:\Program Files\JetBrains\CLion*\bin\cmake\win*\*\bin\cmake.exe",
        os.path.expanduser(r"~\AppData\Local\JetBrains\Toolbox\apps\CLion\*\*\bin\cmake\win*\*\bin\cmake.exe"),
        os.path.expanduser(r"~\AppData\Local\Programs\CLion*\bin\cmake\win*\*\bin\cmake.exe")
    ]
    
    for pattern in search_paths:
        matches = glob.glob(pattern)
        if matches:
            return matches[-1]
            
    return None

def build_project():
    print("🔨 Building C project...")
    cmake_cmd = find_cmake()
    
    if not cmake_cmd:
        print("❌ Error: Could not find CMake on your system or inside CLion.")
        sys.exit(1)
        
    try:
        result = subprocess.run(
            [cmake_cmd, "--build", BUILD_DIR],
            cwd=BASE_DIR,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("❌ Build Failed! Compiler output:")
            print(result.stdout)
            print(result.stderr)
            sys.exit(1)
            
        print("✅ Build Successful!\n")
        
    except Exception as e:
        print(f"❌ Error running CMake: {e}")
        sys.exit(1)

def find_executable():
    executables = glob.glob(os.path.join(BUILD_DIR, "*.exe"))
    if not executables:
        print(f"Error: No .exe found in {BUILD_DIR} after building.")
        sys.exit(1)
    return executables[0]

def run_tests():
    build_project()
    executable = find_executable()

    try:
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {JSON_FILE} not found in {BASE_DIR}")
        sys.exit(1)

    tests = data.get('tests', [])
    passed = 0
    total = len(tests)

    for i, test in enumerate(tests):
        name = test.get('name', f'Test {i+1}')
        stdin_data = test.get('input', '')
        expected_output = test.get('output', '')

        print(f"Running {name}...")

        try:
            result = subprocess.run(
                [executable],
                input=stdin_data,
                text=True,
                capture_output=True,
                timeout=2
            )

            actual_output = result.stdout.strip()
            expected_output = expected_output.strip()

            if actual_output == expected_output:
                print("  ✅ Passed")
                passed += 1
            else:
                print("  ❌ Failed")
                print(f"  Expected: {repr(expected_output)}")
                print(f"  Got:      {repr(actual_output)}")

        except subprocess.TimeoutExpired:
            print("  ❌ Failed (Timeout - infinite loop detected)")

    print(f"\nResults: {passed}/{total} tests passed.")

if __name__ == "__main__":
    run_tests()
