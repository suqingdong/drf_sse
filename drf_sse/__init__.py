import json
from pathlib import Path

from .renderers import SSERenderer
from .responses import SSEResponse
from .mixins import SSEMixin


BASE_DIR = Path(__file__).resolve().parent
version_info = json.load(BASE_DIR.joinpath('version.json').open())

__version__ = version_info['version']
