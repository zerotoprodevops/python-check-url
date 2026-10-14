FROM python:alpine3.24

WORKDIR /opt/app

RUN apk add curl

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "app.py"] 

CMD ["https://google.com"]
 
