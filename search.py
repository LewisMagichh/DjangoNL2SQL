from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
import os
import sys
import json
from .write_down import updata_json_data
from .preproc import proprection

def search_form(request):
    return render(request, 'post.html')

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
    ctx={}
    input_dbid = {}
    input_question = {}
    if request.POST:
        ctx['db_id'] = '你选择的数据库地址为' + request.POST['db_id']
        ctx['raw_question'] = '你说的话为' + request.POST['question']
        input_dbid = request.POST['db_id']
        input_question = request.POST['question']
        params = updata_json_data(input_dbid,input_question)
        ctx['db_id_json'] = params[0]['db_id']
        ctx['question_json'] = params[0]['question']
        proprection()
        ctx['params'] = "successed proprection"
    return render(request,"post.html", ctx)

