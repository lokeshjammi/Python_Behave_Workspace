import os
import time
from os.path import abspath, join

from jproperties import Properties

root_path = abspath(os.path.dirname(__file__))
file_path = join(root_path, '../Properties/')
#fileName = "config.properties"
def fetch_values_from_properties(key, file):
    global fileName
    configs = Properties()
    fileName = file
    try:
        with open(file_path+fileName, 'rb') as read_prop:
            configs.load(read_prop)
            url = configs.get(key).data
            return url
    except Exception as e:
        print('Error while opening the file')

def launch_browser(context, url):
    context.browser.get(url)
    time.sleep(10)