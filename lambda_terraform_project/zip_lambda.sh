#!/bin/bash
cd lambda_function
pip install -r requirements.txt -t .
zip -r ../lambda_function.zip .
cd ..
