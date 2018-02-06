# DemonetizationDetection
An attempt to detect Youtube Videos on your channel that have been demonetized

## What can this do?
This program should be able to detect if a video has been demonetized. It will 
use past data about a videos views to create a threshold of monetized playbacks
that is considered a problem. It will scan all videos on your channel for this 
threshold.

## What can this not do?
This cannot tell you if a video has *just* been demonetized. It needs some data 
from the Youtube API. It also does not currently have any kind of notification 
system in place to alert you. It must be run manually. It will also not work 
well for channels that don't consistently get monetized veiws.

## Theory
Using the number views that a video has recently got with the number of 
monetized playbacks it should be possible to to detect when the monetization 
has been shut off. This is implimented in this python code base by using the 
Youtube Data and Analyics APIs to get data associate with your youtube account.

## Notes about the code
There are two values at the top of `detect.py` that can be changed to get better
results based on your channel. The `days` variable is how many days back worth 
of data the program requests from the server. This is averaged to get one result
. The `threshold` value is the minimum percentage of monetized views to be 
considered typical. Setting this higher may trigger false positives and setting 
it lower will make it less likely to be flaged.

## My Youtube Experience as it relates to this
I get around 300 daily views on youtube. That's not a lot of data to work with 
for this detection method. So I can't say how well this is going to scale up to 
larger channels.

## Installation

You will need python 3 and the google api installed. You will also need to get 
a Google API key to access the Youtube API servers. Once you have a `client_id`
and `client_secret` to put in the `apikey.py` file and add your channel id (it's
the non-custom version of your channel url link) you should be ready.

## Usage
Just run `detect.py` and it will ask you to login to Youtube twice to get access
to the API services. The program uses Oauth2 to login and save your credentials
so you don't have to log back in everytime(saved as the `*_token.json` files).
After than it should collect a list of all videos, get the view data, and output
a list of video names with links to the edit pages that were below the threshold
.


