# Authentication-Flow-API
First learning project on Django, a authentication API includes as well some pages made using Bootstrap

### Pull code to your local machine
From a folder, perform `git clone https://github.com/jedpedregosa/Authentication-Flow-API.git`.

### Docker Setup
- From your command line interface, navigate to the main folder `cd Authentication-Flow-API`
- Perform `docker build -t auth-flow-app .` to instantiate docker, this might require time.
- Execute `docker-compose up -d` to start the docker container.
- Last, perform `docker-compose run authflow python manage.py migrate` to initiate the database.

## Rest API
- To access API use API platforms (Postman, ARC, etc.) for accessing APIs. APIs are accessible through URL: `/api/___` (ex. `http://localhost:8000/api/signup` to access the User Sign Up API).

## User Interface
- The interface is accessible through URL: `/__` (ex. `http://localhost:8000/signup` to display the Sign Up Form page).
