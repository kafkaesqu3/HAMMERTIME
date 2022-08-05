import os
from subprocess import PIPE, Popen
from stage_builders.stage import Stage

class Exe2Shellcode(Stage): 
    def run_command(self):
        print(self.previous_stage)
        srdi_path = "{}/tools/sRDI/Python/ConvertToShellcode.py".format(os.getcwd())
        
        
        

        name = self.params["exe_x64"]["path_val"]
        if name.endswith(".exe") or name.endswith(".dll"): 
            outfile_name = name[0:-4] + ".bin"
        else: 
            outfile_name = name
        
        
        srdi_args = "-f {0} -of raw".format(
            self.params["function_name"], )
        
        if self.params["clear_header"] == True: 
            srdi_args = srdi_args + " -c"
        if self.params["obfuscate_imports"] == True:
            srdi_args = srdi_args + " -i"
        if self.params["delay"] != 0 :
            srdi_args = srdi_args + " -d {0}".format(self.params["delay"])

        # finally add DLL name
        srdi_args = srdi_args + " {0}".format(self.params["exe_x64"]["path_val"])
        srdi_cmd = "/Users/david/.pyenv/shims/python3 {} {}".format(srdi_path, srdi_args)
        print(srdi_cmd)
        srdi_proc = Popen(srdi_cmd, stdout=PIPE, stderr=None, shell=True)
        srdi_proc.wait()

        output = srdi_proc.communicate()[0]
        print(output)
        print(os.getcwd())

        output_read = open(outfile_name, "rb")
        shellcode = output_read.read()
        output_read.close()
        os.remove(outfile_name)
        print(len(shellcode))
        return shellcode

    def build(self, build_directory):
        shellcode = self.run_command()
        out_file = "{}/shellcode.bin".format(build_directory)
        output = open(out_file, "wb")
        output.write(shellcode)
        return out_file