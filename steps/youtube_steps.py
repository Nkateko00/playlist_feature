from behave import *
from helper.youtube_helper import youtubeHelper


youtuber_helper = youtubeHelper()

@given(u'I am on the Youtube homepage')
def step_impl(context):
   youtuber_helper.youtube_homepage()

@when(u'I "{search}" for the vibes playlist on search bar')
def step_impl(context,search):
    youtuber_helper.input_into_search_bar(search)

@then(u'I click  enter')
def step_impl(context):
    youtuber_helper.click_search_bar()

@then(u'I click on playlist to open')
def step_impl(context):
    youtuber_helper.click_playlist()

@then(u'I click on selected song')
def step_impl(context):
    youtuber_helper.click_song()

@then(u'I should get Vibes playlist displayed')
def step_impl(context):
   
    youtuber_helper.validate_search_results()

@given(u'I am on the youtube landing page')
def step_impl(context):
    youtuber_helper.youtube_homepage()


@when(u'I "{lookup}" Lex Fridmans podcast')
def step_impl(context,lookup):
    youtuber_helper.podcast_input(lookup)

@then(u'I click on the podcast to open')
def step_impl(context):
    youtuber_helper.click_podcast()


@then(u'I verify Episode 435 is playing on youtube')
def step_impl(context):
    youtuber_helper.verify_podcast_playing()
    
