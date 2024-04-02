## Demo with `drf-sse`

### Install requirements

```bash
python -m pip install -r requirements.txt
```

### Run server

```bash
# python manage.py migrate

python manage.py runserver 
```

### Preview
- open `index.html`         # SSE_ENCODE_BASE64 = False
- open `index.encode.html`  # SSE_ENCODE_BASE64 = True