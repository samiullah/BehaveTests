from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
chrome_options = Options()
chrome_options.add_experimental_option('prefs',{
    'credentials_enable_service':False,
    'profile':{
        'password_manager_enabled':False
    }
})

def before_all(context):
    chrome_binary = 'chromedriver'
    context.browser = webdriver.Chrome(executable_path=chrome_binary, chrome_options=chrome_options)
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()
