import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from achemflow.readfile import xyz
from achemflow.userin import opt
from achemflow.dealwen import check,optC

import datetime as dt
import json
import os

dag = DAG(
    dag_id="gausswork",
    start_date=dt.datetime(2021, 12, 4),
    tags=["own"]
)

# 获取计算模式，采用的计算方法等信息
def met():
    methods = opt.choose_opt("/root/test.xyz",1,1)
    init_data = {"file":methods.file ,"todo":methods.todo ,"method":methods.method }
    json_data = json.dumps(init_data,sort_keys=True, indent=4, separators=(',', ': '))
    with open("method.json","a+") as f:
        f.seek(0)
        f.truncate()
        f.write(json_data)
    f.close()

met_choose = PythonOperator(
    task_id="met_choose",
    python_callable=met,
    dag=dag,
)

# 获取计算使用的计算机资源，相关的设置在~/.config/achemflow/gw_setting.json文件下面进行更改
def mach():
    machine = opt.compute_use()
    init_data = {"cpus":machine.cpus ,"mems":machine.mems}
    json_data = json.dumps(init_data,sort_keys=True, indent=4, separators=(',', ': '))
    with open("machine.json","a+") as f:
        f.seek(0)
        f.truncate()
        f.write(json_data)

machine_choose = PythonOperator(
    task_id = "machine_choose",
    python_callable=mach,
    dag=dag,
)

# 生成计算文件，计算文件和输入的原始文件处于相同目录下

def file_pull():
    with open("method.json") as f1:
        user = json.load(f1)
    with open("machine.json") as f2:
        machine = json.load(f2)
    compute_file = xyz.xyzReader(user["file"],user["todo"],user["method"],machine["cpus"],machine["mems"])
    output_file = ".".join(compute_file.split(".")[:-1])
    json_data = json.dumps({"compute_file":compute_file, "output_file":output_file})
    with open("compute.json","a+") as f3:
        f3.seek(0)
        f3.truncate()
        f3.write(json_data)

file_make = PythonOperator(
    task_id="file_make",
    python_callable=file_pull,
    dag=dag,
)

# 提交计算任务
def submit():
    with open("compute.json") as f:
        info = json.load[f]
    compute_file = info["compute_file"]

    os.system(f"g16 {compute_file}")

submit_file = PythonOperator(
    task_id = "task_submit",
    python_callable=submit,
    dag = dag
)

# 检查计算文件

def deal():
    with open("compute.json") as f:
        info = json.load[f]
    output_f = info["output_file"]
    check_num = check.checkFile(output_f)
    if check_num == 1:
        result = optC.optResult(output_f)
        energy = result.energy
        atoms = result.atomPosition
        dipole = result.dip
    with open("/root/result.txt","a+") as f:
        f.write(energy)
        f.write(atoms)
        f.write(dipole)
    
deal_file = PythonOperator(
    task_id = "deal_result",
    python_callable=deal,
    dag = dag
)

def mi():
    with open("compute.json") as f:
        info = json.load[f]
    output_f = info["output_file"]
    check_num = check.checkFile(output_f)

    if check_num == 1:
        print("OK")
    if check_num == 0:
        print("NO")

mind = PythonOperator(
    task_id = "result_mind",
    python_callable=mi,
    dag = dag
)

met_choose >> machine_choose >> file_make >> submit_file
submit_file >> deal_file >> mind 
submit_file >> mind

