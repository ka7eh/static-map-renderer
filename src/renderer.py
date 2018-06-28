import base64
import json
import os
import tempfile
import time
import uuid

from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

WORK_DIR = './'
TMP_DIR = '/tmp'


def generate_map(config):
    width = config.pop('width', '800')
    height = config.pop('height', '600')

    # start the virtual display
    display = Display(visible=0, size=(width, height))
    display.start()

    # configure firefox profile to automatically save png files in the current directory
    fp = webdriver.FirefoxProfile()
    fp.set_preference('browser.download.folderList', 2)
    fp.set_preference('browser.download.manager.showWhenStarting', False)
    fp.set_preference('browser.download.dir', TMP_DIR)
    fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'octet/stream')

    browser = webdriver.Firefox(firefox_profile=fp)

    with open('index.html', 'r') as f:
        html = f.read()

    image = None
    try:
        html_fd, html_path = tempfile.mkstemp(suffix='.html', dir=WORK_DIR)
        image_name = str(uuid.uuid4())
        config['image_name'] = image_name

        with open(html_path, 'w') as f:
            f.write(
                html % {
                    'WD': os.getcwd(),
                    'WIDTH': width,
                    'HEIGHT': height,
                    'CONFIG': json.dumps(config)
                }
            )
        os.close(html_fd)

        browser.get('file://{}'.format(html_path))

        delay = 5
        tries = 10
        success = False

        while True:
            try:
                WebDriverWait(browser, delay).until(
                    EC.presence_of_element_located((By.ID, 'DownloadAnchor')))
                success = True
                break
            except TimeoutException:
                if tries == 0:
                    break
                tries -= 1

        tries = 10
        while success:
            try:
                with open(os.path.join(TMP_DIR, '{}.png'.format(image_name)), 'rb') as f:
                    image = f.read()
                break
            except FileNotFoundError:
                if tries == 0:
                    break
                tries -= 1
                time.sleep(2)

        # quit the browser
        browser.quit()

        # stop the display
        display.stop()

        return image
    finally:
        os.remove(html_path)
        return image
