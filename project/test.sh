#!/bin/bash

# Execute data_pipeline.py script with -r flag to load fresh data
python ./data/data_pipeline.py -r

# Execute unit_test.py script to run unit tests
python ./data/unit_test.py

# Print message indicating that the test.sh file was executed
echo "ran the test.sh file"