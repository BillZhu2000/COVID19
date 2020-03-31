"""
Script to visualize county data growth
"""

import json
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# Read in county data
def visualize(url='https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'):
    """
    Visualize COVID19 cases per county over time from NYTimes data
    :param url:
    :return:
    """
    # Get latest county data and load to df
    df = pd.read_csv(url)

    # TODO Figure out how to map the fips data more accurately
    df['fips'] = [str(int(x)).zfill(5) if not np.isnan(x) else 00000 for x in df['fips']]
    # print(df.head())
    df.to_csv('rsc/' + url.split('/')[-1])

    # Load county json coords and plot the graph
    log_cases = np.log10(df['cases'])
    county_coords = json.load(open('rsc/geojson-counties-fips.json'))
    fig = px.choropleth(df, geojson=county_coords, locations='fips', color=log_cases,
                        color_continuous_scale="sunset",
                        range_color=(0, max(log_cases)),
                        scope="usa",
                        labels={'cases': 'Total cases'},
                        animation_frame="date"
                        )
    tickvals = list(range(int(max(log_cases)) + 1))
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      coloraxis_colorbar=dict(
                      title='U.S. COVID19 cases by county over time',
                      tickvals=tickvals,
                      ticktext=[pow(10, x) for x in tickvals]))
    fig.show()

    # TODO Figure out how to save this thing


def main():
    visualize()


if __name__ == '__main__':
    main()
