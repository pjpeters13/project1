import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet

# API Connection
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", "yUnYRTjXHWdK6ATxbXOsJR52v")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("qgea-i56i", limit=5000)
df = pd.DataFrame.from_records(results)