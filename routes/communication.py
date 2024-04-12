from flask import Blueprint
from jinja2 import TemplateNotFound

auth = Blueprint("communication",__name__,template_folder="templates",url_prefix="/chat")

@auth.route('form')
def form_for_communication():
    return "get info from user"
@auth.route('bot')
def bot_for_personalization():
    return "give information about the catalogues etc."