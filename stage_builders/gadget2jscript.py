from stage_builders.stage import Stage

class Gadget2JScript(Stage): 
    def run_command(self):
        g2js_path = "tools/GadgetToJScript/GadgetToJScript.exe"
        g2js_args = ""

    def build(self):
        self.run_command()