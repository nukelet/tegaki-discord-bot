# Tegaki Discord backend

## Running

```bash
$ flask run --debug
```

This will start a web server in `http://127.0.0.1:5000`.

The static files will be served in the `/static` endpoint, and the static files
all live in the [`/static`](./static) subfolder within this directory. The editor
itself is served in `/static/tegaki.html`
