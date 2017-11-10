import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from behave import *
from selenium.webdriver.support.ui import Select


@given('I open insurance website')
def step_impl(context):
   context.browser.get("http://demo.borland.com/InsuranceWebExtJS/index.jsf")
   context.browser.implicitly_wait(5)

@then('I print the title')
def step_impl(context):
   title = context.browser.title
   assert "InsuranceWeb: Home" in title

@then('I click on  the Signup Button')
def step_impl(context):
   signup = context.browser.find_element_by_name("login-form:signup")
   signup.click()

@then('I wait for "{seconds}" seconds')
def step(context,seconds):
    wait_time = int(seconds)
    time.sleep(wait_time)

@then('I wait for the element with xpath "{locator}"')
def step(context,locator):
    wait = WebDriverWait(context.browser, 120, poll_frequency=1,
                         ignored_exceptions=[NoSuchElementException,
                                             ElementNotVisibleException])
    element = wait.until(EC.presence_of_element_located((By.XPATH,locator)))

@then('I enter the firstname as "{field_value}"')
def step(context,field_value):
    element = context.browser.find_element(By.XPATH,"//input[@id='signup:fname']")
    element.send_keys(field_value)

@then('I enter the lastname as "{field_value}"')
def step(context,field_value):
    element = context.browser.find_element(By.XPATH,"//input[@id='signup:lname']")
    element.send_keys(field_value)


use_step_matcher("re")

@then("I fill the signup form  with values")
def step_impl(context):
    context.browser.find_element_by_name("signup:fname").send_keys("Tom")
    context.browser.find_element_by_name("signup:lname").send_keys("hicks")
    context.browser.find_element_by_id('BirthDate').send_keys("07/11/1990")
    context.browser.find_element_by_id('signup:email').send_keys("abc11122sss2@mailinator.com")
    context.browser.find_element_by_id('signup:street').send_keys("street 90 abcplace")
    context.browser.find_element_by_id('signup:city').send_keys("newcity")
    state_select = Select(context.browser.find_element_by_id('signup:state'))
    state_select.options[1].click()
    context.browser.find_element_by_id('signup:zip').send_keys("9999")
    context.browser.find_element_by_id('signup:password').send_keys("123456")

@when('I click on  the Submit Button')
def step_impl(context):
   signup_button = context.browser.find_element_by_id("signup:signup")
   signup_button.click()

@then('I should see continue button')
def step_impl(context):
    if context.browser.find_elements_by_id('signup:continue'):
        pass


@when(u'I log in as "registeredUser"')
def step_impl(context):
    username_field = context.browser.find_element_by_id('login-form:email')
    password_field = context.browser.find_element_by_id('login-form:')
    username_field.send_keys('registeredUser')
    password_field.send_keys('1234')
    submit_button = context.browser.find_element_by_id('submit')
    submit_button.click()

@when(u'I log in as "unregisteredUser"')
def step_impl(context):
    username_field = context.browser.find_element_by_id('username')
    password_field = context.browser.find_element_by_id('password')
    username_field.send_keys('unregisteredUser')
    password_field.send_keys('1234')
    submit_button = context.browser.find_element_by_id('submit')
    submit_button.click()

@then(u'I should see the message {auth_message}')
def imple(context, auth_message):
    message = context.browser.find_element_by_id('auth-message')
    assert message.text == auth_message
