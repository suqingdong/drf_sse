from .renderers import SSERenderer


class SSEMixin(object):

    def get_renderers(self):
        if 'text/event-stream' in self.request.META.get('HTTP_ACCEPT', ''):
            return [SSERenderer()]
        return super().get_renderers()
