import pytest
import os
from dotenv import load_dotenv

from plum.engines.connectors.postgresql import PostgresSqlLoginConnector

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope = "session")
def get_postgres_sql_login_connector() -> PostgresSqlLoginConnector:
    connector = PostgresSqlLoginConnector(
        host = os.getenv("TEST_POSTGRES_HOST"),
        port = os.getenv("TEST_POSTGRES_PORT"),
        database = os.getenv("TEST_POSTGRES_DATABASE"),
        username = os.getenv("TEST_POSTGRES_USERNAME"),
        password = os.getenv("TEST_POSTGRES_PASSWORD")
    )
    return connector