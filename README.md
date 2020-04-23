# Description

HAMMERTIME is a payload builder tool which supports multi-stage payload building. 

Each payload build is defined by a config file, stored in the configs directory. The config file is a JSON object which defines the configurable actions of each stage. Each config represents a payload. You can add as many stages to these payloads as are supposed by the framework. 

Create a builder script for each stage (stored in builder_scripts) directory which defines how each stage is built. Stages are supposed to be linked together, so each stage recieves the previous stage as a parameter. 

Resources required for building the payload (such as other tools used to create the stage, or code templates which a stage is based on) are stored in the tools/ and templates/ directory, respectively. 

# Building a payload 
Since there's only one config (named VIOLETVAGABOND), it's been hardcoded into the program. Just update the config file with your shellcode (the default is to pop calc.exe), modify the process you want to inject into, and run the HAMMERTIME script. Your uncompiled C# template and serialized VBA macro will be stored in the output directory. 

# Quickstart guide for adding new stages

Working on it...