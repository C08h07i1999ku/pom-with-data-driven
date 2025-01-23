import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key



def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Specify the browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsuported browser")
    driver.maximize_window()
    return driver

# ********************* This part is for editing the html report **********************

# Hook for adding environment info in html report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Soul website automation'
    config.stash[metadata_key]['QA Name'] = 'Chinmaya Kumar Nayak'

# Hook for modify or delete environment info in html report
@pytest.mark.optionalbook
def pytest_metadata(metadata):
    metadata.pop('Plugins',None)
