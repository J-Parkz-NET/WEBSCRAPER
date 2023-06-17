# WEBSCRAPER. 

The main purpose of this code is to make an HTTP request to a specific web page and then use the BeautifulSoup library to extract and display the links (<a>) present on that page.

The code performs the following steps:

Make an HTTP request to the provided URL using requests.get(url). The goal is to obtain the HTML content of the web page.

Creates a BeautifulSoup object called soup using the obtained HTML content and the html.parser parser. This makes it easier to parse and work with the HTML content of the page.

Use BeautifulSoup's find_all('a') method to find all <a> the elements on the web page. This returns a list of all links found.

Iterate over the list of links and use link.get('href') to get the URL of each link. Then, the URL is printed. 
