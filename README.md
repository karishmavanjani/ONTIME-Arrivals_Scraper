# ONTIME-Arrivals_Scraper
Data Source: Bureau of Transportation Statistics (BTS)

<h3>What it achieves</h3>

The selenium code looks into the aspx url- https://transtats.bts.gov/ONTIME/Arrivals.aspx and downloads 2019 data for all flights arriving at New York's JFK airport. 

<h3>Methodology</h3>

1) Import necessary packages 
2) Create a new Chrome session using selenium
3) Open Chrome (at this point an automated test window) with the BTS url
4) Check the required filters
5) Write a function to save the excel including a try except block (known as try catch in Java) that knows how to exclude flights that don't fly into JFK.
6) Run a loop that updates the xpath until it reaches the last index number or airline option.

Note: Use of selenium is due to the static nature of the url which limits our ability to scrape the website using only Python. Alternatively, Java can be used instead of Python.

<h3>Caveat: Data is restricted to U.S. carrier scheduled service only.</h3>
