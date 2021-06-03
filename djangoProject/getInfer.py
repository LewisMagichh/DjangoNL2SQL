import os
import sys
import json
import jsonlines
from djangoProject.settings import BASE_DIR
from djangoProject.Restored import restored

def get_infer():
    dir_path = os.path.join(BASE_DIR, 'djangoProject/nltsql/logdir/glove_run/bs=20,lr=7.4e-04,end_lr=0e0,att=0/ie_dirs')
    file = os.listdir(dir_path)
    hasInferred = [0,1,2]
    for p in file:
        file_path = os.path.join(dir_path, p)
        with open(file_path, 'r') as f:
            i = 0
            for item in jsonlines.Reader(f):
                hasInferred[i] = item['beams'][0]['inferred_code']
                i+=1
        f.close()
    restored(hasInferred[0],hasInferred[2])
    return hasInferred
