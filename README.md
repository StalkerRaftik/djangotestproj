# djangotestproj

# Usage:
1. Move to repository root folder;
2. Run `docker-compose up --build`;
3. Run `docker ps` and find `image_id` for `web` contanter
4. Apply migrations via `docker exec -it container_id python manage.py migrate`
