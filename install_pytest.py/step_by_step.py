"""
==========================================================
         Python Selenium Automation Installer
==========================================================

This script installs all required Python packages for
Selenium Automation Framework.

Packages Installed
------------------
1. pytest
2. selenium
3. webdriver-manager
4. pytest-html

Usage
-----
python3 install.py

Author : Manjunath
==========================================================
"""

import subprocess
import sys


def run_command(command, description):
    """Runs a terminal command and prints a description."""
    print("\n" + "=" * 70)
    print(description)
    print("=" * 70)
    print(f"Executing Command:\n{command}\n")
    subprocess.call(command, shell=True)


print("\n")
print("=" * 70)
print("PYTHON AUTOMATION FRAMEWORK INSTALLATION")
print("=" * 70)

# -------------------------------------------------------
# STEP 0
# -------------------------------------------------------

print("""
STEP 0 : Verify Python & pip Installation
""")

run_command("python3 --version", "Checking Python Version")
run_command("pip3 --version", "Checking pip Version")

# -------------------------------------------------------
# STEP 1
# -------------------------------------------------------

print("""
STEP 1 : Install PyTest

PyTest is one of the most popular, powerful,
and widely used automation testing frameworks in Python.

Command:
pip3 install pytest
""")

run_command(
    "pip3 install pytest",
    "Installing PyTest"
)

print("""
Upgrade Command

pip3 install -U pytest

The '-U' or '--upgrade' option upgrades PyTest
to the latest available version.
""")

run_command(
    "pip3 install -U pytest",
    "Upgrading PyTest"
)

print("""
Verify Installed Version
""")

run_command(
    "python3 -m pytest --version",
    "Checking PyTest Version"
)

# -------------------------------------------------------
# STEP 2
# -------------------------------------------------------

print("""
STEP 2 : Install Selenium

Selenium is used for browser automation.
""")

run_command(
    "pip3 install selenium",
    "Installing Selenium"
)

# -------------------------------------------------------
# STEP 3
# -------------------------------------------------------

print("""
STEP 3 : Install WebDriver Manager

Automatically downloads the appropriate browser driver.
""")

run_command(
    "pip3 install webdriver-manager",
    "Installing WebDriver Manager"
)

# -------------------------------------------------------
# STEP 4
# -------------------------------------------------------

print("""
STEP 4 : Install PyTest HTML

Used for generating HTML execution reports.
""")

run_command(
    "pip3 install pytest-html",
    "Installing PyTest HTML"
)

# -------------------------------------------------------
# STEP 5
# -------------------------------------------------------

print("""
STEP 5 : Install PyTest xdist

PyTest xdist enables parallel test execution by
running multiple test cases simultaneously using
multiple CPU cores.

Benefits
--------
• Faster test execution
• Reduced regression testing time
• Supports distributed test execution
• Improves CI/CD pipeline performance

Install Command

pip3 install pytest-xdist

Upgrade Command

pip3 install -U pytest-xdist

Verify Installation

pip3 show pytest-xdist

Example Usage

Run tests using 2 CPU cores

python3 -m pytest -n 2

Run tests using 4 CPU cores

python3 -m pytest -n 4

Automatically use all available CPU cores

python3 -m pytest -n auto

Run tests in parallel with HTML Report

python3 -m pytest -n auto --html=Reports/report.html

Run tests in parallel with Verbose Output

python3 -m pytest -n auto -v -s
""")

run_command(
    "pip3 install pytest-xdist",
    "Installing PyTest xdist"
)

run_command(
    "pip3 show pytest-xdist",
    "PyTest xdist Information"
)

# -------------------------------------------------------
# VERIFY
# -------------------------------------------------------

print("""
Checking Installed Packages
""")

run_command(
    "pip3 show pytest",
    "PyTest Information"
)

run_command(
    "pip3 show selenium",
    "Selenium Information"
)

