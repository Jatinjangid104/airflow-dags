FROM apache/airflow

# Copy DAGs from ./data/dags to /mnt/dags
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip search apache-airflow-providers-python
RUN pip install apache-airflow-providers-python
RUN pip install -r requirements.txt