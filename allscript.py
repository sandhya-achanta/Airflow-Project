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
#loading user_report table		
task3 = BashOperator(
        task_id= 'user_report',
        bash_command='./user_report.sh',
        dag=dag)
		
#loading user_total table		
task4 = BashOperator(
        task_id= 'user_total',
        bash_command='./user_total.sh',
        dag=dag)
		
task1.set_downstream(task3)
task2.set_downstream(task3)		
task2.set_downstream(task4)		
