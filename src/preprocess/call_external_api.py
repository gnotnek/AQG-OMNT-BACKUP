# import http.client
# import json


# API_BASE_URL = '10.181.131.244'
# POS_TAG_PORT = '5500'
# NER_PORT = '10009'

# def get_pos_tag(text):
#     conn = http.client.HTTPConnection(API_BASE_URL, POS_TAG_PORT)
#     payload = json.dumps({'text': text})
#     headers = {
#         "content-type": "application/json",
#         "x-api-key": ""
#         }

#     conn.request('POST', '/', payload, headers)
#     res = conn.getresponse()
#     data = json.loads(res.read().decode('utf-8'))

#     return data

# def get_ner(text):
#     conn = http.client.HTTPConnection(API_BASE_URL, NER_PORT)
#     payload = json.dumps({'text': text})
#     headers = {
#         "content-type": "application/json",
#         "x-api-key": ""
#         }

#     conn.request('POST', '/', payload, headers)
#     res = conn.getresponse()
#     data = json.loads(res.read().decode('utf-8'))

#     return data

import json
import requests
 
url_ner = "https://api.prosa.ai/v2/text/ner"
url_pos = "https://api.prosa.ai/v2/text/basic-nlp"
api_key_ner="eyJhbGciOiJSUzI1NiIsImtpZCI6Ik5XSTBNemRsTXprdE5tSmtNaTAwTTJZMkxXSTNaamN0T1dVMU5URmxObVF4Wm1KaSIsInR5cCI6IkpXVCJ9.eyJhcHBsaWNhdGlvbl9pZCI6MzA5NDk1LCJsaWNlbnNlX2tleSI6IjE4MmY0ZGU0LWM0MzYtNDU0Yi1iNGJmLTlmYWJhMmM1YjNhZiIsInVuaXF1ZV9rZXkiOiI1MWM3MmRmZS02MmQ5LTQxMTktOGM3My1kZjc4ZWM2YThiNzEiLCJwcm9kdWN0X2lkIjoxMSwiYXVkIjoiYXBpLXNlcnZpY2UiLCJzdWIiOiI1NmNlODQ3Yi1jNWIyLTQxNzUtYjc1OC01MGY5MzhlMDZmZGYiLCJpc3MiOiJjb25zb2xlIiwiaWF0IjoxNzA0NjMwMTM0fQ.QWmuyH5SM3v7q4c865IYmjctJhD1mwf8M28zPTMs6doE4x06AqwCTekOFp2EK988AnSaQPkwv5A9VJmTtpd4lHNg5M1tX0sQA8jRwX6NokP3DJMLSliydMtRiTxD0BCKLqhwYr5kyjkwY97MgvnzIpmdC7qBdtBWkVOmVBUDaFdaM9I0EqVp6f9XG6boa9hFYeI7nUTkh-JMo9dNiE9ls60z9_lL-ezBM_Vi7Cqmfqbhooapa2FXhlakWw4lXw-CRqKZ79yRcnrSr7LUvRN8zowsR98Lbc6kAswgsiUamjW2LI9AVFR1yGyc47gWTx_BvLq9MSf7OzCXeGa69ss5Ew"
api_key_pos="eyJhbGciOiJSUzI1NiIsImtpZCI6Ik5XSTBNemRsTXprdE5tSmtNaTAwTTJZMkxXSTNaamN0T1dVMU5URmxObVF4Wm1KaSIsInR5cCI6IkpXVCJ9.eyJhcHBsaWNhdGlvbl9pZCI6Mjk3MDE5LCJsaWNlbnNlX2tleSI6ImExMDFhNmViLTM5OWQtNDNjOC1hODhkLTRmMWU3MTNkNjlkMCIsInVuaXF1ZV9rZXkiOiI3OWQ2ZTQ5YS1kYWEyLTQ4MzYtYTFlYi1hMDQ3YmNhNWE1Y2UiLCJwcm9kdWN0X2lkIjo5LCJhdWQiOiJhcGktc2VydmljZSIsInN1YiI6Ijc2M2FiODlkLWEyOGEtNDUxYS05Nzg1LWIyZmYyMGI2ODVjMCIsImlzcyI6ImNvbnNvbGUiLCJpYXQiOjE3MDE5NjQzMzd9.bk7h9SHQEJakJNuOV_uqbuYdayG9vXQMhEq9xYET7gvj3O5vm2rW1SkRy8pV3pcV4GLQAosjzIIP5XCKIr2VEqsOwlAdsXTtStXulJMOq3cWdkDvsvzRxMBGOw9HBynp1hJ_qlbyPOm9PT6lva4QgZklohynGzIPSJnt-XgWphT3I1AkVOXoTZhZOGIND16fAGpNY02SepqyPxdvNENxjCW4rajaS-g8EzCzxGyBE-d1XSM3wFZ5I5PqcpNSWNf3uf1z8xJZBkUdhXVRXDE-B_FTUne_0j5SpGP0pLFJYmrMbyirjVIRwBAT2bxmSdZpfQwATD7nrDABnw2IYh0Saw"
 


def get_pos_tag(text):
    data = {
        "version": "v2",
        "text": text,
    }
    headers = {
        "Content-Type": "application/json",
         "x-api-key": api_key_pos
    }
    response = requests.post(url_pos, headers=headers, json=data)
    jsondata=response.json()
    pos_tags = []
    for sentence in jsondata['sentences']['sentences']:
        tokens = sentence.get('tokens', [])
        sentence_tags = [[token.get('token', ''), token.get('pos_tag', '')] for token in tokens]
        pos_tags.append(sentence_tags)

    # Create the final dictionary in the desired format
    result = {'postags': pos_tags}
#    return numpy.array(result)
    return result

def get_ner(text):
    data = {
        "version": "v2",
        "text": text,
    }
    headers = {
        "Content-Type": "application/json",
         "x-api-key": api_key_ner
    }
    response = requests.post(url_ner, headers=headers, json=data)
    jsondata=response.json()
    return jsondata
