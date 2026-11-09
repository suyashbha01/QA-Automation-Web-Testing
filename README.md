# QA Automation Testing Projects

A collection of web automation testing projects built using **Python, Selenium WebDriver, and Pytest**. This repository showcases my hands-on practice with web UI automation, test case execution, reusable fixtures, failure screenshots, HTML reports, and CI/CD using GitHub Actions.

## Projects

### 1. SauceDemo Web Testing

**Website:** [SauceDemo](https://www.saucedemo.com/)  
**Project Folder:** `SauceDemo-Testing/`

Automated testing of the SauceDemo demo e-commerce website.

**Test Coverage**
- Login functionality
- Product inventory validation
- Product sorting
- Cart operations
- Checkout functionality
- Sidebar navigation

**Project Files**
- `conftest.py` — Shared Pytest fixtures, browser setup, and failure screenshot handling.
- `test_main_website.py` — Main website automation scenarios.
- `test_saucedemo_login.py` — Login automation tests.
- `pytest.ini` — Pytest configuration and markers.

**Latest Local Test Result — Main Test File**

| Metric | Result |
|---|---:|
| Total Tests | 14 |
| Passed | 14 |
| Failed | 0 |
| Execution Time | Approximately 1 minute 12 seconds |

### 2. The Internet Website Testing

**Website:** [The Internet — Login Page](https://the-internet.herokuapp.com/login)  
**Project Folder:** `the-internet.herokuapp Web Testing/`

A collection of practice scripts for browser automation and web testing.

**Project Files**
- `conftest.py` — WebDriver fixture and failure screenshot handling.
- `test_login.py` — Login test case.
- `Dropdown Page.py` — Dropdown interaction practice.
- `Website_Automaction_Testing_Pratice.py` — Website automation practice.
- `Website_Testing_Main.py` — Website testing scenarios.
- `Run_All_Selenium_Tests.bat` — Windows batch file for running configured tests.

Some practice scripts may need to be run individually if they do not follow Pytest's test-discovery conventions.

## Technologies & Tools

- **Language:** Python
- **Automation:** Selenium WebDriver
- **Test Framework:** Pytest
- **Reporting:** pytest-html
- **CI/CD:** GitHub Actions
- **Version Control:** Git and GitHub
- **IDE:** Visual Studio Code
- **Browser:** Google Chrome

## Getting Started

### Prerequisites

Install:
- Python
- Google Chrome
- Git
- Visual Studio Code

### Install Dependencies

Open the terminal in the repository root and run:

```bash
python -m pip install selenium pytest pytest-html
```

## Running Tests

### Run SauceDemo Main Test File

```bash
python -m pytest "SauceDemo-Testing/test_main_website.py" -v
```

### Run All Tests Discovered in SauceDemo Folder

```bash
python -m pytest "SauceDemo-Testing/" -v
```

### Run The Internet Website Tests

```bash
python -m pytest "the-internet.herokuapp Web Testing/" -v
```

**Note:** Pytest discovers test files using names such as `test_*.py` and test functions starting with `test_`. Practice scripts that do not follow these conventions may need to be run individually.

## HTML Test Reports & Screenshots

Generate a self-contained HTML report:

```bash
python -m pytest "SauceDemo-Testing/test_main_website.py" -v --html=reports/saucedemo-report.html --self-contained-html
```

Create the `reports` folder first if it does not exist.

The test setup also captures screenshots when tests fail. Generated reports and screenshots should generally be excluded from Git using `.gitignore`, unless they are intentionally being published.

## GitHub Actions — Continuous Integration

The SauceDemo test suite is configured to run through GitHub Actions.

The workflow supports:
- Execution on pushes to `main`
- Execution on pull requests to `main`
- Manual workflow execution
- HTML test report artifact upload
- Failure screenshot artifact upload

This helps validate automated tests in a CI environment.

## Learning Objectives

- Practice Selenium WebDriver automation.
- Understand Pytest fixtures and test execution.
- Automate web UI scenarios.
- Implement failure screenshot handling.
- Generate HTML test reports.
- Run automation tests using GitHub Actions.
- Organize testing projects using Git and GitHub.

## Author

**Suyash Bhargava**

[GitHub Profile](https://github.com/suyashbha01)

[Project Repository](https://github.com/suyashbha01/QA-Automation-Web-Testing)

---

*This repository is a learning and practice portfolio for QA Automation Testing.*
