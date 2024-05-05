import pytest

from plum.clients.postgresql.connectors.sql_login_connector import PostgresSqlLoginConnector

@pytest.mark.unit
def test_postgres_sql_login_get_psycopg_connection_string():
    connector = PostgresSqlLoginConnector(
        host = "localhost",
        port = 5432,
        database = "example_db",
        username = "postgres",
        password = "securePassword"
    )
    conn_str: str = connector.get_psycopg_connection_string()

    assert "host=localhost" in conn_str
    assert "dbname=example_db" in conn_str
    assert "user=postgres" in conn_str
    assert "password=securePassword" in conn_str
    assert "port=5432" in conn_str