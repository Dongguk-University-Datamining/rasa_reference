import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random

def get_quote_kor(emotion):
    if emotion == 'happy':
        ref = db.reference('Quote/Korean/Happy_emotion')
        temp_dict = ref.get()
        url_list = list(temp_dict.values())
    elif emotion == 'sad':
        ref = db.reference('Quote/Korean/Sad_emotion')
        temp_dict = ref.get()
        url_list = list(temp_dict.values())
    elif emotion == 'bored':
        ref = db.reference('Quote/Korean/Bored_emotion')
        temp_dict = ref.get()
        url_list = list(temp_dict.values())
    elif emotion == 'lonely':
        ref = db.reference('Quote/Korean/Lonely_emotion')
        temp_dict = ref.get()
        url_list = list(temp_dict.values())
    return url_list

def get_quote_eng(emotion):
    if emotion == 'happy':
        ref = db.reference('Quote/English/Happy_emotion')
        temp_dict = ref.get()
        url_list = list(temp_dict.values())
    elif emotion == 'sad':
        ref = db.reference('Quote/English/Sad_emotion')
        temp_dict = ref.get()
        url_list = list(temp_dict.values())
    elif emotion == 'bored':
        ref = db.reference('Quote/English/Bored_emotion')
        temp_dict = ref.get()
        url_list = list(temp_dict.values())
    elif emotion == 'lonely':
        ref = db.reference('Quote/English/Lonely_emotion')
        temp_dict = ref.get()
        url_list = list(temp_dict.values())
    return url_list
