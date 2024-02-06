from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *

def youtube_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.youtube.com")
    
def click_search_bar(context):
    search_bar = context.driver.find_element(By.XPATH,"//input[@id='search']")
    search_bar.click()
    
def input_into_search_bar(context):
    input_search_bar = context.driver.find_element(By.XPATH,"//input[@id='search']")
    input_search_bar.clear() #clear any existing text
    input_search_bar.send_keys("Nkateko Nkuna Vibes Playlist")
    input_search_bar.submit()
    
def click_playlist(context):
    playlist_displayed = context.driver.find_element(By.XPATH,"//*[@id='video-title']")
    playlist_displayed.click()
    
def validate_search_results(context,expected_outcome):
    search_outcome = context.driver.find_element(By.XPATH,"//*[@id='playlist-thumbnails']")
    final_outcome = search_outcome.text
    #unable to look through element so text
    #loop through results & return true if there is text else return false
    for outcome in final_outcome:
        if expected_outcome in outcome:
            return True
        else:
           return False    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # all_names = []

# def filter(name):
#  full_name = input("What is your name? ")+ name
#  print(full_name)
#  # def filter(name):
#     # fullname = input("What is your name? ") + name
#     # print(fullname)
    
# filter("")
 
# all_names.append(full_name)    
# print(all_names)
