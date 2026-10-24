@echo off
setlocal
cd /d "%~dp0"
echo Starting all Selenium practice tests...
python selenium_revision_main.py
if errorlevel 1 (
  echo.
  echo The Python run returned an error. Check the messages above.
)
echo.
echo When the run finishes, open selenium_test_report.html in this folder.
pause
