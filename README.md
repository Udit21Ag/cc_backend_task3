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
6. Connect Django server to the docker container by modifying settings.py file (Refer: https://github.com/Udit21Ag/cc_backend_task3/blob/6f7c32eb565e2b2e6469375d855f232f3b3adf31/ccsql/ccsql/settings.py#L77-L86C2)
7. To automatically create table relations as per the File model in models.py (Refer: https://github.com/Udit21Ag/cc_backend_task3/blob/main/ccsql/dbwork/models.py)
   ```
   python manage.py migrate
   ```
8. Make APIs to upload, retrieve and delete files (Refer: https://github.com/Udit21Ag/cc_backend_task3/blob/main/ccsql/dbwork/views.py)
9. To upload a file, do a POST request and upload it using request.FILES as it contains all the uploaded files and then, save the file using file.save()
10. To retrieve a file, do a GET request and retrieve using objects.get(name=filename) (if filename is unique). In case of duplicate files, use objects.filter(name=filename).first()
11. To delete a file, do a DELETE request and delete all duplicates of a file using objects.filter(name=filename).delete()

12. Run the django project server using:
   ```
   python manage.py runserver
   ```
13. To upload a file:
    ```
     curl -X POST -F "file=@<file_path>" http://localhost:8000/upload/
    ```
14. To retrieve a file:
    ```
    curl -X GET http://localhost:8000/retrieve/<file_name>/
    ```
15. To delete a file:
    ```
    curl -X DELETE http://localhost:8000/delete/<file_name>/
    ```
