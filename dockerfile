FROM python:3.11
WORKDIR ./app
COPY ./infrastructure ./app/infrastructure
COPY ./services ./app/services
COPY ./domains ./app/domains
COPY requirements.txt ./
COPY main.py ./
RUN pip install -r requirements.txt
CMD python main.py