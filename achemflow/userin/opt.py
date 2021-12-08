import os
import json

class choose_opt:
    def __init__(self,file,todo_num,method_num):
        self.file = file
        self.todo = self.to_ch(todo_num)
        self.method = self.met_ch(method_num)
    
    def to_ch(self,inp):
        dic = {1:"opt" ,2:"opt/freq" ,3:"nmr=giao" ,4:"opt/freq=IR"}
        return dic[inp]

    def met_ch(self,inp):
        dic = {1:"b3lyp/6-31gd",2:"b3lyp/6-311gd2p"}
        return dic[inp]

class compute_use:
    def __init__(self):
        mes = self.make_json()
        self.cpus = mes[0]
        self.mems = mes[1]

    def make_json(self):
        homedir = os.environ['HOME']
        if os.path.exists(f"{homedir}/.config/achemflow/gw_setting.json") == 1:
            with open(f"{homedir}/.config/achemflow/gw_setting.json") as f:
                json_mes = json.load(f)
            try:
                cpu = json_mes["compute_resourse"]["use_cpus"]
                mem = json_mes["compute_resourse"]["use_mems"]
                return [cpu,mem]
            except:
                raise IOError
        else:
            os.makedirs(f"{homedir}/.config/achemflow")
            with open(f"{homedir}/.config/achemflow/gw_setting.json","a+") as f:
                init_data = {"compute_resourse":{"use_cpus":"1","use_mems":"1 GB"}}
                json_data = json.dumps(init_data, sort_keys=True, indent=4, separators=(',', ': '))
                f.write(json_data)
            f.close()
            return [1, 1]
