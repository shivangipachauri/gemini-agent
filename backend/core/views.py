import os
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def prompt_handler(request):
    prompt = request.data.get('prompt', '')

    api_key = os.getenv("GEMINI_API_KEY")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": api_key
    }
    data = {
        "contents": [
            {
                "parts": [
                    { "text": prompt }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        content = response.json()
        reply = content["candidates"][0]["content"]["parts"][0]["text"]

        # Basic classification
        if "joke" in prompt.lower():
            action = "joke"
        elif "weather" in prompt.lower():
            action = "weather"
        else:
            action = "general"

        return Response({
            "action": action,
            "result": reply
        })

    except Exception as e:
        return Response({
            "action": "error",
            "result": str(e)
        })
