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
