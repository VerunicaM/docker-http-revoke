FROM python:3.9-buster

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

COPY . /queue
WORKDIR /queue

RUN pip install -U setuptools pip
RUN pip install -r requirements.txt

RUN sed -i 's/\r$//g' /queue/entrypoint.sh
RUN chmod 755 /queue/entrypoint.sh
ENTRYPOINT ["sh", "/queue/entrypoint.sh"]
