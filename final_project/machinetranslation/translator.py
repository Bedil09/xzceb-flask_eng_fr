""" import and install packages"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2021-12-09'

auth = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION, authenticator=auth)

language_translator.set_service_url(url)


def english_to_french(english_text):
    '''Translates english text to french'''
    french_translation = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    translation = french_translation['translations'][0]['translation']
    return translation


def french_to_english(french_text):
    '''Translates french text to english '''
    english_translation = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    translation = english_translation['translations'][0]['translation']
    return translation
