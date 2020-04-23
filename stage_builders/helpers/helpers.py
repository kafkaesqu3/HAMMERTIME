import sys

def get_os():
    return sys.platform
    #win32
    #darwin

def check_prereqs(prereqs):
    prereqs = prereqs.split(',')
    for prereq in prereqs: 
        if "os" in prereq:
            os = prereq.split(":")[1]
            if os != get_os():
                return False