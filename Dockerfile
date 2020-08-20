FROM python:3.6.9
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8000
COPY . /app
CMD sleep 20 && testdocker/manage.py makemigrations && testdocker/manage.py migrate && testdocker/manage.py runserver 0.0.0.0:8000
