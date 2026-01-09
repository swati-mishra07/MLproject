## END to END DataScience Project
import dagshub
dagshub.init(repo_owner='swati-mishra07', repo_name='MLproject', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)