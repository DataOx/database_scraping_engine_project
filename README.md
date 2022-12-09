Parser project of the Summer School for parsing data from the site
https://www.oxford-royale.com/ every 24 hours.
The data points are date, gender, name, and country.
The project has automation for populating GoogleSheets and populating Postgres database. Data is sent from Postgres to Google Data Studio (this is the dashboard for the project).
The automation system is implemented using celery beat.
The project is deployed on the client server and runs in docker.
## Architecture
![image](https://user-images.githubusercontent.com/119062788/206763712-00c0fc40-f020-4e89-8403-b87737724718.png)
