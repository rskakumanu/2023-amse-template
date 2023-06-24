import os
import sys

# Get the absolute path of the current script file
abs_path = os.path.dirname(__file__)

# Define the expected file name and location
EXPECTED_FILE = "Geschwindigkeitüberwachung_Koeln_Gesamt_2017-2022_0.csv"
EXPECTED_LOCATION = './'

# Check if the file exists in the specified location
file_exists = os.path.exists(os.path.join(EXPECTED_LOCATION, EXPECTED_FILE))

# Print the result of file existence check
print("[UNIT TESTS] Example file exists in the folder:", file_exists)
print("[UNIT TESTS] Cleanup..")

if file_exists:
    # Perform cleanup by removing the file
    os.remove(os.path.join(EXPECTED_LOCATION, EXPECTED_FILE))
    sys.exit(0)  # Exit with success status (file was written as expected)

sys.exit(1)  # Exit with failure status (file was not found)
