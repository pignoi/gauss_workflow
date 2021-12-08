class optResult:
    def __init__(self,outFile):
        self.dealFile = outFile
        ins = self.getMes()
        self.energy = ins["energy"]
        self.atomPosition = ins["atoms"]
        self.dip = ins["dipole"]
        # self.diproad = ins["dipole_road"]
        self.enroad = ins["energy_road"]

    def getMes(self):

        am_lis = []
        en_lis = []
        dip_lis = []

        with open(self.dealFile) as f:
            lines = f.readlines()
            for i,line in enumerate(lines):
                if 'NAtoms' in line:
                    num = eval(line.split()[1])        # 确定计算体系计算的原子个数，方便后续确定文件结构
                if 'Standard orientation:' in line:
                    am_lis.append(i)                   # 确定优化后的结构信息起始行所在位置，最大值即为最终的优化结果
                if "SCF Done" in line:
                    en_lis.append(i)
                if "Dipole moment" in line:
                    dip_lis.append(i)
                
            am_max = max(am_lis)
            en_max = max(en_lis)
            dip_max = max(dip_lis)

            am_fin = lines[am_max+5:am_max+5+num]
            en_fin = lines[en_max].split()[4]
            dip_fin = [ lines[dip_max+1].split()[i] for i in [1,3,5,7] ]

            en_road = [lines[i].split()[4] for i in en_lis]
            # dip_road = [lines[i].split("")[1,3,5,7] for i in dip_lis]

            dic = {"atoms":am_fin,"energy":en_fin,"dipole":dip_fin,
            "energy_road":en_road}#"dipole_road":dip_road}

        return dic

if __name__ == "__main__":
    a = optResult("/Users/cxmac/Desktop/78_data.log")
    z = a.energy
    print(z)