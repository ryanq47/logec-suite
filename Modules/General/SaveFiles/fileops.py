from zipfile import ZipFile

from datetime import datetime, timezone
import os, sys
from shutil import make_archive, unpack_archive

class SaveFiles:
    def __init__(self):
        pass
        
    
    def save_framework(self, options):
        action, self.filename = options
        
        self.sys_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.time = datetime.now(timezone.utc)
        
        if action == "load":
            self.loadfile()
        elif action == "save":
            self.savefile()
        
    def createfile(self):
        os.mkdir(f'{self.sys_path}/Modules/General/SaveFiles/Projects')
        os.mkdir(f'{self.sys_path}/Modules/General/SaveFiles/.tmp_projectfolder')
    
    def savefile(self):
        print(self.filename)
        make_archive(self.filename,'zip',f'{self.sys_path}/Modules/General/SaveFiles/.tmp_projectfolder/')

    def loadfile(self):
        unpack_archive(self.filename, f'{self.sys_path}/Modules/General/SaveFiles/.tmp_projectfolder/','zip')
        
        ## Returning path of loaded file
        #return f'{self.sys_path}/Modules/General/SaveFiles/.tmp_projectfolder/'


