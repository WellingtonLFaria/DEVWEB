FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update
RUN apt-get install libmysqlclient-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "run", "--host", "0.0.0.0" ]