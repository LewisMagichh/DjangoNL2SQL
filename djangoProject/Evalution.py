import os
from djangoProject.settings import BASE_DIR
import json
from django.http import HttpResponse
from django.shortcuts import render

def evalution(request):
    file_path = os.path.join(BASE_DIR,"djangoProject/KVsql.json")
    with open(file_path,'r') as f:
        dic = json.load(f)
        f.close()
    Accuracy = dic['correct']/(dic['correct'] + dic['error'])
    Accuracy = "%.4f%%" % (Accuracy * 100)

    return render(request,"evalution.html",{"Accuracy":Accuracy,"correct":dic['correct'],"error":dic['error']})