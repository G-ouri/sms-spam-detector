import json
import joblib
from pathlib import Path

from django.conf import settings
from django.http import JsonResponse, FileResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import ScanResult


# Load trained model once when Django starts
MODEL = joblib.load(
    Path(__file__).resolve().parent.parent / "spam_model.pkl"
)


def home(request):
    return render(request, "index.html")


def css(request):
    return FileResponse(
        open(settings.BASE_DIR / "templates" / "style.css", "rb"),
        content_type="text/css"
    )


def js(request):
    return FileResponse(
        open(settings.BASE_DIR / "templates" / "app.js", "rb"),
        content_type="application/javascript"
    )


def detect_spam(message):

    prediction = MODEL.predict([message])[0]

    if prediction == "spam":
        return {
            "verdict": "spam",
            "confidence": 85,
            "explanation": "Message resembles known spam patterns."
        }

    return {
        "verdict": "safe",
        "confidence": 85,
        "explanation": "Message resembles legitimate communication."
    }


@csrf_exempt
@require_http_methods(["POST"])
def check(request):

    body = json.loads(request.body)
    message = body.get("message", "").strip()

    if not message:
        return JsonResponse(
            {"error": "No message provided."},
            status=400
        )

    result = detect_spam(message)

    ScanResult.objects.create(
        message=message,
        verdict=result["verdict"],
        confidence=result["confidence"],
        explanation=result["explanation"],
    )

    return JsonResponse(result)