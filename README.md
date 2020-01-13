
Pre-Requsites to Python Install
1) Install Python 3.8
2)pip install py
3) pip install pytest-ordering
4) pip install pytest-html
5) pip install selenium

Selenium Drivers:
1)Copy all the Selenium drivers (ChromeDriver, geckodriver, IEDriverServer) to the local drive say "C:\selenium\drivers"
2) Goto	MyComputer->Properties->Advanced System Settings
3) Click on	Environmental Variable
4) In system Variable, select the Path and click Edit
5) Enter the above path location say "C:\selenium\drivers"
6) Click OK and restart the system

Steps to Run the script:
1) Copy the scripts to the client system
2) Navigate to the Copied folder->tests
3) Launch Terminal or command prompt
4) Navigate to the directory using cd command say "E:\Experiment\herokupapp\tests"
5) Enter the command "py.test .\test_suite_demo.py --html Report01.html

Example:
PS E:\Experiment\herokupapp\tests> py.test .\test_suite_demo.py --html Report01.html
==================================================================== test session starts ====================================================================
platform win32 -- Python 3.8.1, pytest-5.3.2, py-1.8.1, pluggy-0.13.1
rootdir: E:\Experiment\herokupapp\tests
plugins: html-2.0.1, metadata-1.8.0, ordering-0.6
collected 3 items

test_suite_demo.py ... [100%]

----------------------------------------- generated html file: file://E:\Experiment\herokupapp\tests\Report01.html ------------------------------------------
==================================================================== 3 passed in 31.01s =====================================================================

Verify the results:
1) Report01.html to verify the number of tests executed, pass or fail
2) For Investigation look into the "automation.log"
3) Screenshots are copied to the screenshot folder for failed case
