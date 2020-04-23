from stage_builders.stage import Stage

class Shellcode_Injection(Stage): 
   
    def set_template(self, template_name):
        filepath = "templates/shellcode_injection/{}/{}.cs".format(template_name, template_name)
        x86_process = self.params['process']['x86_process_name']
        x86_shellcode = self.params['shellcode_x86']['shellcode_val']
        x64_process = self.params['process']['x64_process_name']
        x64_shellcode = self.params['shellcode_x64']['shellcode_val']
        try: 
            f = open(filepath, 'r')
        except: 
            print("cannot open template file")
            return False

        template = f.read()
        template = template.replace("___X86_PROCNAME_MARKER___", x86_process)
        template = template.replace("___X86_SHELLCODE_MARKER___", x86_shellcode)
        template = template.replace("___X64_PROCNAME_MARKER___", x64_process)
        template = template.replace("___X64_SHELLCODE_MARKER___", x64_shellcode)
        print(template)

    def build(self):
        self.set_template(self.params['injection_type'])