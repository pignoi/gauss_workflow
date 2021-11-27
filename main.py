import readfile.xyz
import userin.opt

a = "test.xyz"
b = 1
c = 1

user = userin.opt.choose_opt(a,b,c)
mechine = userin.opt.compute_use()

a = readfile.xyz.xyzReader(user.file,user.todo,user.method,mechine.cpus,mechine.mems)


