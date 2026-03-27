FROM python:3.12

WORKDIR /usr/scr/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 8080

# flask --app app run --host=0.0.0.0 --port=8080

CMD [ "flask", "--app", "app", "run", "--host=0.0.0.0", "--port=8080" ]