from behave import given, when, then
from framework.webapp import webapp


@given(u'I load the website')
def step_impl_load_website(context):
    webapp.load_website()


@when(u'I go to "{page}" page')
def step_impl_goto_page(context, page):
    webapp.goto_page(page)

@then(u'Title "{page}" is visible')
def step_impl_verify_title(context, page):
    webapp.verify_title_exists(page)

@then(u'I see this component "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_exists(component)

@then(u'Close the browser')
def step_impl_close_browser(context):
    webapp.tear_down()

