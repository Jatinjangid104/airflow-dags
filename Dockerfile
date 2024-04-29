FROM apache/airflow

# Copy DAGs from ./data/dags to /mnt/dags
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./data/dags /opt/airflow/dags
