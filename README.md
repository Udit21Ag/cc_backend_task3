# cc_backend_task3

Task: [Recruitment Task 3.pdf](https://github.com/user-attachments/files/16165774/Recruitment.Task.3.pdf)

Steps to make a django project for the above task: 

1. Download Docker (https://www.docker.com/get-started/)
2. From Docker Hub (https://hub.docker.com/_/postgres) download the postgres official image
   ```
   docker pull postgres:latest
   ```
3. Make a docker container:
   ```
   docker run --name <container_name> -e POSTGRES_PASSWORD=<db_password> -d -p 5432:5432 postgres
   ```
4. Create an init.sql file that contains table schema.
5. Copy this init.sql into the docker container:
   ```
   docker cp init.sql <container_name>:/docker-entrypoint-initdb.d/
   ```
6. Connect Django server to the docker container by modifying settings.py file (Refer: https://github.com/Udit21Ag/cc_backend_task3/blob/00e8137d618f96f73924e0052e69f873192db61d/ccsql/ccsql/settings.py#L83)
7. To automatically create table relations as per the File model in models.py (Refer: https://github.com/Udit21Ag/cc_backend_task3/blob/main/ccsql/dbwork/models.py)
   ```
   python manage.py migrate
   ```
8. Make APIs to upload, retrieve and delete files (Refer: https://github.com/Udit21Ag/cc_backend_task3/blob/main/ccsql/dbwork/views.py)
