from airflow import DAG
from airflow.operators import BashOperator, HiveOperator
from datetime import datetime, timedelta
default_args = {
    'owner': 'avi',
     'start_date': datetime.now() - timedelta(minutes=1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}
dag = DAG('load_csv',schedule_interval=timedelta(minutes=60),default_args=default_args)

load_job = """sh load_csv.sh"""

# Importing the incremental data from Mysql table to HDFS
task1 = BashOperator(
        task_id= 'load_csv_import',
        bash_command='./load_csv.sh',
        dag=dag)
~                                                                                                                                                                                                                                            
~                               