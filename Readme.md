# End to End Kidney Disease Detection

This is a production level project building an end to end kidney disease classification pipeline

## Workflows

1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. Update the app.py

### Steps:

clone the respository

```bash
https://github.com/SepNem32bit/End-to-End-Kidney-Disease-Classification.git
```

### Step 1- Create a virtual environment

```bash
python -m venv myenv
```

```bash
.\myenv\Scripts\activate
```

### Step 2- Install the requirements
```bash
pip install -r requirements.txt
```


## Deployment

EC2 access : It is virtual machine

ECR: Elastic Container registry to save your docker image in aws


### Steps

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

### Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess