def verify_with_infermedica_async(text, app_id, app_key):
    """
    Send user message to Infermedica API.
    Returns: JSON response with extracted conditions and symptoms.
    """

    url = "https://api.infermedica.com/v3/parse/"

    headers = {
        "App-Id": app_id,
        "App-Key": app_key,
        "Content-Type": "application/json"
    }

    # Infermedica requires: "text": [ list ]
    payload = {"text": [text]}

    response = requests.post(url, headers=headers, json=payload)
    return response.json()
