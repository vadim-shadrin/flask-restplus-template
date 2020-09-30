FROM python:latest
ENV DEBIAN_FRONTEND="noninteractive"

ENV PYTHONPATH=.

WORKDIR /code
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY tests/requirements.txt ./tests/
RUN pip install -r tests/requirements.txt

RUN apt-get update && apt-get install -y uwsgi uwsgi-plugin-python
RUN pip install uwsgi

RUN useradd -s /bin/false -M flask-uwsgi

EXPOSE 5080

COPY . /code

CMD ["python", "service/main.py"]
#CMD ["uwsgi", "uwsgi.ini"]