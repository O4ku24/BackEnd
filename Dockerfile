FROM python:3.13.1

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY /app ./app
COPY /static ./static 
COPY /templates ./templates
COPY main.py .

EXPOSE 8000

CMD ["python", "main.py"]
