# QA Automation Testing Projects

A collection of web automation testing projects using **Python, Selenium WebDriver, and Pytest**. This repository demonstrates my practice with browser automation, login testing, test execution, and test organization.

## Projects

### 1. SauceDemo Testing

**Website:** [SauceDemo](https://www.saucedemo.com/)

**Folder:** `SauceDemo-Testing/`

This project contains automated tests for the SauceDemo demo e-commerce website.

**Files:**

- `conftest.py` — Shared Pytest fixtures for the SauceDemo tests.
- `test_main_website.py` — Website testing scenarios, including product sorting, cart operations, checkout, and sidebar functionality.
- `test_saucedemo_login.py` — SauceDemo login automation tests.
- `pytest.ini` — Pytest markers and configuration.

The main SauceDemo test file has been run locally with **14 passing tests**.

### 2. The Internet Website Testing

**Website:** [The Internet — Login Page](https://the-internet.herokuapp.com/login)

**Folder:** `the-internet.herokuapp Web Testing/`

This project contains practice scripts for browser automation and web testing.

**Files include:**

- `conftest.py` — WebDriver fixture and failure screenshot handling.
- `test_login.py` — Login test case.
- `Dropdown Page.py` — Dropdown interaction practice.
- `Website_Automaction_Testing_Pratice.py` — Website automation practice.
- `Website_Testing_Main.py` — Website testing scenarios.
- `Run_All_Selenium_Tests.bat` — Windows batch file for running the configured tests.

Some practice scripts may need to be run individually if their filenames do not follow Pytest's test-discovery conventions.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- HTML test reporting with `pytest-html`
- Git and GitHub
- Visual Studio Code
- Google Chrome

## Prerequisites

Install Python and Google Chrome, then install the required Python packages:

```bash
python -m pip install selenium pytest pytest-html
```

## Running the Tests

Open a terminal in the repository root.

To run the SauceDemo main test file:

```bash
python -m pytest "SauceDemo-Testing/test_main_website.py" -v
```

To run all tests discovered in the SauceDemo folder:

```bash
python -m pytest "SauceDemo-Testing/" -v
```

To run The Internet website tests:

```bash
python -m pytest "the-internet.herokuapp Web Testing/" -v
```

**Note:** Test filenames should follow Pytest's discovery conventions, such as `test_*.py`, and test functions should start with `test_`. Practice scripts may need to be run individually or renamed to match these conventions.

## Test Reports and Screenshots

Generate a self-contained HTML report for the SauceDemo main test file:

```bash
python -m pytest "SauceDemo-Testing/test_main_website.py" -v --html=reports/saucedemo-report.html --self-contained-html
```

Create the `reports` folder first if it does not exist. Generated reports and screenshots should generally be excluded from Git using `.gitignore`, unless you intentionally want to publish them.

## Learning Goals

- Practice Selenium WebDriver automation.
- Understand Pytest fixtures and test execution.
- Automate login and web UI scenarios.
- Practice failure screenshots and test reporting.
- Organize automation projects using Git and GitHub.

## Author

**Suyash Bhargava**

GitHub: [suyashbha01](https://github.com/suyashbha01)

---

*This repository is a learning and practice portfolio for QA automation testing.*