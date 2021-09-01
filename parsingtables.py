import tabula
import numpy as np
import pandas as pd

# Read in CDS
TU20_path = "C:/Users/jamit/Desktop/PersonalProjects/CDS Parsing/CDSes/TrinityCDS2020.pdf"

# Find the tables and save to tables variable. (pages="all" and multiple_tables=True necessary)
tables = tabula.read_pdf(TU20_path, pages = "all", multiple_tables = True)

print(tables[1])

# tables is a list object.