# How to setup your project

Before starting any project, the first step is to systemize. Meaning categorizing folders, creating a virtual environment specifically for that project etc.

 

- Create a folder(root)) which will have all the other folders related to your project.

```bash
mkdir newProject
cd newProject
```

- In that folder create a virtual environment and install required packages.

```bash
virtualenv newenv
cd Scripts
source ./activate
```

```bash
pip install Fastapi
pip install 'uvicorn[standard]'
```

- Create a requirements.txt file; contains all the packages required for the project with specified versions mentioned

```bash
pip freeze > requirements.txt
```

- Now you can create your categorize folder in your folder. For example: I have many models in my root folder. So I create a new folder which will contain all the models

```bash
mkdir models
rm road.py newProject/models/road.py
```