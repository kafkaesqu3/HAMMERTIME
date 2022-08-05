import shutil
import sys
import math
import os
import random
from stage_builders.stage import Stage

class EncryptXOR(Stage): 

    def generate_key(self, size, divider):
        random_bytes = bytes([random.randrange(0, 256) for _ in range(0, math.floor(size / divider ))])
        return random_bytes

    def xor_encrypt(self, text, key, byteorder=sys.byteorder):   
        output = []
        
        for i in range(len(text)):
            xor_num = text[i] ^ key[i % len(key)]
            output.append(xor_num)
        return bytes(output)
        key, text = key[:len(text)], text[:len(key)]
        int_var = int.from_bytes(text, byteorder)
        int_key = int.from_bytes(key, byteorder)
        int_enc = int_var ^ int_key
        return int_enc.to_bytes(len(text), byteorder)

    def xnor_encrypt(self, text, key, byteorder=sys.byteorder):
        print("This broken AF")
        return
        output = []
        
        for i in range(len(text)):
            xor_num = text[i] ^ key[i % len(key)]
            output.append(xor_num)
        return bytes(output)

        key, text = key[:len(text)], text[:len(key)]
        int_var = int.from_bytes(text, byteorder, signed=True)
        int_key = int.from_bytes(key, byteorder, signed=True)
        int_enc = ~(int_var ^ int_key)
        return int_enc.to_bytes(len(text), byteorder, signed=True)
        




    def run_command(self):
        print(self.previous_stage)
        cleartext = open(self.previous_stage, 'rb').read()
        if self.params["generate_key"] == True: 
            key = self.generate_key(len(cleartext), 10) # key 10% of text
            f = open(self.params["password_file"], 'wb+')
            f.write(key)
            f.close()
        key_location = self.params["password_file"]
        k = open(key_location, 'rb')
        keybytes = k.read()
        
        # warn operator if key is much smaller than whats being encrypted, this is NOT safe
        margin = len(cleartext) / 2
        if len(keybytes) + margin < len(cleartext): 
            print("WARNING: The key is really small. try a larger key. Set unsafe to true in config if this is really what you want")
        
        mode = self.params["mode"]
        if mode == "xor": 
            results = self.xor_encrypt(cleartext, keybytes)
        elif mode == "xnor": 
            results = self.xnor_encrypt(cleartext, keybytes)
        else: 
            print("Config error - wrong mode")

        return results

    def build(self, build_directory):
        ciphertext = self.run_command()
        out_file = "{}/xor.bin".format(build_directory)
        shutil.copy(self.params["password_file"], os.path.join(build_directory, "key"))
        output = open(out_file, "wb")
        output.write(ciphertext)
        output.close()
        return out_file