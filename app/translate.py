import requests
from flask_babel import _

from app import app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    endpoint = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': source_language,
        'to': dest_language
    }

    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': app.config['MS_TRANSLATOR_LOCATION']
    }

    body = [{
        'Text': text
    }]

    r = requests.post(constructed_url, params=params, headers=auth, json=body)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()[0]['translations'][0]['text']
