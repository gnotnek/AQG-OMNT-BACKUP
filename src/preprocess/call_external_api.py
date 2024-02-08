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
api_key_ner="eyJhbGciOiJSUzI1NiIsImtpZCI6Ik5XSTBNemRsTXprdE5tSmtNaTAwTTJZMkxXSTNaamN0T1dVMU5URmxObVF4Wm1KaSIsInR5cCI6IkpXVCJ9.eyJhcHBsaWNhdGlvbl9pZCI6MzI0NTc5LCJsaWNlbnNlX2tleSI6IjRiZWNiMzQwLTIyMTUtNGQ0Mi04MTZhLWMyYjdjMWEzYjlhYyIsInVuaXF1ZV9rZXkiOiI1NWQwMTlkNy0xODVhLTQzN2UtOTMyMi0xZGEyNmI0Y2ZlMDciLCJwcm9kdWN0X2lkIjoxMSwiYXVkIjoiYXBpLXNlcnZpY2UiLCJzdWIiOiI3ZmI5ZjU1YS1jZDc4LTQ2MzgtYTU1Yi00NzVhNTcxYWI3N2EiLCJpc3MiOiJjb25zb2xlIiwiaWF0IjoxNzA3NDAzNjgxfQ.kPczloler-CH-DL2D_H6dGp7cyoI9RCQdd6_bHYfuIWWg3nWwD4f2lP9Pvc_SBkYjlFbsT8DCPgziI5XdJm28B-p89o74DkVLiyy9JkGBcmc1itCOV0PWpy9ZRDtG9g0I2xCdoSXi_xXBTR4BV5ziPhUYG-Ed6LA1neHDSPKGFDbriAlZu3bthB5h8Uk2Eq2peJc50LVMGd7Ix2a8IUm84NvS9ri3XxNFzTJOULMLlJ5UQ7umFqo4DAKM-hWnIXvTRuXjDiKpQ_wEjGQ78yFhTLeAQg46u1yTg30KtSQ39aYMYJcuiS0YqU6VZqYGBihksvQUuGa1RObK_7j-IySTg"
api_key_pos="eyJhbGciOiJSUzI1NiIsImtpZCI6Ik5XSTBNemRsTXprdE5tSmtNaTAwTTJZMkxXSTNaamN0T1dVMU5URmxObVF4Wm1KaSIsInR5cCI6IkpXVCJ9.eyJhcHBsaWNhdGlvbl9pZCI6MzI0NTkwLCJsaWNlbnNlX2tleSI6IjVkNTc4YTVlLWRkYTItNDhlYi1iMjdkLWJiZGQwYjZkZGJlOCIsInVuaXF1ZV9rZXkiOiIyNzU5Nzg2OS02NTk3LTRlOGItODA1Ni1iYzY1ZmZhYTczYjQiLCJwcm9kdWN0X2lkIjo5LCJhdWQiOiJhcGktc2VydmljZSIsInN1YiI6IjdmYjlmNTVhLWNkNzgtNDYzOC1hNTViLTQ3NWE1NzFhYjc3YSIsImlzcyI6ImNvbnNvbGUiLCJpYXQiOjE3MDc0MDUzNDh9.dXIz_n7-LnE3jyUmZa9YnGcSgdeYZ7i7Wdip-higZ5u9XTIEqDOX-e6KrEbqzs3GTYdHuUYMZSZ9u0gkvHOmKj1wPwTzF8gCM7rcW3k4ExOHOT2RswtHmgrV1MDaorhNFeO75hp2Nd703azvTxz8FSYft13N90JLUCP2mtlu5sTrANLoCFAdzckLuNPdP59K2JHu-KtQpdbKCRSYSYy2Li7xfl91hjoT_GZ5XdE47j5XaxXm54LeUMi55Qm1HQ06ZTEQ11AbnxjXNJIH_r25rkhHmpbIFPaOgHO0foozgmMiDRCfaWMONx30SVwDQ1AsNGylSNkiWXs6GQ2rhpXTdA"
 


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
