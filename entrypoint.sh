#!/bin/bash

echo "Installing Minio CLI"

curl https://dl.min.io/client/mc/release/linux-amd64/mc --create-dirs -o $HOME/minio-binaries/mc

chmod +x $HOME/minio-binaries/mc
export PATH=$PATH:$HOME/minio-binaries/

echo "Copying Files To Bucket"

MC_ALIAS_HOST="http://$TEST_S3_HOST:$TEST_S3_PORT"
mc alias set test_service $MC_ALIAS_HOST $TEST_S3_ACCESS_KEY_ID $TEST_S3_ACCESS_KEY_SECRET

mc mb --insecure test_service/$TEST_S3_BUCKET_NAME

mkdir /minio_test_data
echo "Sample Content A" > /minio_test_data/sample_file_a.txt
echo "Sample Content B" > /minio_test_data/sample_file_b.txt

mc cp --recursive /minio_test_data/ test_service/$TEST_S3_BUCKET_NAME/

pytest ./test --junitxml=junit/test-results.xml