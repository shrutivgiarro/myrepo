from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from UsersApp.models import User, Logs, Pages
from UsersApp.serializers import UsersSerializer, PagesSerializer, LogsSerializer



@csrf_exempt
def userLogin(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        
        email = user_data.get('email')
        password = user_data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse("User not found with the provided email", safe=False)

        users_serializer = UsersSerializer(user)
        serialized_data = users_serializer.data

        if serialized_data['password'] == password:
            return JsonResponse("Email and password are the same.", safe=False)
        else:
            return JsonResponse("Email and password are different.", safe=False)

    return JsonResponse("Invalid request method", safe=False)



@csrf_exempt
def userApi(request,user_id=0):
    if request.method=='GET':
        users = User.objects.all()
        users_serializer = UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        users_serializer = UsersSerializer( data = user_data )
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("User Added Successfully",safe=False)
        return JsonResponse("User Failed to Add",safe=False)
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(user_id = user_data['user_id'])
        users_serializer = UsersSerializer(user,data = user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("User Updated Successfully",safe=False)
        return JsonResponse("User Failed to Update")
    elif request.method=='DELETE':
        user = User.objects.get(user_id = user_id)
        user.delete()
        return JsonResponse("User Deleted Successfully",safe=False)

@csrf_exempt
def logsApi(request, log_id = 0):
    if request.method == 'GET':
        logs = Logs.objects.all()
        logs_serializer = LogsSerializer(logs, many=True)
        return JsonResponse(logs_serializer.data, safe=False)

    elif request.method == 'POST':
        log_data = JSONParser().parse(request)
        # print(log_data)  # Add this line to check the content of log_data
        user_id = log_data.get('user_id')
        
        try:
            user_id = int(user_id)
        except ValueError:
            return JsonResponse("Invalid user_id. Please provide a valid integer.", safe=False)

        try:
            user_instance = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return JsonResponse("User not found with the provided user_id.", safe=False)
        
        # log_data['user_id'] = user_instance
        logs_serializer = LogsSerializer(data=log_data)
        
        # print(logs_serializer.is_valid())
        if logs_serializer.is_valid():
            logs_serializer.save()
            return JsonResponse("Log Added Successfully", safe=False)
        return JsonResponse("Log Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        log_data = JSONParser().parse(request)
        log = Logs.objects.get(log_id = log_data['log_id'])
        logs_serializer = LogsSerializer(log, data=log_data)
        if logs_serializer.is_valid():
            logs_serializer.save()
            return JsonResponse("Log Updated Successfully", safe=False)
        return JsonResponse("Log Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        log = Logs.objects.get(log_id = log_id)
        log.delete()
        return JsonResponse("Log Deleted Successfully", safe=False)


@csrf_exempt
def pagesApi(request, page_visit_id = 0):
    if request.method == 'GET':
        pages = Pages.objects.all()
        pages_serializer = PagesSerializer(pages, many=True)
        return JsonResponse(pages_serializer.data, safe=False)
    elif request.method == 'POST':
        page_data = JSONParser().parse(request)
        user_id = page_data.get('user_id')
        log_id = page_data.get('log_id')
        
        try:
            user_id = int(user_id)
            log_id = int(log_id)
        except ValueError:
            return JsonResponse("Invalid user_id or log_id. Please provide a valid integer.", safe=False)

        try:
            user_instance = User.objects.get(pk=user_id)
            log_instance = Logs.objects.get(pk=log_id)
        except User.DoesNotExist or Logs.DoesNotExist:
            return JsonResponse("User or Log not found", safe=False)

        pages_serializer = PagesSerializer(data=page_data)
        if pages_serializer.is_valid():
            pages_serializer.save()
            return JsonResponse("Page Added Successfully", safe=False)
        return JsonResponse("Page Failed to Add", safe=False)

    elif request.method == 'PUT':
        page_data = JSONParser().parse(request)
        page = Pages.objects.get(page_visit_id=page_data['page_visit_id'])
        pages_serializer = PagesSerializer(page, data=page_data)
        if pages_serializer.is_valid():
            pages_serializer.save()
            return JsonResponse("Page Updated Successfully", safe=False)
        return JsonResponse("Page Failed to Update", safe=False)

    elif request.method == 'DELETE':
        page = Pages.objects.get(page_visit_id = page_visit_id)
        page.delete()
        return JsonResponse("Page Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)