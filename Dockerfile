FROM python:3.12-slim  

RUN apt-get update && apt-get install -y \  
    gcc curl \  
    && rm -rf /var/lib/apt/lists/*  

RUN curl -sSL https://install.python-poetry.org | python3 -  

WORKDIR /app  

ENV PATH="/root/.local/bin:$PATH"  

COPY pyproject.toml poetry.lock ./  
RUN poetry install --no-root  

COPY . .  

EXPOSE 5000
CMD ["poetry", "run", "flask", "--app", "magic_converter", "run", "--host=0.0.0.0", "--port=5000"]

