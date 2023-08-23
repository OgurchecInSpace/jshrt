FROM python:3.10.5-alpine

RUN adduser -D jshrt

WORKDIR /home/jshrt

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY jshrt.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP jshrt.py

RUN chown -R jshrt:jshrt ./
USER jshrt

EXPOSE 80
ENTRYPOINT ["./boot.sh"]