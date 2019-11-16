"""
Some links to check out if you work on this and are stuck:
https://stackoverflow.com/questions/25757163/importing-requests-module-does-not-work
https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script/31764155
https://curl.trillworks.com/
https://pypi.org/project/requests/
https://cloud.ibm.com/apidocs/natural-language-understanding/natural-language-understanding#keywords
https://cloud.ibm.com/services/natural-language-understanding/crn%3Av1%3Abluemix%3Apublic%3Anatural-language-understanding%3Aus-south%3Aa%2F7fd62a78587949c5ac941211da5cefba%3A9131df81-8d9a-4068-b48f-fe834cfdb59b%3A%3A?paneId=gettingStarted
"""

user_audio_file_location = "audio-file.flac"

import requests

headers = {
    'Content-Type': 'audio/flac',
}

data = open(user_audio_file_location, 'rb').read()
response = requests.post('https://stream.watsonplatform.net/speech-to-text/api/v1/recognize', headers=headers, data=data, auth=('apikey', 'eEqdSotOfLXQb39UorT9BqwyUfGhPpl-gNld9lbXN1C-'))
print response

"""
headers_two = {
    'Content-Type': 'application/json',
}

params_two = (
    ('version', '2019-07-12'),
)

data_two = '{                                             \n  "text": "I love apples! I do not like oranges.",\n  "features": {\n    "sentiment": {\n      "targets": [\n        "apples",\n        "oranges",\n        "broccoli"\n      ]          \n    },           \n    "keywords": {\n      "emotion": true\n    }\n  }\n}'

response = requests.post('https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze', headers_two=headers_two, params_two=params_two, data_two=data_two, auth=('apikey', 'eyGxtlKE8AEr_Ng7sbBJLsqVCbwiJ7lElY0Og9R2_9-x'))
"""






"""
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2019-07-12', headers=headers, data=data, auth=('apikey', 'eyGxtlKE8AEr_Ng7sbBJLsqVCbwiJ7lElY0Og9R2_9-x'))
curl -X POST -u "apikey:eyGxtlKE8AEr_Ng7sbBJLsqVCbwiJ7lElY0Og9R2_9-x" \
--request POST \
--header "Content-Type: application/json" \
--data '{
    "text": ""
    "features": {
        "keywords": {
        }
    }
}'
"""
