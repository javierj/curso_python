__author__ = 'Javier'

# Según la documentación, no funciona en Python 3

from splinter import Browser
import os

os.environ["PATH"] += os.pathsep + "C:\code\workspaces\Python\_miscelanea\Selenium"

with Browser('chrome') as browser:
     # Visit URL
     url = "http://www.google.com"
     browser.visit(url)
     browser.fill('q', 'splinter - python acceptance testing for web applications')
     # Find and click the 'search' button
     button = browser.find_by_name('btnG')
     # Interact with elements
     button.click()
     if browser.is_text_present('splinter.cobrateam.info'):
         print("Yes, the official website was found!")
     else:
         print("No, it wasn't found... We need to improve our SEO techniques")