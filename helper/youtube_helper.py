from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from xpath_paths import XPaths
import sqlite3

#Xpaths here for now will fix
youtube_url = XPaths.youtube_url
input_search = XPaths.input_search
click_playlist = XPaths.click_playlist
click_song = XPaths.click_song
playing_song = XPaths.playing_song
lex_podcast = XPaths.lex_podcast
podcast_title = XPaths.podcast_heading


class youtubeHelper:

    def youtube_homepage(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #allow elements to be found on dom
        self.driver.get(youtube_url)
        
    def db_connection(self):
        db_file = 'test_data.db'
        db_connect = sqlite3.connect(db_file)
        cursor = db_connect.cursor()
        
        cursor.execute("SELECT * FROM inputs")
        test_data = cursor.fetchall()
        all_rows = []
        #create empty array to store data returned from for loop
        for row in test_data:
            all_rows.append(row)
        return all_rows
        
        
    def click_search_bar(self):
        search_bar = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,input_search)))
        search_bar.click()
        
    def input_into_search_bar(self,search):  
        db_data = self.db_connection()
        search_data = db_data[0][1]
        input_search_bar = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH, input_search))
        )
        input_search_bar.clear()
        input_search_bar.send_keys(search_data)
        input_search_bar.submit()
        
    def podcast_input(self,lookup):
        db_data = self.db_connection()
        search_data = db_data[1][1]
        input_podcast = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,input_search)))
        input_podcast.clear()
        input_podcast.send_keys(search_data)
        input_podcast.submit()
        
    def click_podcast(self):
        open_podcast = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,lex_podcast))
        )
        open_podcast.click()
        time.sleep(50)
        
    def click_playlist(self):
        playlist_displayed = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,click_playlist))
        )
        playlist_displayed.click()
        
    def click_song(self):
        play_song = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,playing_song))
        )
        play_song.click()
        time.sleep(50)
        # allow song to play for duration & quit driver

    def validate_search_results(self):
        search_outcome = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,playing_song))
        )
        if search_outcome:
                return True
        else:
               return False  
           
    def verify_podcast_playing(self):
        podcast_playing = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,podcast_title))
        )
        if podcast_playing:
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
