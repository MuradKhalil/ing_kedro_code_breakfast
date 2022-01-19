FROM python:3.7.11
COPY src/requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /kedro_tutorial
COPY . /kedro_tutorial

RUN apt-get update && \
    apt-get install -y nano

CMD ["bash"]



