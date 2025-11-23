import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
STATIC_DIR = os.path.join(ROOT_DIR, "static")
PROCESSED_DIR = os.path.join(STATIC_DIR, "processed")
