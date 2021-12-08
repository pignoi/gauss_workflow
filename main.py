import achemflow.readfile.xyz as xyz
import achemflow.userin.opt as opt

a = "test.xyz"
b = 1
c = 1

user = opt.choose_opt(a,b,c)
mechine = opt.compute_use()

a = xyz.xyzReader(user.file,user.todo,user.method,mechine.cpus,mechine.mems)
