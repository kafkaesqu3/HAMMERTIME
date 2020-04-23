import json
from stage_builders.shellcode_injection import *
from stage_builders.gadget2jscript import *

CONFIG = "configs/VIOLETVAGABOND.json"

config_file = open(CONFIG, "r")
parsed_conf = (json.loads(config_file.read()))

def stage_loader(stage): 
    name = stage['action']
    if name == "shellcode_injection":
        stage_builder = Shellcode_Injection(stage)
        stage_builder.build()
    elif name == "gadget2jscript":
        stage_builder = Gadget2JScript(stage)
        stage_builder.build()
    else: 
        print("Not supported")

for stage in parsed_conf['stages']: 
    action = stage['action']
    print("Stage {}".format(action))
    stage_loader(stage)