Backend Sharing Vision

Stack : Python Django Framework, MySql

Install configuration :
- Mysql : pip install mysqlclient
- Django : pip install django
- Django REST Framework : pip install djangorestframework


Instalation :
- Clone repository
- Open repository in your code editor
- Make sure the database settings in microservice/settings.py are correct, like ENGINE, NAME, USER, PASSWORD
- Create the initial database migrations/Apply the migrations to MySQL: : python manage.py migrate
- Create migrations for your model changes : python manage.py makemigrations articles
- Apply the migrations to your database : python manage.py migrate articles
- Run : python manage.py runserver (like http://127.0.0.1:8000/)
- Test your API 

Testing with Postman
1. Create a New Article (POST /article/)

URL: http://127.0.0.1:8000/article/
Method: POST
Body (raw, JSON):
json
Copy code
{
  "title": "The title must be at least 20 characters long",
  "content": "The content must be at least 200 characters long.",
  "category": "The category must be at least 3 characters long.",
  "status": "publish/draft/thrash"
}
Headers:
Content-Type: application/json

2. List Articles with Pagination (GET /article/<limit>/<offset>/)

URL: http://127.0.0.1:8000/article/10/0/
Method: GET
This URL fetches the first 10 articles starting from the first article.

3. Retrieve an Article (GET /article/<id>/)

URL: http://127.0.0.1:8000/article/1/
Method: GET
This URL fetches the article with ID 1.

4. Update an Article (PUT or PATCH /article/<id>/)

URL: http://127.0.0.1:8000/article/1/
Method: PUT or PATCH
Body (raw, JSON):
json
Copy code
{
  "title": "Updated Title ",
  "content": "Updated content .",
  "category": "Updated category",
  "status": "Updated status"
}
Headers:
Content-Type: application/json

5. Delete an Article (DELETE /article/<id>/)

URL: http://127.0.0.1:8000/article/1/
Method: DELETE
