import sys
from env_check import check_version, check_version_old

func = check_version_old if "--old" in sys.argv else check_version

assert func("3.9", "3.10") is False, "3.9 should be older than 3.10"
assert func("3.12", "3.10") is True
print("All tests passed")