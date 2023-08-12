FROM python:slim

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3","form_app.py"]