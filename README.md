# Web-Scraping-Python-For-Multi-Page
This code used to scrape data with Python from a website -(called Wuzzuf) - can scarp data from multi-page at the same time automatically


The link of the page of wuzzuf is:
https://wuzzuf.net/search/jobs/?a=hpb&q=python&start=0

firstly; making while loop to take data from multi-pages 
storage site in a variable, store the content in a variable
then create an object from the Library BeautifulSoup. 
Making if condition to stop the error out of the index.
5th Step find the elements containing info we need
job title, company names,  location names, job skills
6th step loop over returned lists to extract needed info into other lists
        Caution in line 48 you need to add "https://wuzzuf.net" because the Url in the site in "Inspect" don't have this part of Url,
        then the code will give you an Exception --->
        Exception has occurred: MissingSchema Invalid URL '/jobs/p/T2ShpO8q8U6v-Python-Tech-Lead-Eastern-Enterprise-Cairo-Egypt?o=1&l=sp&t=sj&a=python|search-v3|hpb':
        No scheme supplied. Perhaps you meant http:///jobs/p/T2ShpO8q8U6v-Python-Tech-Lead-Eastern-Enterprise-Cairo-Egypt?o=1&l=sp&t=sj&a=python|search-v3|hpb?
          File "D:\programing\Python holiday\Holy.py", line 55, in <module>
            result = requests.get(link)

Put all of it in try to ignore any errors.
Making for loop to fetch data from sites in the source site 
and put it also in try to ignore any errors.

Putting all lists in a list, then exporting it in a CSV file.
Using with open to ignore any error 
