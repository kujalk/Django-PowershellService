1. Install all packages as in requirements.txt
2. Install Redis
    - Installed WSL (Windows SubSystem for Linux)
    - Install Ubuntu Distro
    - Update apt-get packages
    - Install Redis
    - Start Redis
    - Check Redis is up and Running

Architecture
--------------
- Producer -> Celery Beat
- Consumer -> Celery Worker
- Broker(Queue) -> Redis

3. Start Web
   - pipenv shell
   - cd mcafee
   - python manage.py migrate
   - python manage.py runserver
4. Producer
   - pipenv shell
   - cd mcafee
   - celery -A mcafee beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
5. Consumer
   - pipenv shell
   - cd mcafee
   - celery -A mcafee worker --pool=solo  --loglevel=info