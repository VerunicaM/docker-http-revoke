# docker-http-revoke

This is a basic [Docker Compose](https://docs.docker.com/compose/) template based on [mattkohls](https://github.com/mattkohl) project [docker-flask-celery-redis](https://github.com/mattkohl/docker-flask-celery-redis) and designed to revoke Celery tasks via HTTP requests immediately. I used it in a real project on a Raspberry Pi to start LED light scenes via Streamdeck, so that the running scene is interrupted and the new scene starts immediately. 


### Installation

To clone the repository simply type the following command into your terminal or command line:

`git clone https://github.com/VerunicaM/docker-http-revoke`

You can now start the build process via

`docker-compose up -d --build`

or 

`docker-compose -f docker-compose.yml -f docker-compose.development.yml up --build`

to build and enable hot code reload.

The project is set up to expose the Flask application's endpoints on port `5001` as well as a [Flower](https://github.com/mher/flower) server for monitoring workers on port `5555`.


### Usage

There are already three very simple tasks defined in the [celery-queue/tasks.py](./celery-queue/tasks.py) file. The `revokeall` task stops running tasks except for itself. The `sub_task` simulates a long running task and takes one argument that defines how long the task will run. The `main_task` wraps both tasks so that they are executed one after the other. 

The Flask application defines only one route. Use this route to trigger the `main_task` and add a parameter to the route to define how long the `sub_task` should run. Your url should look something like this:

`http://localhost:5001/?t=60`

Trigger another request and check 

`http://localhost:5555`

to see what happend.


### Contribute

I welcome contributions to django-powerbi-embedded. If you have a bug fix or new feature that you would like to contribute, please fork the repository and submit a pull request.