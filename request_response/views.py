import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def weather1(request,city,year):
    print("city1 = %s" % city )
    print("year1 = %s" % year)
    return HttpResponse("weather1")

def weather2(request,year,city):
    print("city2 = %s" % city )
    print("year2 = %s" % year)
    return HttpResponse("weather2")

def weather3(request,year,city):
    print("city3 = %s" % city )
    print("year3 = %s" % year)
    return HttpResponse("weather3")

def weather4(request,year,city):
    print ("city3 = %s" % city)
    print ("year3 = %s" % year)
    a = request.GET.get("a")
    b = request.GET.get("b")
    alist = request.GET.getlist("a")
    print(a,b,alist)

    return HttpResponse ("weather4")

def get_body_form(request):
    a = request.POST.get("a")
    b = request.POST.get("b")
    a_list = request.POST.getlist("a")
    print(a,b,a_list)
    return HttpResponse("get form data success")

def get_body_json(request):
    bytes_str = request.body
    json_str = bytes_str.decode()
    req_data = json.loads(json_str)
    print(req_data["a"])
    print(req_data["b"])
    return HttpResponse("get json data success")

def response_json(request):
    return HttpResponse("OK",content_type="text/html",status=200)

def response_json1(request):
    response = HttpResponse("OK",content_type="text/html",status=201)
    response["Itcast"] = "Python"
    return response

def response_json2(request):
    json_dict = {"name":"xcg","age":3}
    return JsonResponse(json_dict)

def cookie_demo(request):
    response = HttpResponse("cookie_demo")
    response.set_cookie("name","chaoge",max_age=3600)
    name = request.COOKIES.get("name")
    print(name)
    return response

def session_demo(request):
    request.session["name"] = "Xcg"
    name = request.session.get("name")
    print(name)
    return HttpResponse("session_demo")
