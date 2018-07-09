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
    renderer = config.pop('renderer', 'leaflet')
    output_format = config.pop('format', 'byte')
    width = config.pop('width')
    height = config.pop('height')

    display = Display(visible=0, size=(width, height))
    display.start()

    fp = webdriver.FirefoxProfile()
    fp.set_preference('browser.download.folderList', 2)
    fp.set_preference('browser.download.manager.showWhenStarting', False)
    fp.set_preference('browser.download.dir', TMP_DIR)
    fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'octet/stream')

    browser = webdriver.Firefox(firefox_profile=fp)
    dx, dy = browser.execute_script(
        'let w=window; return [w.outerWidth - w.innerWidth, w.outerHeight - w.innerHeight];'
    )
    browser.set_window_size(width + dx, height + dy)

    with open('{}.html'.format(renderer), 'r') as f:
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

        delay = 10
        tries = 3

        while True:
            try:
                
                WebDriverWait(browser, delay).until(
                    EC.presence_of_element_located((By.ID, 'Ready'))
                )
                screenshot = browser.get_screenshot_as_base64()
                if output_format == 'byte':
                    image = base64.b64decode(screenshot)
                elif output_format == 'base64':
                    image = bytes(screenshot, 'ascii')
                break
            except TimeoutException:
                if tries == 0:
                    break
                tries -= 1

        browser.quit()

        display.stop()

        return image
    finally:
        os.remove(html_path)
        return image
