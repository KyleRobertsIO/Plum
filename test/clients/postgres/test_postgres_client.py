import pytest
import psycopg

from plum.clients.postgresql.connectors.sql_login_connector import PostgresSqlLoginConnector
from plum.clients.postgresql.client import PostgresClient

@pytest.mark.integration_postgres
def test_create_connection(
    get_postgres_sql_login_connector: PostgresSqlLoginConnector
):
    pg_engine = PostgresClient(connector = get_postgres_sql_login_connector)
    conn, conn_err = pg_engine._create_connection()

    if conn_err != None:
        assert False, 'failed to connect to PostgreSQL database'
    assert isinstance(conn, psycopg.Connection), 'method did not return psycopg.Connection when expected'


@pytest.mark.unit
def test_create_bulk_insert_details(
    get_postgres_sql_login_connector: PostgresSqlLoginConnector
):
    pg_engine = PostgresClient(connector = get_postgres_sql_login_connector)

    data = [
        { "first_name": "John", "last_name": "Smith", "age": 43 },
        { "first_name": "Jane", "last_name": "Doe", "age": 35 }
    ]
    key_col, tuple_col = pg_engine._create_bulk_insert_details(dict_col= data)

    assert len(key_col) == 3
    assert "first_name" in key_col
    assert "last_name" in key_col
    assert "age" in key_col

    first_record = tuple_col[0]
    assert first_record[0] == "John"
    assert first_record[1] == "Smith"
    assert first_record[2] == 43

    second_record = tuple_col[1]
    assert second_record[0] == "Jane"
    assert second_record[1] == "Doe"
    assert second_record[2] == 35

@pytest.mark.integration_postgres
def test_bulk_insert(
    get_postgres_sql_login_connector: PostgresSqlLoginConnector
):
    pg_engine = PostgresClient(connector = get_postgres_sql_login_connector)

    data = [
        { "first_name": "John", "last_name": "Smith", "age": 43 },
        { "first_name": "Jane", "last_name": "Doe", "age": 35 }
    ]

    insert_err: Exception = pg_engine.bulk_insert(
        table = "dbo.staging_person", 
        data = data
    )

    assert insert_err == None, f'failed to perform bulk insert; {insert_err.args}'

    forced_insert_err: Exception = pg_engine.bulk_insert(
        table = "dbo.staging_person_unknown", 
        data = data
    )

    assert forced_insert_err != None, 'expected to get bulk insert error but did not get one'