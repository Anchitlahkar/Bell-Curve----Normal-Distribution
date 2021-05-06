import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")

averageRating = df["Avg Rating"].tolist()

graph = ff.create_distplot([averageRating],["Average Rating"], show_hist=False)

graph.show()