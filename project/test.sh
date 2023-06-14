#!/bin/bash

# if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Run the pipeline with the -r flag, forcing it to load fresh data
python ./project/data/data_pipeline.py -r

# Check if the pipeline was successful in creating the output file
# EXPECTED_OUTPUT_FILE="./data/db_Saki.db"
# if ! test -f "$EXPECTED_OUTPUT_FILE"; then
#     echo "[ERROR] $EXPECTED_OUTPUT_FILE doesn't exist!"
#     exit 2
# fi
 
# echo "[SUCCESS] $EXPECTED_OUTPUT_FILE exists."

# Run unit tests
# python ./project/data/unit_test.py

echo "ran the test.sh file"
