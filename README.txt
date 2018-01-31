The Ultimate Scraper buit by Brandon Rice (Agent Programmer)

Note ***

I really liked the trickyness of this challenge looking at the
code of the site I was sumpted for about 5 mins.
But as an Electrical engineer i taught my self to always exploit
a materials characteristics. I decided to exploit HTML
because html is 'markdown language' any parser library has to go from top to bottom
so I figued id store the state everytime I saw Sunset and sun rise and with in
that state look for my data. That way I only go through the list once to keep 
my time efficentcy Low I imagine retrieving he data wasnt st costly because bs4 stores the website
in memory which is why i choose a for loop for the locations instead of all at one time.

as an extra i stored the data in a csv file for review. I currently work in at The United
States Geological Survey so I work with alot of researchers and dataminers. And they are 
very visual when they need data parsed or collected and miniulated.

thanks this was fun 

***

Dependencies 
bs4 (Beautiful soup) [pip install bs4]

Python version 3.6^

in a terminal run 'python scraper.py'
