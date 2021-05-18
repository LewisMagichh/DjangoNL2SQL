import base64

import datetime

import json

import os

import wave

import requests
from django.http import JsonResponse
from django.shortcuts import render

from pyaudio import PyAudio, paInt16

from pydub import AudioSegment
from djangoProject.settings import BASE_DIR

# 获取token
def get_access_token():

    API_Key = '2m48v8HfayF7ZwdLiOlCeAef' # 换成你自己的

    Secret_Key = 'Z3W1ELS32ibx2nINjYMmZ5jYizNN2kvU' # 换成你自己的

    url = 'https://openapi.baidu.com/oauth/2.0/token?'

    payload = {
        "grant_type": "client_credentials",
        "client_id": API_Key,
        "client_secret": Secret_Key
    }

    response = requests.get(url, params=payload, timeout=3)
    json_str = json.loads(response.text)

    access_token = json_str['access_token']

    return access_token


framerate = 16000
NUM_SAMPLES = 2000
channels = 1
sampwidth = 2
TIME = 3

# 前端传来的语音文件写入方式
def save_wave_file(filename, data):

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()


# 音频格式转换（mp3转wav）
# def trans_mp3_to_wav():
#
#     # 转换前的语音地址
#     song = AudioSegment.from_mp3('/home/wwwroot/zcc/01.mp3')
#
#     # 转换后的语音地址
#     song.export("/home/wwwroot/zcc/01.wav", format="wav")


# 百度音频转换接口
def get_word():

    file_path = os.path.join(BASE_DIR,'djangoProject/01.wav')
    with open(file_path, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf8')

    size = os.path.getsize(file_path)

    headers = {'Content-Type': 'application/json'}

    access_token = get_access_token()

    url = 'https://vop.baidu.com/server_api'
    data = {
        "format": "wav",
        "rate": 16000,
        "channel": 1,
        "cuid": 'tyc',
        "dev_pid": 1737,
        "token": access_token,
        "len": size,
        "speech": speech,
    }
    req = requests.post(url, json.dumps(data), headers)
    result = json.loads(req.text)
    return result


# 录音（微信小程序开发腾讯有录音功能所以这个没用上）
def my_record(request):
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=1,
                    rate=framerate, input=True,
                    frames_per_buffer=NUM_SAMPLES)
    my_buf = []
    count = 0
    print('录音中')
    # 控制录音时间
    while count < TIME * 10:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1

    save_wave_file('01.wav', my_buf)
    print('结束录音')
    stream.close()
    result = get_word()
    print(result)
    return JsonResponse(result)
if __name__ == '__main__':

    my_record()
    result = get_word()
    print(result)