from classes.library import Library
from utils.db import db
from utils.load_initial_data import load_initial_data
from utils.simulator import librar_simulator

l = Library()
load_initial_data(l,db)

librar_simulator(l)