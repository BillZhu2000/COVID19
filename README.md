# COVID19
All sorts of visualization tools and predictive modelling

```county_viz.py``` builds an in-browser visulization of U.S. COVID19 cases per county per day using NYTimes data that 
they host on their GitHub. Simply running the script will fetch the latest available data and use plotly to build an 
animation. An example is given by the 3_28_county_anim.mp4 file. The script also uses the ```geojson-coutnies-fips.json```
file which contains all the fips geo location data for the counties.

The goal of ```reddit_scraper.py``` is to gather subreddit data an perform various data cleaning procedures in preparation
for NLP experiments (not sure what yet). It has a Python ```praw``` dependency which is the Python Reddit API wrapper
that efficiently retrieves posts, titles, comments, etc.

TODO: Finish ```reddit_scraper.py```, design NLP experiments, etc.
