from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
import os
import sys
import json
from .write_down import updata_json_data
from .preproc import proprection
from .InitFile import init_file
from .getInfer import get_infer
from .KVwrite import write_error,write_correct
def search_form(request):
    return render(request, 'searchpost.html')

def search(request):
    request.encoding='utf-8'
    if 'db_id' in request.GET and request.GET['db_id']:
        dbid = request.GET['db_id']
    else:
        message = '请输入数据库'

    if 'question' in request.GET and request.GET['question']:
        raw_question = request.GET['raw_question']
    else:
        message = '请输入查询语句'

    message = '你输入的数据为' + 'db_id:'+ dbid +' raw_question:' +raw_question
    return HttpResponse(message)

def search_post(request):

    # if request.POST:
    #     input_dbid = request.POST['db_id']
    #     input_question = request.POST['question']
    #     # params = updata_json_data(input_dbid,input_question)
    #     # ctx['db_id_json'] = params[0]['db_id']
    #     # ctx['question_json'] = params[0]['question']
    #     proprection()
    #     ctx['params'] = get_infer()

    return render(request, "searchpost.html", ctx)


def inferlist(request):
    if request.POST:
        init_file()
        input_dbid = request.POST['db_id']
        input_question = request.POST['question']

        params = updata_json_data(input_dbid,input_question)
        proprection()

    infer = get_infer()

    return render(request,"infer.html",{"inferone":infer[0],"infertwo":infer[2]})