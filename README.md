# Team: Iota
### BostonHacks 2018
### Track: Data for Urban Good

## Inspiration
To pursue Data for Urban Good, we partnered with the City of Boston to try to recreate a dataset they created in 2014 by walking all 1600 miles of sidewalk in Boston. We were deeply moved by the image of dedicated data scientists spending all of there time walking the streets just to collect data. With 2 future data scientists on our team, we knew there had to be a better way to collect this data. So we accepted the difficult challenge of finding a new, easier way to collect data that can be completed far more often.

## What it does
Our code takes in a range of GPS coordinates, inputs them into the Google Roads API, which outputs a list of coordinates that makes a smooth path through the roads of Boston, then takes each coordinate and queries the Google StreetView API the get an image of the road. We then intend for future steps to include inputting these images into image recognition software, extracting the sidewalk only from those images, and running through a machine learning algorithm that has been trained with the 2014 data to score the sidewalk based on its condition.

## How we built it
We utilized Google's extensive library of APIs, then scraped Google maps data through Python. We used an image recognition software (that we would be happy to give you the name of when our image recognition specialist arrives) to analyze the images, and we used QGIS, a geographic information software, to understand the 2014 sidewalk data.

## Challenges we ran into
The 2014 data was stored with a strange coordinate projection system, called the Lamber Conical Projection. Intense transformations were applied to the standard coordinate system of latitude and longitude that Google Maps uses, and we had to reverse engineer the coordinate system we are accustomed to.

As is expected, machine learning and image recognition is always a challenge. (Extracting a sidewalk from the photos we downloaded is difficult.)

Getting the geographic information from Google Maps as a series of nodes that we can iterate through and scrape was more challenging than we expected when we first explored all our Google API options.

We struggled with creating a front end to display our work.

## Accomplishments that we're proud of
We learned an entirely new technology: QGIS.

## What we learned
How to divide work, how to communicate, how to overcome intense confusion together, how to read a shapefile, how to work with Google APIs in Python, the basics of image recognition. The list goes on and on.

## What's next for Iota
Develop a front end, working on more detailed image recognition.
