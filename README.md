# Web Scraping Homework - Mission to Mars

In this assignment, I will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what I did.

## Step 1 - Scraping

I completed my initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News

* I scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. 

### JPL Mars Space Images - Featured Image

* I visited the url for the Featured Space Image site [here](https://spaceimages-mars.com).

* Then used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

### Mars Facts

* I visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Then used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* I visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

* I clicked each of the links to the hemispheres in order to find the image url to the full resolution image.

* Then I appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

## Step 2 - MongoDB and Flask Application

I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* I started by converting my Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executed all of my scraping code from above and returned one Python dictionary containing all of the scraped data.

* Next, I created a route called `/scrape` in my `app.py` that will import my `scrape_mars.py` script and call my `scrape` function.

  * I stored the return value in Mongo as a Python dictionary.

* I created a root route `/` that will query my Mongo database and pass the mars data into an HTML template to display the data.

* Lastly, I created a template HTML file called `index.html` that takes the mars data dictionary and displays all of the data in the appropriate HTML elements.
