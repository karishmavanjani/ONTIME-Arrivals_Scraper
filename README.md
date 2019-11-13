# ONTIME-Arrivals_Scraper
Data Source: Bureau of Transportation Statistics (BTS)

<h3>What it achieves</h3>

The selenium code looks into the aspx url- https://transtats.bts.gov/ONTIME/Arrivals.aspx and downloads data for all flights that have landed at New York's JFK airpor for all months and dates from 2015 to 2019! To analyze and parse the data extracted we later use Pandas. 

File Name: Scraper_BTSWebsite.

Ouput: CSV files in the data folder 

<h3>Methodology</h3>

1) Import necessary packages 
2) Create a new Chrome session using selenium
3) Open Chrome (at this point an automated test window will open) with the BTS url
4) Check the required filters
5) Write a function to save the csv including a try except block (known as try catch in Java) that knows how to exclude flights that don't fly into JFK.
6) Run a loop that updates the xpath until it reaches the last index number or airline option.

Note: Use of selenium is due to the static nature of the url which limits our ability to scrape the website using only Python. Alternatively, Java can be used instead of Python.

<h3> Pandas</h3>

To obtain the difference between 'Scheduled Arrival Time' and 'Actual Arrival Time' of passengers at the JFK gate, we analyze thousands of rows of data using Pandas.

File Name: *.ipynb files in the notebook folder including Merge_all csv.ipynb

Output= Final_Trend in the output folder

<h3>Methodology</h3>

The code looks at difference in flight arrival times by creating new columns using pd.to_datetime. 

For the edge case where the airlines report an actual arrival time or scheduled arrival time of '24:00,' the time has been converted to 00:00 and a new column called the 'actual arrival date' or schedule date has been created which is +1 day to factor in for the change in the date.
(Yes, I asked BTS what 24:00 even means! They are getting back to me.)

Finally, we compiled all the data to check the number of flights that arrived early in 2015 vs all years later.


<h3>Caveat: Data is restricted to U.S. carrier (domestic) scheduled service only.</h3>
