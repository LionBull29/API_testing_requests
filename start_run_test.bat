@echo off

rem Create a virtual environment named "venv".
python -m venv venv

rem Activate the virtual environment (Windows).  Adjust as needed for your shell.
call venv\Scripts\activate.bat

rem Install the project's dependencies from the "requirements.txt" file.
pip install -r requirements.txt

rem Run pytest to execute the tests and generate an HTML report.
rem Replace "path/filename.html" with the desired path and filename for the report.
pytest --html=path/filename.html

rem Deactivate the virtual environment.
deactivate

echo.
echo Tests complete.  Check the HTML report at: path/filename.html (or your specified path)
echo.
pause