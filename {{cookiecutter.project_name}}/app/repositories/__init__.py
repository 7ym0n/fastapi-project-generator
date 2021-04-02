#
# Copyright (C) {{cookiecutter.copyright}}
#
# Author: {{cookiecutter.author}} <{{cookiecutter.email}}>
#

from sqlalchemy.orm import Session


class Repository:
    db: Session

    def __init__(self, db: Session):
        self.db = db
