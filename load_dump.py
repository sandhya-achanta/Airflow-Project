from airflow import DAG
from airflow.operators import BashOperator, HiveOperator
from datetime import datetime, timedelta
default_args = {
    'owner': 'avi',
     'start_date': datetime.now() - timedelta(minutes=1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

#dag = DAG('load_test', default_args=default_args)


dag = DAG('load_test',schedule_interval=timedelta(minutes=60),default_args=default_args)




load_job = """sh load.sh"""

# Importing the incremental data from Mysql table to HDFS
task1 = BashOperator(
        task_id= 'load_import',
	bash_command='./load.sh',
        dag=dag)