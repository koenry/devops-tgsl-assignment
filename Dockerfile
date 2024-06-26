FROM python:3.10.12

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./api .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
