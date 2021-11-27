import os

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
        self.cpus = self.make_json()[0]
        self.mems = self.make_json()[1]

    def make_json(self):
        if os.path.exists("gw_setting.json") == 1:
            with open("gw_setting.json") as f:
                ins = f.readlines()
            try:
                cpu = int(eval(ins[0].split("=")[-1]))
                mem = ins[1].split("=")[-1]
                return [cpu,mem]
            except:
                raise IOError
        else:
            with open("gw_setting.json","a+") as f:
                f.write("use_cpus = 1\n")
                f.write("use_mem =  1 GB")
            return [1, 1]