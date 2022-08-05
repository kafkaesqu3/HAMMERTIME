import os
from subprocess import PIPE, Popen
from stage_builders.stage import Stage

class Crossfit(Stage): 

    def generate_payload(self, name, arch):
        oldcwd = os.getcwd()
        crossfit_path = os.getcwd() + self.params["crossfit_path"]
        payload_fullpath = os.path.join(oldcwd, name)
        if arch == "x64":
            crossfit_args = "-a {0} -p 64".format(payload_fullpath)
        elif arch == "x86":
            crossfit_args = "-a {0} -p 32".format(payload_fullpath)
        else: 
            print("Arch not supported: {0}".format(arch))
            return None
        if self.params["apc_safe"] == True: 
            crossfit_args = crossfit_args + " --apc"
        if self.params["newdomain"] == True:
            crossfit_args = crossfit_args + " -n"
        crossfit_cmd = "python.exe {}clrvoyance.py {}".format(crossfit_path, crossfit_args)
        print(crossfit_cmd)
        oldcwd = os.getcwd()
        os.chdir(crossfit_path)
        crossfit_proc = Popen(crossfit_cmd, stdout=PIPE)
        output = crossfit_proc.communicate()
        print(output[0].decode("utf-8"))
        os.chdir(oldcwd)
        outfile_name = name + ".shellcode" 
        output_read = open(outfile_name, "rb")
        shellcode = output_read.read()
        output_read.close()
        return shellcode


    def run_command(self):
        print(self.previous_stage)
        output = self.generate_payload(self.previous_stage, self.params["arch"])
        return output 

    def build(self, build_directory):
        shellcode = self.run_command()
        out_file = "{}\shellcode.bin".format(build_directory)
        output = open(out_file, "wb")
        output.write(shellcode)
        return out_file