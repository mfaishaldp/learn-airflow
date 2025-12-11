from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner' : 'mfaishaldp',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v5',
    default_args = default_args,
    description='this is our first dag that we write',
    start_date=datetime(2021, 7, 30, 2),
    schedule='@daily'
) as dag :
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command="echo hello world, this is the first task!"
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = "echo hey, i am task2 and will be running after task1"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo hey, i am task3 and will be running after task2"
    )

    #task depenndency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)


    # task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # task dependency methood 3
    task1 >> [task2, task3]