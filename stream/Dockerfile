FROM python:3.12.0-slim

WORKDIR /app

RUN apt-get update

RUN apt-get install libgl1-mesa-glx libglib2.0-0 -y

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]