#!/usr/bin/env python
# coding: utf-8

import sys
import json
import requests
import time 
import pandas as pd

def get_int_answer(question):
    while True:
        try:
            user_inp = int(input(question))  
            # assert user_inp > 0
            if user_inp > 0: 
                return user_inp
            raise ValueError('Less than 1!')
        except ValueError:
            print('should be a positive integer, try again..')

l = 2
port = 5000
while (reply:=input('do you want to run test with default parameters? (enter y/n): ').lower()) not in {'y', 'n'}: pass
if reply == 'n':
    l = get_int_answer('enter matrix dimension: ')
    # port = get_int_answer('enter server port: ')

job_id = str(requests.get("http://127.0.0.1:" + str(port) + "/calculate/" + str(l)).content.decode('utf-8'))
print('\nyour job id is : %s\n\nplease, wait..' % job_id)
while True:
    res = requests.get("http://127.0.0.1:" + str(port) + "/result/" + job_id)
    if res.status_code == 200:
        df = pd.DataFrame(json.loads(res.content.decode('utf-8')))
        print('\nhere is your random matrix:\n', df)
    elif res.status_code == 201:
        time.sleep(1)
        continue
    else:
        print('oops, something went wrong', res)
    break