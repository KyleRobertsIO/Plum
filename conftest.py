import pytest
import os
from dotenv import load_dotenv

from plum.clients.postgresql.connectors.sql_login_connector import PostgresSqlLoginConnector
from plum.clients.s3.connectors.access_key_connector import S3AccessKeyConnector

@pytest.fixture(scope='session', autouse=True)
def load_env():
    '''
    Loads the enviornment variables used in the project test suite.
    '''
    load_dotenv()

@pytest.fixture(scope = "session")
def get_postgres_sql_login_connector() -> PostgresSqlLoginConnector:
    '''
    Creates a PostgresSqlLoginConnector object for test cases that need it.
    '''
    connector = PostgresSqlLoginConnector(
        host = os.getenv("TEST_POSTGRES_HOST"),
        port = os.getenv("TEST_POSTGRES_PORT"),
        database = os.getenv("TEST_POSTGRES_DATABASE"),
        username = os.getenv("TEST_POSTGRES_USERNAME"),
        password = os.getenv("TEST_POSTGRES_PASSWORD")
    )
    return connector

@pytest.fixture(scope = "session")
def get_s3_access_key_connector() -> S3AccessKeyConnector:
    connector = S3AccessKeyConnector(
        host = os.getenv("TEST_S3_HOST"),
        port = os.getenv("TEST_S3_PORT"),
        bucket_name = os.getenv("TEST_S3_BUCKET_NAME"),
        tls = True if os.getenv("TEST_S3_TLS", "FALSE").upper() == "TRUE" else False,
        access_key_id = os.getenv("TEST_S3_ACCESS_KEY_ID"),
        access_key_secret = os.getenv("TEST_S3_ACCESS_KEY_SECRET")
    )
    return connector