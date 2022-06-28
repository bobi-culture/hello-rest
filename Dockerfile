FROM python:3-alpine
WORKDIR /service

#COPY requirements.txt .
#COPY hello.py ./service
#RUN pip install -r requirements.txt

RUN pip install flask 
COPY . . 

EXPOSE 5000
ENV FLASK_APP=hello
ENV FLASK_RUN_HOST=0.0.0.0 

ENTRYPOINT ["flask", "run"]

