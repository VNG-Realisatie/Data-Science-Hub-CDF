FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --upgrade pip && \
    pip install --no-cache-dir pandas

COPY ./app /app

EXPOSE 80