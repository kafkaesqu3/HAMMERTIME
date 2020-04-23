import os
import subprocess
from stage_builders.stage import Stage

class Gadget2JScript(Stage): 
    def run_command(self):
        print(self.previous_stage)
        g2js_path = "{}\\tools\\GadgetToJScript\\GadgetToJScript.exe".format(os.getcwd())
        outfile_name = "output"
        g2js_args = "-w {scriptType} -i {input} -r {references} -o {output}".format(
            scriptType=self.params['format'],input=self.previous_stage, references = self.params['runtimes'], output=outfile_name)
        g2js_cmd = "{} {}".format(g2js_path, g2js_args)
        print(g2js_cmd)
        #g2js_cmd = "whoami > {}".format(outfile_name)
        g2js_proc = subprocess.Popen(g2js_cmd)
        g2js_proc.wait()
        print(os.getcwd())
        output_read = open('output.{}'.format(self.params['format']), 'r')
        macro = output_read.read()
        output_read.close()
        os.remove('output.{}'.format(self.params['format']))
        print(macro)
        return macro

    def build(self, build_directory):
        macro = self.run_command()
        out_file = "{}/macro.txt".format(build_directory)
        output = open(out_file, "w")
        output.write(macro)
        return out_file