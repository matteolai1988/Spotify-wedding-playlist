#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install python-dotenv


# In[3]:


#pip install spotipy


# In[4]:


import csv
import os
import re

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials


# In[15]:


CLIENT_ID = "XXX"
CLIENT_SECRET = "XXX"
OUTPUT_FILE_NAME = "track_info.csv"
PLAYLIST_LINK = "https://open.spotify.com/playlist/26F8B0jWC2kMkw5hXFmW2g?si=6a54a91bb7cd42b3"


# In[16]:


# authenticate
client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)

# create spotify session object
session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# In[17]:


# get uri from https link
if match := re.match("https://open.spotify.com/playlist/(.*)\?", PLAYLIST_LINK):
    playlist_uri = match.groups()[0]
else:
    raise ValueError("Expected format: https://open.spotify.com/playlist/...")


# In[18]:


# get list of tracks in a given playlist (note: max playlist length 100)
tracks = session.playlist_tracks(playlist_uri)["items"]


# In[19]:


# create csv file
with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # write header column names
    writer.writerow(["track", "artist"])

    # extract name and artist
    for track in tracks:
        name = track["track"]["name"]
        artists = ", ".join(
            [artist["name"] for artist in track["track"]["artists"]]
        )

        # write to csv
        writer.writerow([name, artists])


# In[ ]:




