FROM python:3.12-alpine
WORKDIR /app

COPY . .

RUN apk update && apk upgrade && apk add curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

RUN poetry install --no-root

EXPOSE 5000

CMD ["poetry", "run", "flask", "--app", "magic_converter", "run", "--host=0.0.0.0", "--port=5000"]
