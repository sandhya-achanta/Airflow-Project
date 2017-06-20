from airflow import DAG
from airflow.operators import BashOperator, HiveOperator
from datetime import datetime, timedelta
default_args = {
    'owner': 'avi',
     'start_date': datetime.now() - timedelta(minutes=1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('practical_exercise',schedule_interval=timedelta(minutes=60),default_args=default_args)

# Importing the incremental data from Mysql table to HDFS
task1 = BashOperator(
        task_id= 'load_csvfile_import',
        bash_command='./load_csv.sh',
        dag=dag)
# Importing the incremental data from Mysql table to HDFS
task2 = BashOperator(
        task_id= 'load_tables_import',
        bash_command='./load_tables.sh',
        dag=dag)
# Importing the incremental data from Mysql table to HDFS
task3 = BashOperator(
        task_id= 'reporting_tables',
        bash_command='./reporting_tables.sh',
        dag=dag)
