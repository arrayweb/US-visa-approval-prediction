import os
from pathlib import Path
project_name = 'US-visa'
lists_of_files =[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py"
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/trainning_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirments.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py"
    "config/model.yaml",
    "config/schema.yaml"

]

for filepath in lists_of_files:
    filepath = Path(filepath)
    filder, filename = os.path.split(filepath)
    if filder != "":
     os.makedirs(filder, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
       with open(filepath, "w") as f:
          pass
    else:
       print(f"file is already present at {filepath}")