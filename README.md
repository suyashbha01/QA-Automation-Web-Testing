QA Automation Testing Projects
A portfolio of web UI automation projects built with Python, Selenium WebDriver, and Pytest. This repository contains practice projects for browser automation, login flows, e-commerce workflows, test organization, waits, assertions, and reporting.
Projects
1. SauceDemo Web Testing
- Website: https://www.saucedemo.com/
- Folder: SauceDemo-Testing/
- Main test file: test_main_website.py
Automated coverage includes:
- Products page and sorting options
- Adding products to the cart, including random product selection
- Removing products from the cart
- Checkout flow and checkout information validation
- Sidebar menu and its Lazy Load, Spinner, and Slider options
- Closing the sidebar and using the All Items and About links
- Reset App State and logout
Main files:
- conftest.py — Shared WebDriver fixture and failure-screenshot handling
- test_main_website.py — Main SauceDemo UI scenarios
- test_saucedemo_login.py — Additional login automation tests
The main SauceDemo test file was run locally with 14 passing tests.
2. The Internet Website Testing
- Website: https://the-internet.herokuapp.com/login
- Folder: the-internet.herokuapp Web Testing/
This folder contains Selenium practice scripts for different pages and interactions on The Internet sample website.

Files include:
- conftest.py — WebDriver fixture for this project
- test_login.py — Login test
- Dropdown Page.py — Dropdown interaction practice
- Website_Automaction_Testing_Pratice.py — Website automation practice
- Website_Testing_Main.py — Additional testing scenarios
- Run_All_Selenium_Tests.bat — Windows batch file for running configured tests
Some practice scripts do not start with test_, so Pytest will not automatically collect them by default. Run them individually when appropriate or rename them and their test functions to follow Pytest's discovery conventions.
Technologies
- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Git and GitHub
- Visual Studio Code
- Google Chrome
Prerequisites and Installation
Install Python and Google Chrome, clone this repository, and open a terminal in the repository root.

Install the Python packages:
python -m pip install selenium pytest pytest-html
Running the Tests
Run the main SauceDemo test suite:
python -m pytest "SauceDemo-Testing/test_main_website.py" -v
Run only Test Case 9 (sidebar menu):
python -m pytest "SauceDemo-Testing/test_main_website.py" -v -m testcase9
Run all tests that Pytest discovers in the SauceDemo folder:
python -m pytest "SauceDemo-Testing/" -v
Run the tests discovered in The Internet project folder:
python -m pytest "the-internet.herokuapp Web Testing/" -v
Run a practice script that is not collected by Pytest using Python directly. For example:
python "the-internet.herokuapp Web Testing/Dropdown Page.py"
Run commands from the repository root so Pytest can find the root pytest.ini configuration.
HTML Reports and Failure Screenshots
Generate a self-contained HTML report for the main SauceDemo suite:
python -m pytest "SauceDemo-Testing/test_main_website.py" -v --html=reports/saucedemo-report.html --self-contained-html
The report will be saved to reports/saucedemo-report.html. Create the reports folder first if it does not exist.

The SauceDemo WebDriver fixture saves a screenshot when a test fails. Screenshots are stored under screenshots/ when configured by the fixture.

Avoid committing virtual environments, caches, temporary files, or generated reports unless you intentionally want to publish them.
Learning Goals
- Practise Selenium locators, browser interactions, explicit waits, and assertions.
- Organize tests with Pytest fixtures and markers.
- Automate login, shopping-cart, checkout, and navigation scenarios.
- Capture failure screenshots and generate HTML reports.
- Manage and document automation projects using Git and GitHub.
Author
Suyash Bhargava
- GitHub: https://github.com/suyashbha01
This repository is a learning and practice portfolio for QA automation testing.
