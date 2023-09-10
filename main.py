# """
# OPTIFINE AUTOINSTALLER:
# preconditions:
# minecraft is updated to the desired version(??)/latest version(??). java edition
# take all versions and compile into selector?? (figure out how to do this)
# steps this will enact:
# 1) get a string of the desired version/update (format: x.x.x or x.x, x can be any number of any length, will probably
# separate into list) (if i only download latest version i can read from website until i stumpble on first download link)
# 2) download link is the same format in all places EXCEPT for the version number, link can easily be concatenated
# 3) get python to open download link hopefully this makes it appear in downloads folder
# 4) open with java


# NEW CODE
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

"""
OPTIFINE AUTOINSTALLER:
preconditions:
minecraft is updated to the desired version(??)/latest version(??). java edition
take all versions and compile into selector?? (figure out how to do this)
steps this will enact:
1) get a string of the desired version/update (format: x.x.x or x.x, x can be any number of any length, will probably
separate into list) (if i only download latest version i can read from website until i stumpble on first download link)
2) download link is the same format in all places EXCEPT for the version number, link can easily be concatenated
3) get python to open download link hopefully this makes it appear in downloads folder
4) open with java
"""
url = "https://optifine.net/downloads"
"""
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
"""


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


page = requests.get(url)
source_text = page.text
# assigns variable to page's html text
start_location = source_text.find("http://optifine")
# the first instance of this leads to the download link to the latest version of optifine, this leads to a second page
end_location = source_text.find("\"", start_location)
download_link = source_text[start_location:end_location]
# finds the first instance of the quotation mark after the start location, the start and end locations encapsulate the
# download link

chrome_options = Options()
chrome_options.add_argument('--headless')

chrome_options.set_preference('C:\\', 2)
chrome_options.set_preference('browser.download.manager.showWhenStarting', False)
chrome_options.set_preference('browser.download.dir', '/tmp')
chrome_options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
driver = webdriver.Chrome(options=chrome_options)

driver.get(download_link)
time.sleep(20)
clickable = driver.find_element(By.ID, "Download")
clickable.click()

time.sleep(20)

driver.quit()
