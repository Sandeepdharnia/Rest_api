from django.http import HttpResponse, JsonResponse
def home_page(request):
    print("Home page requested")
    friends = [
        "Raj",
        "Vikas",
        "Ravi"
    ]
    return JsonResponse(friends, safe=False)
