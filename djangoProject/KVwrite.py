import os
from djangoProject.settings import BASE_DIR
import json
from django.http import HttpResponse
from django.shortcuts import render

def write_correct(request):
    file_path = os.path.join(BASE_DIR,"djangoProject/KVsql.json")
    with open(file_path,'r') as f:
        dic = json.load(f)
        f.close()
    dic["correct"] += 1
    with open(file_path,'w') as f:
        json.dump(dic,f)
        f.close()
    return HttpResponse()

def write_error(request):
    file_path = os.path.join(BASE_DIR, "djangoProject/KVsql.json")
    with open(file_path, 'r') as f:
        dic = json.load(f)
        f.close()
    dic["error"] += 1
    with open(file_path, 'w') as f:
        json.dump(dic, f)
        f.close()
    return HttpResponse()