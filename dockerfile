FROM python:3.11
WORKDIR ./app
COPY ./infrastructure ./infrastructure
COPY requirements.txt ./
COPY main.py ./
RUN pip install -r requirements.txt
CMD python main.py