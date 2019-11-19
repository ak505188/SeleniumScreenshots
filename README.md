# Selenium Screenshot Tool
Take full page screenshots of a specified webpage using Selenium.
Window widths are specified in the python script.

### Supported Browsers
  * Chrome Headless
  * Firefox

### Dependencies
  1. Selenium
  2. Python 3
  3. Chrome Headless
  4. Firefox
  5. Geckodriver (for Firefox)
  
### Installation
  1. Install dependecies.
  2. Clone this repo and `cd` into repo.
  3. (Optional) Set up a python virtualenv for python dependencies.
     `pyvenv .` or `python -m venv`
  4. (Optional) Activate virtualenv `. bin/activate`.
  5. Install python dependencies. `pip install -r requirements.txt`
  6. Run script. `python index.py`
  7. (Optional) When done using tool deacivate using `deactivate`

### Usage Information
Base url, url extensions, and window sizes are stored in `index.py`. Window
height is auto-adjusted and irrelevant. If you want to disable screenshots for
one of the browsers change it's value in `enabled` dict in `index.py` to `False`.

For simpler use run `./run`. This will activate the virtualenv, run the script,
and deactivate the virtualenv when done.
