# djangotestproj

# Usage:
1. Move to repository root folder;
2. Run `sudo docker-compose up --build`;
3. Run `sudo docker ps` and find `container_id` for `web` contanter;
4. Apply migrations via `sudo docker exec -it container_id python manage.py migrate`;
5. Go to `0.0.0.0:8000/admin`;
6. Use login:pass `admin:admin` to access admin panel;
7. Done!
