import spotipy
import spotipy.util as util
SPOTIPY_CLIENT_ID = '5b219ea7c93c475db3fa7acd846af046'
SPOTIPY_CLIENT_SECRET = '372adbb3af4d4a03a935d894cd5f2af5'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

userSpot = ""
scope = 'user-library-read user-modify-playback-state'

token = util.prompt_for_user_token(userSpot, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth=token)

Song1 = ""
Song2 = ""
Song3 = ""
Song = "One"

def SearchSong(Song):
    global Song1
    try:
        result = sp.search(q=Song, type='track', limit=1)
        if not isinstance(Song, str):
            return 0
        elif result['tracks']['items']:
            Song1 = result['tracks']['items'][0]['uri']
        else:
            print(f"Song not found! {Song}")
            return 0
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error while searching for song: {e}")

def PlaySong(track_uri):
    sp.start_playback(uris=[track_uri])

