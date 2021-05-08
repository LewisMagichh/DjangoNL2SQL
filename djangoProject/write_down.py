import os
import sys
import json
from djangoProject.settings import BASE_DIR

def updata_json_data(str1,str2):
    file_path = os.path.join(BASE_DIR,'djangoProject/nltsql/data/spider/dev.json')
    with open(file_path,'r') as f:
        params = json.load(f)
        f.close()
        for i in range(0,3):
            params[i]['db_id'] = str1
            params[i]['question'] = str2
        with open(file_path,'w')as f:
            json.dump(params,f)
            f.close()
    return params