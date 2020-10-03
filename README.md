# Boilerplate App
This App is meant to act as a boilerplate for upcoming projects.

## Setup
- create virtual env `pipenv shell --python 3.8`
- install requirements `pip install -r requirements.txt`
- to create a user, first run `manage.py migrate`
- create an admin `manage.py createsuperuser`
- run dev server `manage.py runserver`

## Azure deployment via CLI
- make sure, that migrations have been created with `manage.py makemigrations` before creating the webapp
- Login to Azure `az login`
- Create Azure PostgresDB resource
```
az postgres up 
    --resource-group <resource group name> 
    --location <location: e.g. germanywestcentral> 
    --sku-name <sku_name: e.g. B_Gen5_1> 
    --server-name <server_name> 
    --database-name <db_name> 
    --admin-user <admin_username> 
    --admin-password <admin_pw> 
    --ssl-enforcement Enabled
```
- Create Azure Webapp resource
  - this command will later be used to deploy updates
```
az webapp up 
    --resource-group <resource group name> 
    --location <location: e.g. germanywestcentral> 
    --plan DjangoPostgres-tutorial-plan 
    --sku <sku: e.g. B1> 
    --name <webapp_name>
```
- If necessary, create environmental variables (in the webapp environment)
```
az webapp config appsettings set 
    --settings 
        DJANGO_ENV="production" 
        DBHOST="<db-server_name>.postgres.database.azure.com" 
        DBNAME="<db_name> " 
        DBUSER="<admin_username>@<db-server_name>" 
        DBPASS="<pw>"
```

## ToDo's
- [ ] Add basic models for necessary pages
- [ ] Add rest_framework support