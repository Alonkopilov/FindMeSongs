FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./datasets /code/datasets
COPY ./src /code/src

CMD ["uvicorn", "src.main:app"]
