"""XYZ format
    [ comment line            ] !! NOT IMPLEMENTED !! DO NOT INCLUDE
    [ N                       ] # of atoms, required by this xyz reader plugin  line 1
    [ molecule name           ] name of molecule (can be blank)                 line 2
    atom1 x y z [optional data] atom name followed by xyz coords                line 3
    atom2 x y z [ ...         ] and (optionally) other data.
    ...
    atomN x y z [ ...         ]                                                 line N+2
"""

import os

class xyzReader:
    def __init__(self,file1,todo,method,cpus,mems):
        self.file = file1
        self.todo = todo        # 计算的目的，如结构优化、计算IR等等
        self.method = method    # 计算使用的泛函以及基组方法
        self.cpus = cpus
        self.mems = mems
        self.output = self.wr()

    def rd(self):
        with open(self.file) as f:
            lines = f.readlines()
        # 首先应当判断文件格式的合法性，问题是在于XYZ文件注释行如果是空行则不好判断
        def judge_start(lines):
            num = 0
            for i in lines:
                if i.split() != []:
                    return num
                else:
                    num += 1
        start_num = judge_start(lines)
        sta_lines = [i for i in lines[start_num+2:] if i.split() != []] 
        try:
            atom_num = eval(lines[0])
            if len(sta_lines) != atom_num:
                raise IOError
        except:
            raise IOError
        # 再依次读取文件中原子坐标的信息
        atoms = []
        for atom in sta_lines:
            atoms.append(f" {atom.split()[0]}    {atom.split()[1]}    {atom.split()[2]}    {atom.split()[3]}")    # 将原子坐标信息格式化输出
        atom_part = "\n".join(atoms)
        return atom_part

    def wr(self):
        final_name = self.file.split('.')[0] + ".gjf"
        with open(final_name,"a+") as f:
            f.seek(0)
            f.truncate()
            f.write(f"%cpu={self.cpus}\n")
            f.write(f"%mem={self.mems}\n")
            f.write(f"#{self.todo} {self.method}\n\n")
            f.write("Title card required\n\n")
            f.write("0 1\n")
            f.write(f"{self.rd()}\n\n")
            f.close()

        return final_name