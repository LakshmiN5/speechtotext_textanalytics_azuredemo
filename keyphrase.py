import os, requests, uuid, json



def get_keywords(input_text):
    subscription_key = 'f0460139f2df470dbd4764cf28cdc116'
    base_url = 'https://eastus.api.cognitive.microsoft.com/text/analytics'
    path = '/v2.0/keyPhrases'
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
            "documents": [
                {
                "language": "en",
                "id": "1",
                "text": input_text
                }
            ]
            }
    response = requests.post(constructed_url, headers=headers, json=body)
    print(response)
    return response.json()
