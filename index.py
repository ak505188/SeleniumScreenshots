from selenium import webdriver
from selenium.webdriver.common.keys import Keys

default_width = 1024
default_height= 768

sizes = [
    [320, 240],
    [640, 480],
    [1024, 768],
    [1440, 900],
    [1920, 1080],
    [2560, 1440],
    [3840, 2160]
]

base_url = "https://www.leapsandrebounds.com/"

url_extensions = [
  "",
  "products/bungee-rebounders-mini-trampoline",
  "products/stability-bar",
  "products/bungees-for-leaps-rebounds",
  "pages/faqs",
  "pages/community",
  "cart"
]

firefox = webdriver.Firefox()

for dimensions in sizes:
  firefox.set_window_size(dimensions[0], dimensions[1])
  for extension in url_extensions:
    firefox.get(base_url + extension)

    file_name = "./screenshots/firefox/" + extension + "_" + str(dimensions[0]) + "x" + str(dimensions[1]) + ".png"

    element=firefox.find_element_by_tag_name('body')
    element_png = element.screenshot_as_png
    with open(file_name, "wb") as file:
      file.write(element_png)

firefox.close()

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

    file_name = "./screenshots/chrome/" + extension + "_" + str(dimensions[0]) + "x" + str(dimensions[1]) + ".png"

    chrome.get_screenshot_as_file(file_name)

chrome.close()
