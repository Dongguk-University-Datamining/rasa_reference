import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
from playsound import playsound

# database 인증 및 초기화
cred = credentials.Certificate('actions/Mykey.json')
default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://imagesoundquote.firebaseio.com/'})

def play(ref):
    temp_dict = ref.get()
    url_list = list(temp_dict.values())
    url = random.choice(url_list)
    playsound(url)

def get_sound(emotion):
    if emotion == 'happy':
        ref = db.reference('Sound/Happy_emotion')
        play(ref)
    elif emotion == 'sad':
        ref = db.reference('Sound/Sad_emotion')
        play(ref)
    elif emotion == 'bored':
        ref = db.reference('Sound/Bored_emotion')
        play(ref)
    elif emotion == 'lonely':
        ref = db.reference('Sound/Lonely_emotion')
        play(ref)

