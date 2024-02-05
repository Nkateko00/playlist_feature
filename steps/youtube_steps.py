from behave import *
from helper.youtube_helper import *


@given(u'I am on the Youtube homepage')
def step_impl(context):
    youtube_homepage(context)

@when(u'I search for the vibes playlist on search bar')
def step_impl(context):
    input_into_search_bar(context)

@then(u'I click  enter')
def step_impl(context):
    click_search_bar(context)


@then(u'I should get Vibes playlist displayed')
def step_impl(context):
    expected_outcome = "expected_outcome"
    validate_search_results(context,expected_outcome)


@then(u'I click on playlist to open')
def step_impl(context):
    click_playlist(context)