#!/usr/bin/python3
"""initializes storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
