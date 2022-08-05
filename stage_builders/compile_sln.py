import os
from stage_builders.stage import Stage
from subprocess import PIPE, Popen
import shutil

class CompileSln(Stage): 
    def run_command(self):
        print(self.previous_stage)


        # update resource file
        if self.params["update"]: 
            if self.params["update"]["resource"]: 
                src = open(self.previous_stage, 'rb').read()
                        
                # navigate to solution directory
                oldcwd = os.getcwd()
                os.chdir(self.params["project_path"])
                dst = os.path.join(self.params["project_path"], self.params["update"]["resource"]["dst"])
                f = open(dst, 'wb+')
                f.write(src)
                f.close()
                os.chdir(oldcwd)

        # build sln
        oldcwd = os.getcwd()
        os.chdir(self.params["project_path"])
        msbuild_cmd = self.params["msbuild_path"] + " /t:Clean,Build /property:Configuration=Release"
        msbuild_proc = Popen(msbuild_cmd, stdout=PIPE)
        output = msbuild_proc.communicate()
        print(output[0].decode("utf-8"))
        result = output[0].decode("utf-8").split('\n')
        
        # extract path of output file from results (this is so ugly im sorry)
        for line in result:
            if "->" in line: 
                output_file = line.split(' ')[4].rstrip('\n').rstrip('\r')
                break

        os.chdir(oldcwd)
        return output_file
        

    def build(self, build_directory):
        compiled_path = self.run_command()
        compiled_name = compiled_path.split('\\')[-1]
        out_file = "{0}/{1}".format(build_directory, compiled_name)
        shutil.copyfile(compiled_path, out_file)
        return out_file