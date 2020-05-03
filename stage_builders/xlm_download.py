from stage_builders.stage import Stage

class XLM_Download(Stage): 
    def build(self, build_directory):
        url = self.params['URL']
        path = self.params['path']
        f = open('templates/excel_4_0/URLDOWNLOADTOFILE.txt', 'r')
        template = f.read()
        template = template.replace("___URL_MARKER___", url)
        template = template.replace("___PATH_MARKER___", path)
        print(template)
        return template
