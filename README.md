# Pets api

## Примечание
При экспорте данных через команду ``python manage.py export_pets`` ссылки на файлы будут формироваться по первому хосту в ALLOWED_HOSTS


### Развертывание проекта

- Скопировать проект  
  
  ```bash
  git clone https://github.com/y0gurt-dv/WIS-Software-test-project.git
  ```

- Установка зависимостей
  
  ```bash
  pip install -r requirements.txt
  ```

- Создать файл .env

- Вынести константы в .env (пример есть в .env.example)
  
  ```
   SECRET_KEY=
   DEBUG=
   ALLOWED_HOSTS=
   ACCESS_API_KEY=
  
   DB_NAME=
   DB_USER=
   DB_PASS=
   DB_HOST=
   DB_PORT=
  ```

- Запуск миграций
  
  ```bash
  cd pets_api
  python manage.py makemigrations
  python manage.py migrate
  ```

- Запуск проекта
  
  ```bash
  python manage.py runserver
  ```

##### Запуск docker

- Создать файл .env

- Вынести константы в .env (пример есть в .env.example)
  
  ```
   SECRET_KEY=
   DEBUG=
   ALLOWED_HOSTS=
   ACCESS_API_KEY=
  
   DB_NAME=
   DB_USER=
   DB_PASS=
   DB_HOST=
   DB_PORT=
  ```

- Запуск docker
  ```bash
  docker-compose up --build -d
  ```
- Создание супер пользователя (при необходимости)
  ```bash
  docker exec <CONTAINER-ID> python manage.py init_admin --email test@test.com --username test --password test
  ```
