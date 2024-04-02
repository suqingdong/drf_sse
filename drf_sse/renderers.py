from rest_framework.renderers import BaseRenderer


class SSERenderer(BaseRenderer):
    """
    Support render for sse request
    """
    media_type = 'text/event-stream'
    format = 'sse'
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data
