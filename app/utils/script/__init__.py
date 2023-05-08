from flask import Flask

from app.utils.script.command import BaseCommand


def initialize_script(app: Flask):
    app.cli.add_command(BaseCommand)
