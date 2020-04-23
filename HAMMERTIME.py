import json
import time
import os
from stage_builders.shellcode_injection import *
from stage_builders.gadget2jscript import *

CONFIG = "configs/VIOLETVAGABOND.json"

config_file = open(CONFIG, "r")
parsed_conf = (json.loads(config_file.read()))
build_name = parsed_conf['name']
build_version = parsed_conf['version']
timestamp = time.strftime("%Y%m%d-%H%M%S")
build_directory = "build_outputs/{}_v{}_{}".format(build_name, build_version, timestamp)
os.makedirs(build_directory, exist_ok = False)

def stage_loader(stage, previous_stage): 
    name = stage['action']
    if name == "shellcode_injection":
        stage_builder = Shellcode_Injection(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "gadget2jscript":
        stage_builder = Gadget2JScript(stage, previous_stage)
        return stage_builder.build(build_directory)
    else: 
        print("Stage {} not supported".format(name))
        return False

previous_stage = None
for current_stage in parsed_conf['stages']: 
    action = current_stage['action']
    print("Building stage: {}".format(action))
    finished_stage = stage_loader(current_stage, previous_stage)
    previous_stage = finished_stage