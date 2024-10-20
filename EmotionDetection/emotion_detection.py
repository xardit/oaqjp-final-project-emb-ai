import requests


def emotion_detector(text_to_analyze):
    # Send a POST request to the Emotion Predict function
    response = requests.post(
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        },
        json={"raw_document": {"text": text_to_analyze}},
    )

    # Check if the response is successful
    if response.status_code == 200:
        # Return the json response
        RESPONSE_DATA = response.json()
        return {
            "anger": RESPONSE_DATA.anger_score,
            "disgust": RESPONSE_DATA.disgust_score,
            "fear": RESPONSE_DATA.fear_score,
            "joy": RESPONSE_DATA.joy_score,
            "sadness": RESPONSE_DATA.sadness_score,
            "dominant_emotion": "joy",
        }
    else:
        # Handle the case where the request was unsuccessful
        raise Exception(f"Error {response.status_code}: {response.text}")


# Example usage (Uncomment to test)
# result = emotion_detector("I love this new technology.")
# print(result)
