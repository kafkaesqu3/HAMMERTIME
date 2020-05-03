from stage_builders.stage import Stage

class XLM_Execute(Stage): 
    def build(self, build_directory):
        exec_method = self.params['exec_method']
        cmd = self.params['cmd']
        args = self.params['args']

        if exec_method in ["EXEC", "ShellExecute"]:
            filepath = "templates/excel_4_0/{}".format(exec_method)
        else:
            print("Exec method not supported")
            return False
        f = open(filepath, "r")
        template = f.read()
        template = template.replace("___CMD_MARKER___", cmd)
        template = template.replace("___ARGS_MARKER___", args)
        print(template)
        return template
        
