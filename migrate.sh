mysql --user="root" --password="123456" -e "drop database catalog_item"
mysql --user="root" --password="123456" -e "create database catalog_item"

source activate flask-env
export FLASK_APP=/Users/jerryle/Projects/moocs/fullstack/projects/catalog-item-backend-api/autoapp.py
rm -rf migrations
flask db init
flask db migrate
flask db upgrade
