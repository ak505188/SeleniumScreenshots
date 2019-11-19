from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import os

default_width = 1024
default_height= 768

enabled = {
    'firefox': True,
    'chrome': True
}

sizes = [
    [320, 240],
    [640, 480],
    [1024, 768],
    [1440, 900],
    [1920, 1080],
    [2560, 1440]
]

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

# Website url
# ex: https://leapsandrebounds.com
base_url = "https://leapsandrebounds.com"
hostname = urllib.parse.urlparse(base_url).hostname

# Add url extensions here
# ex: /products/jump-pack
url_extensions = [
  "",
  "/products/jump-pack"
]

if enabled['firefox']:
  firefox = webdriver.Firefox()
  for dimensions in sizes:
    firefox.set_window_size(dimensions[0], dimensions[1])
    for extension in url_extensions:
      firefox.get(base_url + extension)

      dir = "./screenshots/firefox/"
      ensure_dir(dir)
      file_name = dir + hostname + extension.replace("/", ".") + "_" + str(dimensions[0]) + "x" + str(dimensions[1]) + ".png"

      print("Screenshoting:", file_name)

      element=firefox.find_element_by_tag_name('body')
      element_png = element.screenshot_as_png

      with open(file_name, "wb") as file:
        file.write(element_png)
  firefox.close()


if enabled['chrome']:
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--disable-extensions')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-gpu')
  chrome_options.add_argument('--hide-scrollbars')

  chrome = webdriver.Chrome(chrome_options=chrome_options)

  for dimensions in sizes:
    for extension in url_extensions:
      # Get body height
      chrome.set_window_size(dimensions[0], dimensions[1])
      chrome.get(base_url + extension)
      page_height = chrome.find_element_by_tag_name('body').size['height']

      chrome.set_window_size(dimensions[0], page_height)

      dir = "./screenshots/chrome/"
      ensure_dir(dir)
      file_name = dir + hostname + extension.replace("/", ".") + "_" + str(dimensions[0]) + ".png"

      print("Screenshoting:", file_name)

      chrome.get_screenshot_as_file(file_name)

  chrome.close()
