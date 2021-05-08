import os
import sys
from djangoProject.settings import BASE_DIR
def init_file():
    file_path = os.path.join(BASE_DIR,'djangoProject/nltsql/logdir/glove_run/bs=20,lr=7.4e-04,end_lr=0e0,att=0/ie_dirs')
    del_file = os.listdir(file_path)
    for f in del_file:
        del_path = os.path.join(file_path, f)
        os.remove(del_path)
    return del_file