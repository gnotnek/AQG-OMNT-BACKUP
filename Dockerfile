FROM Ubuntu:20.4

WORKDIR /usr/src/app

COPY . .

RUN apt-get -y update 

RUN apt-get -y upgrade

RUN apt-get -y install git

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

RUN python test_app.py

CMD ["python", "app.py"]