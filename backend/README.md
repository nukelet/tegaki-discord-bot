# Tegaki Discord backend

## Running

```bash
$ flask --app backend run --debug
```

This will start a web server in `http://127.0.0.1:5000`.

The static files will be served in the `/static` endpoint, and the static files
all live in the [`/static`](./static) subfolder within this directory. The editor
itself is served in `/static/tegaki.html`

## Resetting the database

```bash
$ flask --app backend init-db
```

## Generating API keys
```bash
$ flask --app backend generate-api-keys
```
