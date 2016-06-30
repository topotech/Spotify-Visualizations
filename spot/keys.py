import spotipy
import spotipy.util as util
import os, ast

#Spotify API keys
scope = "playlist-read-private"
uir = "http://localhost:8888"
username = "rino21111"

spotify_keys = os.environ["SPOTIFY_KEYS"]

spotify_keys = ast.literal_eval(spotify_keys)


#set up access
def get_access():
  for key in spotify_keys:
    try:
      token = util.prompt_for_user_token(username, scope, key["uid"], key["usec"], uir)
      return spotipy.Spotify(auth=token)
    except:
      continue