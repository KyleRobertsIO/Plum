FROM python:3.11-bullseye

WORKDIR /library_testing

COPY ./plum ./plum
COPY ./requirements.txt ./requirements.txt

COPY ./pytest.ini ./pytest.ini
COPY ./conftest.py ./conftest.py
COPY ./test ./test
COPY ./entrypoint.sh ./entrypoint.sh

RUN pip install -r requirements.txt

RUN mkdir ./junit
VOLUME /library_testing/junit

ENTRYPOINT ["./entrypoint.sh"]