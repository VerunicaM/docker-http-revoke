import time
from flask import Flask, request, Response
from worker import celery


dev_mode = True
app = Flask(__name__)


@app.route('/')
def index():
    print(type(request.args.get('t')))
    celery.send_task('tasks.main_task', args=[int(request.args.get('t'))], kwargs={})
    return f'Running a task for {request.args.get("t")} seconds'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
