# SSE(Server-Sent Events) for DjangoRestFramework

## Installation

```bash
python3 -m pip install drf-sse
```

## Usage

1. Edit your `setting.py`:
```python
INSTALL_APPS += [
    'rest_framework',
    'corsheaders',
    'drf_sse',
]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
CORS_ALLOW_ALL_ORIGINS = True

# SSE configuration
# SSE_RESPONSE_MODE = 'add'  # [optional, default: "chunk"]
SSE_ENCODE_BASE64 = True     # [optionnal, default: False]
```

2. Use in your views:

```python
import time

from drf_sse import SSEMixin, SSEResponse
from rest_framework.views import APIView

class MyView(SSEMixin, APIView):
    def get(self, request, format=None):

        def iter_data():
            iter_data = 'This is a server-sent events response'.split()
            for part in iter_data:
                yield part
                time.sleep(1)

        return SSEResponse(iter_data())
        # return SSEResponse(iter_data(), mode='chunk', encode=False)  # will overwrite settings
```

3. Test from the frontend:

- `SSE_ENCODE_BASE64 = False`

```html
<body>
    <p id="result"></p>
</body>
<script>
    const eventSource = new EventSource('http://127.0.0.1:8000/sse/')
    eventSource.onmessage = (event) => {
        console.log(event)
        document.getElementById('result').innerHTML += event.data + ' '
    }
    eventSource.onopen = () => {
        console.log('sse opened.')
    }
    eventSource.addEventListener('end', () => {
        eventSource.close()
        console.log('sse closed.')
    })
</script>
```

<details>
<summary>Preview</summary>
<img src="https://suqingdong.github.io/drf_sse/src/sse.png" widt="60%"/>
</details>

- `SSE_ENCODE_BASE64 = True`

```html
<body>
    <p id="result"></p>
</body>
<script>
    const base64DecodeAndUtf8Decode = (encodedStr) => {
        const textDecoder = new TextDecoder();
        const bytes = Uint8Array.from(atob(encodedStr), c => c.charCodeAt(0));
        return textDecoder.decode(bytes);
    }

    const eventSource = new EventSource('http://127.0.0.1:8000/sse/')
    eventSource.onmessage = (event) => {
        console.log(event)
        document.getElementById('result').innerHTML += base64DecodeAndUtf8Decode(event.data) + ' '
    }
    eventSource.onopen = () => {
        console.log('sse opened.')
    }
    eventSource.addEventListener('end', () => {
        eventSource.close()
        console.log('sse closed.')
    })
</script>
```

<details>
<summary>Preview</summary>
<img src="https://suqingdong.github.io/drf_sse/src/sse-encode.png" widt="60%"/>
</details>
