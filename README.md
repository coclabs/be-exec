
### Development server
Change workdir to app and execute the below command
> uvicorn main:App.service --reload

=======================================================

You can specify app root instead of changing workdir
> uvicorn --app-dir /path/to/be-exec main:App.service --reload
