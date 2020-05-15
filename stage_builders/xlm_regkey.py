from stage_builders.stage import Stage

class XLM_Regkey(Stage): 
    def build(self, build_directory):
        pass
        
        # create
        # __REGKEY_MARKER___

        # set
        # =SetKeyValueDWORD(-2147483647, "___DWORD_KEYNAME_MARKER___", "___DWORD_KEYVAL_MARKER___", 4, ___DWORD_KEYDATA_MARKER___, 4)
        #=SetKeyValueSZ(-2147483647, "___SZ_KEYNAME_MARKER___", "___SZ_KEYVAL_MARKER___", 1, ___SZ_KEYDATA_MARKER___, ___SZ_KEYDATASIZE_MARKER___)

