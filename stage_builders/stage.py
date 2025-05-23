from stage_builders.helpers.helpers import *


class Stage:
    def __init__(self, params, previous_stage):
        self.name = params['action']
        self.params = params['action_params']
        self.previous_stage = previous_stage
        prereqs = params['action_prereqs']
        if prereqs: 
            if not check_prereqs(prereqs):
                print("Missing prereq in {}".format(self.name))
                raise OSError