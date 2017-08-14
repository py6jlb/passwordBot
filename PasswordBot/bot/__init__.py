from flask import Blueprint

mybot = Blueprint('mybot', __name__)

from . import bot