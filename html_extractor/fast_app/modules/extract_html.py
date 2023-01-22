import os,time
import json
import requests
from bs4 import BeautifulSoup
import re
import string
import pickle

def preprocess_text(text:str) -> str:
  return re.sub('[a-zA-Z0-9 ]','',text.strip())

def save_data_dict_and_html(data_dict:dict,html_code:str,save_dir='./saved_content') -> str:
    time_stamp = str(time.time()).replace('.','_')
    files_save_dir = os.path.join(save_dir,time_stamp)
    if not os.path.exists(files_save_dir):
        os.makedirs(files_save_dir)
    with open(os.path.join(files_save_dir,'data_dict.json'),'w') as f:
        json.dump(data_dict,f)
    with open(os.path.join(files_save_dir,'html_content.html'),'w') as f:
        f.write(html_code)
    return files_save_dir


def extract_text_from_url(url:str):
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception('Invalid Response from url')
    html_content = resp.content.decode('utf-8')
    files_save_dir = extract_text_from_html(html_content)
    return files_save_dir

def extract_text_from_html(html_code:str):
    html_soup = BeautifulSoup(html_code)
    data_dict = {}
    text_tags_ = ['h1','h2','h3','h4','h5','h6','p','li','td']
    for i,elem in enumerate(html_soup.find_all(text_tags_)):
        text_ = elem.get_text()
        if preprocess_text(text_):
            elem_id_ = elem.get('id',default=str(i))
            data_dict[elem_id_] = text_
            elem['id'] = elem_id_
    files_save_dir = save_data_dict_and_html(data_dict,str(html_soup))
    return files_save_dir



