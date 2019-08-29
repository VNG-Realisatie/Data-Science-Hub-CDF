FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --upgrade pip && \
    pip install --no-cache-dir pandas && \
    pip install --no-cache-dir cbsodata

COPY ./fastapi/app /app

EXPOSE 80