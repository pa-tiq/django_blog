# django_blog

Create and activate virtual environment:
```bash
conda create --name django_blog django 
activate django_blog
pip install -r requirements.txt
```

Create and run migrations:
```bash
py manage.py migrate
py manage.py makemigrations blog
py manage.py makemigrations auth_app
py manage.py migrate
```

Run the server:
```bash
py manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) to view it in your browser.
