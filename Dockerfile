FROM python:slim

WORKDIR /opt

COPY . /opt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3","app.py"]
