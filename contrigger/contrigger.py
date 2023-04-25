from datetime import timedelta
from airflow.timetables.trigger import CronTriggerTimetable
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@weekly',
}

dag = DAG('tutorial', catchup=False, default_args=default_args)



@dag(
    # Executa toda segunda feira, uma vez por semana.
    schedule=CronTriggerTimetable(
        "0 0 * * 1",
        timezone="UTC",
    ),
    ...,
)
def example_dag():
    pass


@dag(
    # 
    schedule=CronTriggerTimetable(
        "45 12 * * 1",
        timezone="UTC",
        interval=timedelta(mounths=2),
    ),
    ...,
)
def example_dag():
    pass