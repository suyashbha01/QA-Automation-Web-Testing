
# QA Automation Testing Projects

A collection of web automation testing projects using **Python, Selenium WebDriver, and Pytest**. This repository demonstrates my practice with browser automation, login testing, test execution, and test organization.

## Projects

### 1. SauceDemo Testing

Website: https://www.saucedemo.com/

Folder: `SauceDemo-Testing/`

This project contains automated tests for the SauceDemo demo e-commerce website.

**Files:**
- `conftest2.py` — Shared Pytest fixtures for the SauceDemo tests.
- `test_login.py` — Login test cases.
- `test_main_website.py` — Website testing scenarios.
- `test_saucedemo_login.py` — SauceDemo login automation tests.

### 2. The Internet Website Testing

Website: https://the-internet.herokuapp.com/login

Folder: `the-internet.herokuapp Web Testing/`

This project contains practice scripts for browser automation and web testing.

**Files include:**
- `conftest.py` — WebDriver fixture and failure screenshot handling.
- `website_automation_testing.py` — Website automation practice.
- `website_testing_practice.py` — Website testing practice scenarios.
- `Run_All_Selenium_Tests.bat` — Windows batch file for running the configured tests.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- HTML test reporting with `pytest-html`
- Git and GitHub
- Visual Studio Code

## Prerequisites

Install Python and Google Chrome, then install the required Python packages:

```bash
pip install selenium pytest pytest-html
```

## Running the Tests

Open a terminal in the project root.

To run the SauceDemo tests:

```bash
python -m pytest SauceDemo-Testing/ -v
```

To run The Internet website tests:

```bash
python -m pytest "the-internet.herokuapp Web Testing/" -v
```

**Note:** Test filenames must follow Pytest's discovery conventions, such as `test_*.py`. Files used as practice scripts may need to be run individually or renamed to match these conventions. Test execution also depends on the fixtures and imports used by each test.

## Test Reports and Screenshots

The project includes configuration for capturing screenshots when tests fail and generating HTML reports where configured. Generated reports and screenshots are excluded from Git using `.gitignore`.

## Learning Goals

- Practice Selenium WebDriver automation.
- Understand Pytest fixtures and test execution.
- Automate login and web UI scenarios.
- Practice failure screenshots and test reporting.
- Organize automation projects using Git and GitHub.

## Author

**Suyash Bhargava**

GitHub: https://github.com/suyashbha01

---

*This repository is a learning and practice portfolio for QA automation testing.*