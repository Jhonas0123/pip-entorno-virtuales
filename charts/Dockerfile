FROM python:3.12.3

WORKDIR /charts
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /charts/requirements.txt

COPY . /charts

CMD bash -c "while true; do sleep 1; done" 