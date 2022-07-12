"""System module."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# Values of .env
apikey = os.environ['apikey']
url = os.environ['url']

# Instance IBM Watson
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

# Translate english to french
def english_to_french(english_text):
    """Convert text in english to french"""
    if english_text is not None:
        # Translate text
        french_text = language_translator.translate(
        text = english_text,
        model_id = 'en-fr').get_result()
        # Obtain translated text
        french_text =  french_text.get('translations')[0].get('translation')
        print('English text: ' + english_text + ' to French text: ' + french_text)
        return french_text
    return None

# Translate french to english
def french_to_english(french_text):
    """Convert text in english to french"""
    if french_text is not None:
        # Translate text
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        # Obtain translated text
        english_text =  english_text.get('translations')[0].get('translation')
        print('French text: ' + french_text + ' to English text: ' + english_text)
        return english_text
    return None
