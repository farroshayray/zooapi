# Zoo Management API by Farros
### This API is designed to manage a zoo, with features to add, remove, and list animals and staff
- [farroshayray API link](https://enthusiastic-beaver-farroshayray-fa549bb9.koyeb.app/)  
- [documentation for zooapi](https://documenter.getpostman.com/view/37782623/2sAXxLBE2C)

There are 3 major steps to do:  
- [Create The Flask Project](#section1)  
- [Create Docker Image File](#section2)
- [Create Test](#section3)
- [Deploy API to Koyeb](#section4)
## <h2 id="section1">Section 1: Create The Flask Project</h2>

1. Install Poetry
```bash
pip install poetry
```
2. Create a new project using Poetry
```bash
poetry new zooapi --name src
```
3. Add Flask project
- this command will makes a .venv folder
```bash
poetry add flask
```

4. Run virtual environment
```bash
poetry shell
```
or
```bash
.\.venv\Scripts\activate
```
5. create `main.py` file in the root
6. add example lines to the main.py
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Hello World !!</h1>"
```
7. save the project
8. Run the Flask app
where `main` is your `.py` file to run
```bash
Flask --app main run
```
## <h2 id="section2">Section 2: Create Docker Image File</h2>

1. install Docker to your PC [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Create a new file called `Dockerfile` in the root of your project (no extension needed)
3. Make sure your project structure required `Dockerfile`, `main.py`,`poetry.lock`, `pyproject.toml`, `requirements.txt` and `README.md` in the root of the project
```csharp
zooapi/
├── Dockerfile
├── main.py
├── poetry.lock
├── pyproject.toml
├── requirements.txt
└── README.md
```
4. Add this lines to your `Dockerfile`
```Dockerfile
# Stage 1: Base image with Python 3.12 and Poetry installation
FROM python:3.12-slim-bookworm AS base

# Install Poetry
RUN pip install poetry

# Set environment variables for Poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Add Poetry to the system PATH
ENV PATH="$PATH:$POETRY_HOME/bin"

# Stage 2: Build stage
FROM base AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the pyproject.toml file to the container
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry install --only=main

# Copy the rest of the application code
COPY . .

# Stage 3: Runtime stage
FROM base AS runtime

# Set the working directory inside the container
WORKDIR /app

# Copy all built files from the build stage to runtime stage
COPY --from=build /app /app

# Activate the virtual environment created by Poetry
ENV PATH="/app/.venv/bin:$PATH"
RUN echo "source /app/.venv/bin/activate" >> /etc/profile.d/venv.sh

# Expose the port 5000 for Flask
EXPOSE 5000

# Set the default command to run the Flask app
CMD ["flask", "--app", "main", "run", "--host", "0.0.0.0"]
```
5. Build docker image
- with this step you can check 'images' in your Docker desktop
- zooapi can be replaced with your project name folder
```bash
docker build -t zoobase:latest .
```
6. Run Docker Container
- zooapi can be replaced with your project name folder
```bash
docker run -d -p 5000:5000 zoobase:latest
```
7. Run localhost:5000 or click the port in the Containers of Docker desktop
8. if you want to deploy on [Koyeb](https://app.koyeb.com/) you don't have to do step number 5-7  

## <h2 id="section3">Section 3: Add Tests and Finish Important Test Coverage</h2>  
1. install `pytest` and `coverage`
```bash
poetry add pytest coverage
```
2. create folder `tests` in the root of the project
3. create `conftest.py` file in the root of the project
4. create `pytest.ini` file in the root of the project
5. Add initial configuration in the `pytest.ini` file
```ini
[pytest]
addopts = -s
```
6.create first test in `test_<testname>.py` file inside the `tests` folder and try this for the first test
```python
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
```
7. run the first test
```bash
pytest
```
the pytest will automatically detect `functions`, `filenames`, `folders`, that have word `test_` in the initial word, for example:  
```
└── 📁tests
    └── 📁animals
        └── test_animals_delete.py
        └── test_animals_exception.py
        └── test_animals_get_all.py
        └── test_animals_get_id.py
        └── test_animals_post.py
        └── test_animals_put.py
    └── 📁employees
        └── test_employees_delete.py
        └── test_employees_exception.py
        └── test_employees_get_all.py
        └── test_employees_get_id.py
        └── test_employees_post.py
        └── test_employees_put.py
    └── __init__ copy.py
    └── __init__.py
    └── test_main.py
    └── test_trial.py
```
8. run coverage test
```bash
coverage run -m pytest
```
9. run coverage report  
to get the test report, and to know the percentages of tests that we cover in our project
```bash
coverage report
```
10. get detail report of coverage  
to know codes covered and missed by your tests, we use
```bash
coverage html
```
it will show you the detail of which lines covered by your test and which lines of codes you missed it

## <h2 id="section4">Section 4: Deploy API to [Koyeb](https://app.koyeb.com/)</h2>
1. Create a [github](https://github.com) repository and push your project. remember, push the project file, not the folder of the project file
2. Create a [Koyeb](https://app.koyeb.com/) account and sign up with github
3. Login Koyeb
4. Create new service using github repositories
5. Choose your repository to deploy
6. Choose your plan and click next
7. Change Builder to Dockerfile
8. Change Exposed Ports to 5000
9. Change Health check configured on ports to 5000
10. Deploy