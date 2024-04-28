from classes.library import Library
from utils.db import db
from utils.load_data import load_initial_data

l = Library()
load_initial_data(l,db)

