from airflow.operators import BashOperator, PythonOperator, HiveOperator
from airflow.models import DAG
from datetime import datetime, timedelta

default_args = {
    'owner': 'sandhya',
    'start_date': datetime.now() - timedelta(minutes=1),
    'email': [],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG('practical_project_dag',
          default_args=default_args, schedule_interval=None,
          start_date=datetime.now() - timedelta(minutes=1))
data_load = BashOperator(
    task_id='data_load',
    bash_command="""python /root/airflow/dags/practical_exercise.py --load_data """,
    dag=dag)

csv_creation = BashOperator(
    task_id='csv_creation',
    bash_command="""python /root/airflow/dags/practical_exercise.py --create_csv
    mv user_upload_dump.*.csv /home/cloudera/airflow/csv_files/user_upload_dump.$(date +%s)
 """,
    dag=dag)
