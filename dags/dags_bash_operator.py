from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

import datetime
import pendulum

with DAG(
    dag_id="dags_bash_operator",
    # 분 시 일 월 요일
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 8, tz="Asia/Seoul"),
    catchup=False,                                  # 시작 시간부터 현재까지 다 돌릴 것인가
    dagrun_timeout=datetime.timedelta(minutes=60),  # 타임아웃 시간
    tags=["example", "example2"],                   # 옵션
    params={"example_key": "example_value"},
) as dag:
    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoAmI",
    )

    # [START howto_operator_bash]
    bash_t2 = BashOperator(
        task_id = "bash_t2",
        bash_command = "echo $HOSTNAME",
    )

    bash_t1 >> bash_t2