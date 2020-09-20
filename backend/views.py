from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404

from .models import Snack, User

# Create your views here
def index(request):
    return HttpResponse("Hello, world. You're at the snacks system backend index")

# return all snacks
def snacks(request):
    snack_list = list(Snack.objects.all().values())
    return JsonResponse({'snacks': snack_list})

# get the balance of user
def balance(request, user_id):
    try:
        user = get_object_or_404(User, pk=user_id)
        return JsonResponse({
            'slackID': user.slackID,
            'name': user.name,
            'balance': user.balance,
        })
    except User.DoesNotExist:
        return Http404("user not found")
