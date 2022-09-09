from behave import given, when, then

from src.resource.CommonUtilities.CommonOperations import fetch_values_from_properties, launch_browser


@given('lauch browser and open the "{url}"')
def launch_browser_and_open_url(context, url):
    if url.startswith('properties'):
        print('Method starts')
        url = url.split('properties.')[1]
        url = fetch_values_from_properties(url, "config.properties")
        launch_browser(context, url)

@when('proper user details are entered')
def step_impl(context):
    pass


@then('Click on Submit button and check the homepage')
def step_impl(context):
    pass


@then('Close the browser')
def step_impl(context):
    pass