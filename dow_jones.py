from ucimlrepo import fetch_ucirepo

# Verify the Python executable
import sys
print("Python executable:", sys.executable)

# Fetch dataset
try:
    dow_jones_index = fetch_ucirepo(id=312)
    print("Dataset fetched successfully.")
    print(dow_jones_index)
except Exception as e:
    print(f"Error fetching dataset: {e}")


    