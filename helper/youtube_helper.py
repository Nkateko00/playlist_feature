from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from xpath_paths import XPaths

#Xpaths here for now will fix
youtube_url = XPaths.youtube_url
input_search = XPaths.input_search
click_playlist = XPaths.click_playlist
click_song = XPaths.click_song
playing_song = XPaths.playing_song


class youtubeHelper:

    def youtube_homepage(context):
        context.driver = webdriver.Chrome()
        context.driver.implicitly_wait(10)
        #allow elements to be found on dom
        context.driver.get(youtube_url)
        
    def click_search_bar(context):
        search_bar = context.driver.find_element(By.XPATH,input_search)
        time.sleep(5) 
        search_bar.click()
        
    def input_into_search_bar(context,search):
        input_search_bar = context.driver.find_element(By.XPATH,input_search)
        input_search_bar.clear() #clear any existing text
        input_search_bar.send_keys(search)
        time.sleep(5) 
        input_search_bar.submit()
        
    def click_playlist(context):
        playlist_displayed = context.driver.find_element(By.XPATH,click_playlist)
        time.sleep(5) 
        playlist_displayed.click()
        
    def click_song(context):
        play_song = context.driver.find_element(By.XPATH,playing_song) 
        time.sleep(5) 
        #  //*[@id="video-title"] //*[@id="text"]
        play_song.click()
        time.sleep(15)
        # allow song to play for duration & quit driver

    def validate_search_results(context,expected_outcome):
        search_outcome = context.driver.find_element(By.XPATH,playing_song)
        time.sleep(5) 
        final_outcome = search_outcome.text
        #unable to loop through element so text
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
