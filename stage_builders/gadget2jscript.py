from stage_builders.helpers.helpers import *

class Gadget2JScript: 
    def __init__(self, params):
        self.params = params['action_params']
        prereqs = params['action_prereqs']
        if prereqs: 
            if not check_prereqs(prereqs):
                print("Missing prereq")

    def run_command(self):
        g2js_path = "tools/GadgetToJScript/GadgetToJScript.exe"
        g2js_args = ""

    def build(self):
        self.run_command()