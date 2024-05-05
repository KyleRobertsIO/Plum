FROM python:3.11-bullseye

WORKDIR /library_testing

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./plum ./plum
COPY ./pytest.ini ./pytest.ini
COPY ./conftest.py ./conftest.py
COPY ./test ./test
COPY ./entrypoint.sh ./entrypoint.sh

RUN mkdir ./junit
VOLUME /library_testing/junit

ENTRYPOINT ["./entrypoint.sh"]