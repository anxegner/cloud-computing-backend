FROM python:3.12

WORKDIR /usr/src/app

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--port=8080"]