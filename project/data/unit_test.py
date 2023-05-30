import os
import sys
import data_pipeline

abs_path = os.path.dirname(__file__)

EXAMPLE_CSV = "weather-cologne-bonn-history-2000-2021.csv"
EXPECTED_LOCATION = './'

data_pipeline.save_url(EXAMPLE_CSV, EXPECTED_LOCATION)

file_exists = os.path.exists(EXPECTED_LOCATION)

print("[UNIT TESTS] Example file was written as expected:", os.path.exists(EXPECTED_LOCATION))
print("[UNIT TESTS] Cleanup..")

if file_exists:
    os.remove(EXPECTED_LOCATION)
    sys.exit(0)

sys.exit(1)