from django.shortcuts import render
from .models import Service, Subscription, Fake_News, FAQ, Info, Message
# Create your views here.

def index(request):
    services = Service.objects.all()
    subscriptions = Subscription.objects.all()
    news = Fake_News.objects.all()
    faqs = FAQ.objects.all()
    info = Info.objects.all()
    
    if request.method == "POST":
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")
        Message.objects.create(email = email, message = message)
        print("Posting")

    return render(request, "index.html", {
        "services" : services[:3],
        "subscriptions" : subscriptions[:3],
        "news" : news[:3],
        "faqs" : faqs,
        "info" : info[0]
    })