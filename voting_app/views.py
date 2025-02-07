from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Vote
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def cast_vote(request):
    if request.method == "POST":
        data = json.loads(request.body)
        choice = data.get("choice")
        if choice in ["v1", "v2"]:
            Vote.objects.create(choice=choice)
            return JsonResponse({"message": f"Vote recorded for {choice}!"}, status=200)
        return JsonResponse({"error": "Invalid vote. Vote for 'v1' or 'v2'."}, status=400)

def display_results(request):
    v1_count = Vote.objects.filter(choice="v1").count()
    v2_count = Vote.objects.filter(choice="v2").count()
    winner = "It's a tie!" if v1_count == v2_count else ("V1 wins!" if v1_count > v2_count else "V2 wins!")
    return JsonResponse({"v1": v1_count, "v2": v2_count, "winner": winner})