run_command(
    "pip3 show webdriver-manager",
    "WebDriver Manager Information"
)

run_command(
    "pip3 show pytest-html",
    "PyTest HTML Information"
)

# -------------------------------------------------------
# NOTES
# -------------------------------------------------------

print("""
==========================================================
                INSTALLATION COMPLETED
==========================================================

==========================================================
                Useful PyTest Commands
==========================================================

1. Run All Test Files
---------------------
Executes every test file in your current project.

Command:
python3 -m pytest


2. Run a Specific Test File
---------------------------
Executes only the specified test file.

Command:
python3 -m pytest test_login.py


3. Run a Specific Test Method
-----------------------------
Executes only a single test function from a test file.

Command:
python3 -m pytest test_login.py::test_login


4. Run Tests with Verbose Output
--------------------------------
Displays detailed information about each executed test.

Command:
python3 -m pytest -v


5. Display print() Statements
-----------------------------
Shows the output of print() statements in the terminal.

Command:
python3 -m pytest -s


6. Run Tests with Verbose Output + Console Logs
-----------------------------------------------
Displays detailed execution information along with print() statements.

Command:
python3 -m pytest -v -s


7. Stop Execution on First Failure
----------------------------------
Stops the test execution immediately after the first failed test.

Command:
python3 -m pytest -x


8. Re-run Only Failed Tests
---------------------------
Executes only the tests that failed in the previous run.

Command:
python3 -m pytest --lf


9. Generate an HTML Test Report
-------------------------------
Creates a professional HTML report after test execution.

Command:
python3 -m pytest --html=Reports/report.html


10. Generate HTML Report with Console Output
--------------------------------------------
Creates an HTML report while displaying detailed execution logs.

Command:
python3 -m pytest -v -s --html=Reports/report.html


11. Generate a Self-Contained HTML Report
-----------------------------------------
Embeds CSS, JavaScript, and images into a single HTML file.

Command:
python3 -m pytest --html=Reports/report.html --self-contained-html


12. Execute Tests by Marker
---------------------------
Runs only tests marked with a specific marker.

Command:
python3 -m pytest -m smoke

Example:
@pytest.mark.smoke


13. Execute Tests by Keyword
----------------------------
Runs tests whose names contain a specific keyword.

Command:
python3 -m pytest -k login


14. Show Available Markers
--------------------------
Lists all custom markers defined in the project.

Command:
python3 -m pytest --markers


15. Display Test Collection Only
--------------------------------
Shows all discovered tests without executing them.

Command:
python3 -m pytest --collect-only


16. Export Installed Packages
-----------------------------
Creates a requirements.txt file containing all installed packages.

Command:
pip3 freeze > requirements.txt


17. Install Packages from requirements.txt
------------------------------------------
Installs all packages listed in the requirements file.

Command:
pip3 install -r requirements.txt


18. List All Installed Packages
-------------------------------
Displays all installed Python packages.

Command:
pip3 list


19. Show Package Information
----------------------------
Displays detailed information about an installed package.

Command:
pip3 show pytest

pip3 show selenium

pip3 show webdriver-manager

pip3 show pytest-html


20. Check PyTest Version
------------------------
Displays the installed version of PyTest.

Command:
python3 -m pytest --version


==========================================================
                 Quick Reference
==========================================================

Run All Tests
python3 -m pytest

Run Single Test File
python3 -m pytest test_login.py

Verbose Execution
python3 -m pytest -v

Display print() Statements
python3 -m pytest -s

Verbose + Print Output
python3 -m pytest -v -s

Generate HTML Report
python3 -m pytest --html=Reports/report.html

Run Smoke Tests
python3 -m pytest -m smoke

Run Login Tests
python3 -m pytest -k login

Stop on First Failure
python3 -m pytest -x

Re-run Failed Tests
python3 -m pytest --lf

==========================================================
Python Automation Environment is Ready!
Happy Automation Testing!
==========================================================
""")