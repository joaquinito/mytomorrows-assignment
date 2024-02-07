#!/bin/sh

cd venv/lib/python3.11/site-packages/
zip -r9 ../../../../fastapi_lambda_function.zip .
cd ../../../..
zip ./fastapi_lambda_function.zip -r api
