import sys

def get_os():
    return sys.platform
    #win32
    #darwin

def check_prereqs(prereqs):
    for prereq in prereqs: 
        if prereq.contains("os"):
            os = prereq.split(":")[1]
            if os != get_os():
                return False