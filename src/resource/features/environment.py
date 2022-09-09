import os
from os.path import abspath, join

from selenium import webdriver

project_root = abspath(os.path.dirname(__file__))
driver_bin = join(project_root, '../DriverExecutables/Windows/Edge/msedgedriver.exe')
def before_scenario(context, feature):
    if 'UI' in feature.tags:
        context.browser = webdriver.Edge(executable_path=driver_bin)
        context.browser.maximize_window()

def after_scenario(context, feature):
    if 'UI' in feature.tags:
        print('This comes after feature')