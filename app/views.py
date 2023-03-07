from django.shortcuts import render
from django.http import HttpResponse
def nkrapp1_first(request):
    return HttpResponse("<h1><marquee>NKR APP1 First</marquee></h1>")

def nkrapp1_second(request):
    return HttpResponse("<h1><marquee>NKR APP1 Second</marqee></h1>")