import logging
import requests
import csv
import os
import random

## Log file parameters##
#logFile = 'C:\\devops\\private\\assignments\\mobili\\log.log'
logFile = '/output/output.log'
logging.basicConfig(filename=logFile,filemode='a',format='%(asctime)s - %(levelname)s - %(message)s' , level=logging.INFO)

## File output parameter
query_id = str(random.randint(1,1000))
csv_file_output_path = '/output/song-list_'+query_id+'.csv'
csv_file_header = ['song name', 'performer name', 'album name', 'song share URL']

## musicmatach site parameters
musicmatch_api_key = "56054d5d1fcf530ceca835218b071ec5"
musicmatch_base_url = "https://api.musixmatch.com/ws/1.1/track.search?"

song_word_search= os.getenv("word_search") or "car"
song_language = "en"
song_release_date_max = "20100101"

def respone_status(response):
    if response.status_code == 200:
        logging.info("Starting to search")
    elif response.status_code == 401:
        logging.error("Authentication failed - Please validate your API key")
    elif response.status_code == 402:
        logging.error("You have reached your daily request limit - please try again tomorrow")
    elif response.status_code == 403:
        logging.error("You are not authorized to perform this operation")
    elif response.status_code == 404:
        logging.error("The requested resource was not found")
    elif response.status_code == 405:
        logging.error("The requested method was not found")
    else:
        logging.error("Opppss - server side error")

def number_of_songs(number_matched_songs):
    if number_matched_songs == 0:
        logging.info("The query returned 0 results ")
        exit()
    elif number_matched_songs == 10000:
        logging.info("Number of songs that match the query are at least 10,000")
    else:
        logging.info("Number of songs that match the query: " + str(number_matched_songs))

with open(csv_file_output_path,'w', encoding='utf-8',newline='') as csv_file:
    url_request_path = musicmatch_base_url + "&q_lyrics=" + song_word_search + "&f_lyrics_language=" + song_language + "&f_track_release_group_first_release_date_max=" + song_release_date_max +"&apikey=" + musicmatch_api_key
    response = requests.get(url=url_request_path)
    logging.info("Running query ID: " + query_id)
    logging.info ("request url: "  + url_request_path )
    respone_status(response)
    number_matched_songs = response.json()["message"]["header"]["available"]
    number_of_songs(number_matched_songs)
    response_json_filter = response.json()["message"]["body"]["track_list"]
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_file_header)
    for song in response_json_filter:
        song_name = song["track"]["track_name"]
        performer_name = song["track"]["artist_name"]
        album_name = song["track"]["album_name"]
        song_share_URL = song["track"]["track_share_url"]
        csv_writer.writerow([song_name, performer_name, album_name, song_share_URL])