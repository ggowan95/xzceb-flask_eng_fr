"""
Translator using IBM's Watson Translating function for the english and french languages
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

languages = language_translator.list_languages().get_result()

def englishtofrench(englishtext):
    """
    This function uses Watsons Translate Function to translate english text to french
    """
    if englishtext is None:
        return None  
    translation = language_translator.translate(
    englishtext,
    model_id='en-fr').get_result()
    frenchtext = translation
    return frenchtext

def frenchtoenglish(frenchtext):
    """
    This function uses Watsons Translate Function to translate french text to english
    """
    if frenchtext is None:
        return None
    translation = language_translator.translate(
    frenchtext,
    model_id='fr-en').get_result()
    englishtext = translation
    return englishtext
