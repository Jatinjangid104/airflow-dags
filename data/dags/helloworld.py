from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class MultiplyBy5Operator(BaseOperator):
    @apply_defaults
    def __init__(self, my_operator_param, *args, **kwargs):
        self.my_operator_param = my_operator_param
        super(MultiplyBy5Operator, self).__init__(*args, **kwargs)

    def execute(self, context):
        # Your custom logic here
        result = self.my_operator_param * 5
        print(f'MultiplyBy5Operator result: {result}')
        return result

def print_hello():
    return 'Hello World'

dag = DAG('hello_world', description='Hello world example', schedule_interval='0 12 * * *', start_date=datetime(2017, 3, 20), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

multiplyby5_operator = MultiplyBy5Operator(my_operator_param='my_operator_param', task_id='multiplyby5_task', dag=dag)

dummy_operator >> hello_operator

dummy_operator >> multiplyby5_operator
