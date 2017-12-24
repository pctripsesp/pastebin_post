#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import requests

url = 'https://pastebin.com/api/api_post.php'

global USERNAME, PASSWORD, api_dev_key, api_user_key

api_paste_name = 'TEST'
api_paste_code = 'HELLO WORLD!'

#Get from localfile SECRET pass and API like {"USERNAME": "YOUR_USERNAME", "PASSWORD": "YOUR_PASS", "api_dev_key": "YOUR_API_KEY"}
def get_SECRETO():

    try:
        f = open('SECRETO.txt', 'r+')
        sec_dic = json.loads(f.read())
        global USERNAME, PASSWORD, api_dev_key, api_user_key
        USERNAME = sec_dic['USERNAME']
        PASSWORD = sec_dic['PASSWORD']
        api_dev_key = sec_dic['api_dev_key']

        if 'api_user_key' in sec_dic:
            api_user_key = sec_dic['api_user_key']
            print('USER KEY =',api_user_key)
        else:
            api_user_key = get_api_user_key()
            print('USER KEY CREATED =',api_user_key)
            sec_dic['api_user_key'] = api_user_key
            f.seek(0)
            f.write(str(sec_dic).replace("'",'"'))

        f.close()

    except Exception as e:
        print(e)

#TRY TO USE SAME API_USER_KEY ONCE CREATED; ELSE YOU CAN CREATE A NEW ONE EACH TIME
def get_api_user_key():
    global USERNAME, PASSWORD, api_dev_key, api_user_key
    data = {'api_dev_key': api_dev_key,
            'api_user_name': USERNAME,
            'api_user_password': PASSWORD}
    response = requests.post('http://pastebin.com/api/api_login.php', data=data)

    return response.text


#Def function with request parameters
def create_paste(api_paste_code, api_paste_name):

    #OPTIONAL PARAMETERS
    api_paste_private = '2'             #0=public 1=unlisted 2=private
    api_paste_expire_date = '1H'        #N = Never ; 10M = 10 Minutes; 1H = 1 Hour ; 1D = 1 Day ; 1M = 1 Month ; 6M = 6 Months ; 1Y = 1 Year
    api_paste_format = 'python'         # dos, c, csharp, cpp, css, go, java...
    api_option = 'paste'

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



#get_api_user_key()
get_SECRETO()
create_paste(api_paste_code, api_paste_name)
