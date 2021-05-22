
### Development server
=====================================================
Firstly install dependencies.
> pip{python_version} install -r requirements.txt -c constraints.txt
 
Change workdir to app and execute the below command.
> uvicorn main:App.service --reload

=======================================================

You can specify app root instead of changing workdir.
> uvicorn --app-dir /path/to/be-exec main:App.service --reload

You can run on specific port instead of deafult 8000.
> uvicorn --app-dir /path/to/be-exec main:App.service --reload --port 8080
