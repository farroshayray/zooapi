## Create The Flask Project
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
6. Run the Flask app
where `main` is your `.py` file to run
```bash
Flask --app main run
```

## Create Docker Image File
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
docker build -t zooapi:latest .
```
6. Run Docker Container
- zooapi can be replaced with your project name folder
```bash
docker run -d -p 5000:5000 zooapi:latest
```
7. Run localhost:5000 or click the port in the Containers of Docker desktop
8. finish