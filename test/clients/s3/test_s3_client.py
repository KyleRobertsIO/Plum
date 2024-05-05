import pytest

from plum.clients.s3.client import S3Client
from plum.clients.s3.connectors.access_key_connector import S3AccessKeyConnector

@pytest.mark.integration_minio
def test_list_objects_and_get_content(get_s3_access_key_connector: S3AccessKeyConnector):
    """
    Confirms that the list objects and get object content methods are working.
    """
    client = S3Client(
        connector = get_s3_access_key_connector
    )

    # Test getting list of objects from S3 bucket
    objs, list_err = client.list_objects(
        prefix = ""
    )
    if list_err != None:
        assert False, f"error when listing object; {list_err.args}"
    assert len(objs) > 0, "expected objects returned but got 0 objects"
    
    # Test getting content from S3 bucket
    file_bytes, content_err = client.get_object_contents(
        key = objs[0].get("Key")
    )
    if content_err != None:
        assert False, f"failed to collect byte contents of s3 object; {content_err.args}"
    try:
        file_bytes.decode("utf-8")
    except Exception as decode_err:
        assert False, f"failed to decode S3 file contents; {decode_err.args}"
    
    assert True