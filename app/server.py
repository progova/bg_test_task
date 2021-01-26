#!/usr/bin/env python
# coding: utf-8

from flask import Flask, Response, abort
import tasks

app = Flask(__name__, static_folder = '.', static_url_path = '')

@app.route('/')
def home():
    return 'hello, world'

@app.route('/calculate/<num>')
def calculate(num):
    try:
        num = int(num)
    except ValueError:
        abort(415, 'please, use digits only')
    if num < 1: 
        abort(415, 'dimension must be positive!')
    job = tasks.do_large_task.delay(num)
    return Response(job.id, status = 201, mimetype = 'application/json') 
        
@app.route('/result/<op_id>')
def result(op_id):
    if op_id:       
        job = tasks.get_job(op_id)
        if job.state == 'SUCCESS':
            return Response(job.get(), status = 200, mimetype = 'application/json')
        else:
            return Response(status = 201)
    return Response(status=404)


if __name__=='__main__':
    app.run(host='0.0.0.0')