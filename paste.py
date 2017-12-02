#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

USERNAME = 'YOUR_PASTEBIN_USERNAME'
PASSWORD = 'YOUR_PASTEBIN_PASSWORD'
api_dev_key = 'YOUR_APIDEV_KEY' #Get from https://pastebin.com/api
api_option = 'paste'
url = 'https://pastebin.com/api/api_post.php'

api_paste_name = 'PASTE_NAME'
api_paste_code = 'HI WORLD!'

#username and pass are needed to get api_user_key; else, you will post as a guest
def get_api_user_key():
    global USERNAME, PASSWORD, api_dev_key
    data = {'api_dev_key': api_dev_key,
            'api_user_name': USERNAME,
            'api_user_password': PASSWORD}
    response = requests.post('http://pastebin.com/api/api_login.php', data=data)
    return response.text

#Def function with request parameters
def create_paste(api_dev_key, api_option, api_paste_code, api_paste_name):

    #OPTIONAL PARAMETERS
    api_paste_private = '0'             #0=public 1=unlisted 2=private
    api_paste_expire_date = '1H'        #N = Never ; 10M = 10 Minutes; 1H = 1 Hour ; 1D = 1 Day ; 1M = 1 Month ; 6M = 6 Months ; 1Y = 1 Year
    api_paste_format = 'python'         # dos, c, csharp, cpp, css, go, java...
    api_user_key = get_api_user_key()   #If None or no correct, guest user will be created

    #add to dictionary all parameters you want post
    params = {}
    params['api_dev_key']= api_dev_key
    params['api_option']= api_option
    params['api_paste_code']= api_paste_code
    params['api_paste_name']= api_paste_name
    params['api_paste_expire_date']= api_paste_expire_date
    params['api_user_key']= api_user_key
    params['api_paste_private']= api_paste_private


    resp = requests.post(url, params)
    print(resp.text)

create_paste(api_dev_key, api_option, api_paste_code, api_paste_name)
