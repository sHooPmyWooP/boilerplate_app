# Boilerplate App
This App is meant to act as a boilerplate for upcoming projects.

## Setup
- create virtual env `pipenv shell --python 3.8`
- install requirements `pip install -r requirements.txt`
- create an admin `manage.py createsuperuser`
- run dev server `manage.py runserver`

## Azure deployment via CLI
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

## ToDo's
- [ ]Add basic models for necessary pages
- [ ]Add rest_framework support