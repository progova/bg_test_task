# bg_test_task
a web app emulating execution of a 'heavy' task in the background.

Although the app is simple itself, it is configured as it was a serious one.

Flask has been chosen as a framework due to it's simplicity. 
Asynchronous tasks are processed by Celery queue with RabbitMQ brocker help.
These components were built together with Docker.

## Running tests

_Server (with 3 workers):_

```
git clone https://github.com/progova/bg_test_task

cd bg_test_task

docker-compose up --scale worker=3
```

_Client:_
```
python client.py
```
