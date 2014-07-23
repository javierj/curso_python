from behave import *

@given('we have behave installed')
def impl(context):
    pass

@when('we implement a test')
def impl(context):
    assert True is not False

@then('behave will test it for us!')
def impl(context):
    assert context.failed is False