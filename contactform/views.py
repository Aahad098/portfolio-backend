from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
import json

@csrf_exempt
def submit_contact(request):
    if request.method == "POST":
        try:
            if request.headers.get('Content-Type') == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST

            Contact.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                message=data.get('message')
            )
            return JsonResponse({"success": True}, status=201)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return JsonResponse({"success": False, "error": "Only POST method allowed"}, status=405)