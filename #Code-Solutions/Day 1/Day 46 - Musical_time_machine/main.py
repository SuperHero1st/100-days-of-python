import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD ")
songs_website = requests.get(f'https://www.billboard.com/charts/hot-100/{date}').text
soup = BeautifulSoup(songs_website, 'html.parser')
songs = soup.select('li h3#title-of-a-story.c-title')

songs_list = [" ".join(song.get_text().split()) for song in songs]

spotify_id = 'b5e33db1331f4b3cab8a65704eb1d8ae'
spotify_key = '9f59ae71229747ee86ae0c6628fddae7'
redirect_url = 'http://example.com'
scope = "playlist-modify-public playlist-modify-private"


# Get the authorization URL to authorize the app
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_id, client_secret=spotify_key, redirect_uri=redirect_url, scope=scope))
user_id = sp.current_user()['id']


# Extracting the tracks URLs

track_urls = []
year = date.split("-")[0]

for song in songs_list:
    results = sp.search(f'track:{song} year:{year}', type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_name = track['name']
        track_url = track['external_urls']['spotify']
        track_urls.append(track_url)
    else:
        print(f"{song} doesn't exist in Spotify. Skipped.")

track_ids = [url.split("/")[-1] for url in track_urls]
playlist_id = sp.user_playlist_create(user= user_id, name=f'{date} Billboard 100' , public=True, collaborative=False, description='')['id']
sp.user_playlist_add_tracks(user_id, playlist_id, track_ids)

