import spotipy
import spotipy.util as util


SPOTIPY_CLIENT_ID = '5b219ea7c93c475db3fa7acd846af046'
SPOTIPY_CLIENT_SECRET = '372adbb3af4d4a03a935d894cd5f2af5'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

userSpot = "ANGELOCEL"
scope = 'user-library-read user-modify-playback-state'

token = util.prompt_for_user_token(userSpot, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth=token)

Song1 = ""
SongAll = ""

current_playback = None


def SearchSong(Song):
    global Song1, SongAll
    result = sp.search(q=Song, type='track', limit=1)
    if not isinstance(Song, str):
        return 0
    elif result['tracks']['items']:
        SongAll = result['tracks']['items'][0]
        return 1
    else:
        print("Song not found! {song_name}")
        return 0


def SelectSong(Song, Space):
    if SearchSong(Song):
        # user.Songs1[Space] = Song1
        return 1
    else:
        return 0


def PlaySong(track_uri):
    if sp.devices()['devices']:
        print("Playing song!")
        return 1
    else:
        print("Song not playing!")
        return 0


def UserSpotSelect(UserSpot):
    global userSpot
    userSpot = UserSpot
    print(userSpot)


def PauseMusic():
    sp.pause_playback()


def VerifySong(Song):
    if sp._get_uri(Song['uri'], 'track'):
        print("Song defualt!")
        return 1
    else:
        return 0


def GetSongDuration(Duration):
    duration_ms = Duration
    duration_s = duration_ms / 1000
    print(duration_s)
    # duration_minutes = duration_ms // 60000
    # duration_seconds = (duration_ms // 1000) % 60
    # print(duration_ms)
    # print("Minutes:",duration_minutes,":",duration_seconds) #Es para darlo en minutos y segundos exacti
    return duration_s



