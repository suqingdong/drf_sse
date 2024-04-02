import base64

from django.http import StreamingHttpResponse
from django.conf import settings


class SSEResponse(StreamingHttpResponse):

    SSE_ENCODE_BASE64 = getattr(settings, 'SSE_ENCODE_BASE64', False)
    SSE_RESPONSE_MODE = getattr(settings, 'SSE_RESPONSE_MODE', 'chunk')

    def __init__(self, iter_data, *args, mode=None, encode=None, **kwargs):
        kwargs.setdefault('content_type', 'text/event-stream')
        data = self.event_stream(
            iter_data,
            mode=mode or self.SSE_RESPONSE_MODE,
            encode=encode if encode is not None else self.SSE_ENCODE_BASE64,
        )
        super().__init__(data, *args, **kwargs)

        self['Cache-Control'] = 'no-cache'

    @staticmethod
    def event_stream(iter_data, mode=None, encode=None):
        data = ''
        for n, part in enumerate(iter_data):
            if mode == 'chunk':
                data = part
            else:
                data += ' ' + part

            if encode == True:
                data = base64.b64encode(data.encode()).decode()

            yield f'id: {n}\ndata: {data}\n\n'

        yield 'event: end\ndata: \n\n'