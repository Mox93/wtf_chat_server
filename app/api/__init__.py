from flask import Blueprint

api = Blueprint("api", __name__)

from .user import *
from .chat import *
from .message import *
from .access import *
