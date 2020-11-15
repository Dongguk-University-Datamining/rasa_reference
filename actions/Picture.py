import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
from urllib.request import urlopen
from PIL import Image

# database 인증 및 초기화
# cred = credentials.Certificate('actions/Mykey.json')
# default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://imagesoundquote.firebaseio.com/'})

def show(ref):
    temp_dict = ref.get()
    url_list = list(temp_dict.values())
    url = random.choice(url_list)
    img = Image.open(urlopen(url))
    img.show()


def get_image(emotion):
    if emotion == 'happy':
        ref = db.reference('Picture/Happy_emotion')
        show(ref)

    elif emotion == 'sad':
        ref = db.reference('Picture/Sad_emotion')
        show(ref)

    elif emotion == 'lonely':
        ref = db.reference('Picture/Lonely_emotion')
        show(ref)

    elif emotion == 'bored':
        ref = db.reference('Picture/Bored_emotion')
        show(ref)
