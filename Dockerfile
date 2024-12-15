FROM python:3.13.1

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY /app .src/app
COPY /static .src/static 
COPY /templates .src/templates
COPY main.py .src/

WORKDIR /src

EXPOSE 8000

CMD ["python", "main.py"]
