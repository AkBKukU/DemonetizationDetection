# DemonetizationDetection
An attempt to detect Youtube Videos on your channel that have been demonetized

## What can this do?
This program should be able to detect if a video has been demonetized. It will 
use past data about a videos views to create a threshold of monetized playbacks
that is considered a problem. It will scan all videos on your channel for this 
threshold.

## What can this not do?
This cannot tell you if a video has *just* been demonetized. It needs some data 
from the Youtube API. The time it takes for new analytics data to show up in the
Creator Studio is the same as when it shows up in the API . It also does not 
currently have any kind of notification system in place to alert you. It must be
run manually. It will not work well for channels with consistently low amounts
of monetized views.

## Theory
Using the number views that a video has recently got with the number of 
monetized playbacks it should be possible to to detect when the monetization 
has been shut off. This is implemented in this python code base by using the 
Youtube Data and Analyics APIs to get data associated with your youtube account.

## Notes about the code
There are three values at the top of `detect.py` that can be changed to get 
better results based on your channel. 

 - `days`: Is how many days back worth of data the program requests from the 
     server. This is averaged to get one result. 
 - `threshold`: Is the minimum percentage of monetized views to be considered 
     typical. Setting this higher may trigger false positives and setting it 
     lower will make it less likely to flag videos. 
 - `views_for_confidence`: Is the number of views a video needs to have for a 
     high level of confidence that it is demonetized.

## My Youtube Experience as it relates to this
On [my Youtube channel](https://www.youtube.com/AkBKukU) I get around 300 daily 
views. That's not a lot of data to work with for this detection method. So I 
can't say how well this is going to scale up to larger channels. Almost every 
video I upload gets demonetized initially. So I know what it's like.

## Installation

You will need [python 3](https://www.python.org/downloads/) and the [google api](https://developers.google.com/api-client-library/python/start/installation) 
installed. You will also need to get a [Google API key](https://support.google.com/googleapi/answer/6158862) 
to access the Youtube API servers. Once you have a `client_id` and 
`client_secret` to put in the `apikey-empty.py` file and add your channel id 
(it's the non-custom version of your channel url link) you should be ready. Then 
rename it to `apikey.py`.

The code is written in python and is compatible with Windows, Mac, and Linux.
I'll have more detailed installation instructions as I continue to improve the 
program.

## Usage
Just run `detect.py` and it will ask you to login to Youtube to get accessto the
API services. The program uses Oauth2 to login and save your credentials so you 
\don't have to log back in every time(saved as the `*token.json` file). After 
that it should collect a list of all videos, get the view data, and output a 
list of video names with links to the edit pages that were below the threshold.

## Output

When run the program will not initially output anything. It takes a while to 
collect all the data from the API servers. For me it takes about 9s to run with
3 days worth of data. Once it has received all the data and processed it, it
will output confidence headers, the name of the video, the percentage of 
monetized playbacks, and a link to go directly to the Creator Studio edit page 
for that video.

Here is an example of what that output looks like when I run it against my own 
channel. 
```
$ ./detect.py

High Confidence of Demonetiztion:
Video "Channel Updates" is at 0% (0/178) monetized views
https://www.youtube.com/edit?o=U&video_id=201isF9onSc

Low Confidence of Demonetiztion:
Video "0x001D - DIY LED Filming Lights" is at 0% (0/0) monetized views
https://www.youtube.com/edit?o=U&video_id=M-1O5SR0sYY
Video "META: My Audio Setup" is at 0% (0/0) monetized views
https://www.youtube.com/edit?o=U&video_id=HjlQ65Ywot4
Video "Prototyping Inline Volume Controls V2 LIVE pt1" is at 0% (0/0) monetized views
https://www.youtube.com/edit?o=U&video_id=ki9X1qRimMw
Video "Prototyping Inline Volume Controls V2 LIVE pt2" is at 0% (0/1) monetized views
https://www.youtube.com/edit?o=U&video_id=v7RDmFpYw0Y
```

I did not monetize the video "Channel Updates" to test this. It got 178 views 
the previous day but none were monetized. So it gets a high confidence rating.

In this case the low confidence values are all false positives because I do not 
get enough views for this to work properly. (this is pretty all my videos so I
cut it short for the example)

## Roadmap
This is program is functional but not complete. I still have several more 
features to add to it:

 - GUI: Because not everyone wants a grey beard
 - Local Database: You can't upload videos in the past\*. So keep existing video
     information locally and only check by default for videos after the newest
     one the the DB.

\*Streams can be a bit odd with their dates

At this point I don't plan on making a service out of this functionality. It
would be possible to setup a server with a web login that let's people add their
youtube accounts and be notified when a video has been demonetized. There would 
also be a recurring cost of server time so I would need to find a way to fund 
it. If this garners enough interest I can look into setting this up.

