import os,time
import json
import requests
from bs4 import BeautifulSoup

def extract_html_from_url(url:str):
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            raise Exception('Invalid Response from url')
        html_content = resp.content.decode('utf-8')

    except Exception as e:
        print('[ERROR] in extract_html_from_url : {}'.format(e))
        

def extract_text_from_html(html_code:str):
