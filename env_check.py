import sys

def in_virtualenv():
    return sys.prefix != sys.base_prefix

def check_version_old(version, minimum):
    # buggy: compares strings
    return version >= minimum

def check_version(version, minimum):
    # correct: compares tuples of numbers
    v = tuple(int(x) for x in version.split("."))
    m = tuple(int(x) for x in minimum.split("."))
    return v >= m

if __name__ == "__main__":
    print(f"venv active: {in_virtualenv()}")