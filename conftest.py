import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None

def load_config(file):
    global target
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    if target is None:
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    webadmin_config = load_config(request.config.getoption("--target"))['webadmin']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['base_url'])
    fixture.session.login(username=webadmin_config['username'], password=webadmin_config['password'])
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")






