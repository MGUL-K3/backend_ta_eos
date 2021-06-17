# Запускаем backend
docker-compose up 

# Выполняем миграции
docker ps (выбрать id контейнера web)  
docker exec -it my_web_container_id /bin/sh  
python manage.py migrate  
exit  
