import os
import sys
import json
import jsonlines
from djangoProject.settings import BASE_DIR

def get_infer():
    dir_path = os.path.join(BASE_DIR,'djangoProject/nltsql/logdir/glove_run/bs=20,lr=7.4e-04,end_lr=0e0,att=0/ie_dirs')
    file = os.listdir(dir_path)
    for p in file:
        file_path = os.path.join(dir_path,p)

    with open(file_path,'r') as f:
        for item in jsonlines.Reader(f):
            hasInferred = item['beams'][0]['inferred_code']

    return hasInferred