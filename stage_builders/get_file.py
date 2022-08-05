import os
from stage_builders.stage import Stage

# Simply reads a file in. usually to start off the chain
class GetFile(Stage): 

    def run_command(self):
        isBinary = self.params["binary"]
        if isBinary == True: 
            f = open(self.params["path"], 'rb')
        else: 
            f = open(self.params["path"], 'r')
        output = f.read()
        f.close()
        return output
        

    def build(self, build_directory):
        stage = self.run_command()
        out_file = "{}/initialstage".format(build_directory)
        output = open(out_file, "wb")
        output.write(stage)
        return out_file