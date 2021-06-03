import os
from djangoProject.settings import BASE_DIR
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time

def restored(inferone,infertwo):
    file_path = os.path.join(BASE_DIR,"djangoProject/stored_history.json")
    with open(file_path,'r') as f:
        dic = json.load(f)
        f.close()
    lenth = len(dic)
    mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    dic.append({
        "index":lenth+1,
        "infer_one":inferone,
        "infer_two":infertwo,
        "mtime": mtime
    }
    )
    with open(file_path,'w') as f:
        json.dump(dic,f)
        f.close()
    return
@csrf_exempt
def showstoreddata(request):
    file_path = os.path.join(BASE_DIR, "djangoProject/stored_history.json")
    with open(file_path,'r') as f:
        dic = json.load(f)
        f.close()

    return JsonResponse(dic,safe=False)

def tabled(request):

    return render(request,'bs-table.html')
if __name__=='__main__':
    restored(3,2)