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
There are two values at the top of `detect.py` that can be changed to get better
results based on your channel. The `days` variable is how many days back worth 
of data the program requests from the server. This is averaged to get one result
. The `threshold` value is the minimum percentage of monetized views to be 
considered typical. Setting this higher may trigger false positives and setting 
it lower will make it less likely to flag videos.

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
Just run `detect.py` and it will ask you to login to Youtube twice to get access
to the API services. The program uses Oauth2 to login and save your credentials
so you don't have to log back in every time(saved as the `*_token.json` files).
After that it should collect a list of all videos, get the view data, and output
a list of video names with links to the edit pages that were below the threshold
.

## Output

When run the program will not initially output anything. It takes a while to 
collect all the data from the API servers. For me it takes about 30s to run with
3 days worth of data. Once it has received all the data and processed it, it
will output the name of the video, the percentage of monetized playbacks, and
a link to go directly to the Creator Studio edit page for that video.

Here is an example of what that output looks like when I run it against my own 
channel. (Note, these are *all* false positives because I do not get enough 
views for this to work properly.)
```
$ ./detect.py
Video "Python Youtube Demonetization Detector" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=FCObiesnPRM
Video "Tektronix Type 503 Oscilliscope a Recent Acquisition" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=C_XdrXjYqGE
Video "Prototyping Inline Volume Controls V2 LIVE pt1" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=ki9X1qRimMw
Video "Prototyping Inline Volume Controls V2 LIVE pt2" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=v7RDmFpYw0Y
Video "Big Box PC Game Collecting/Shipping Pains" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=I0leGSxS3Ic
Video "Hello" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=JtVpXpxSdqk
Video "0x0017 - MDR-7506 Driver Replacement" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=7zNz5HaaezU
Video "0x0014[Extra] - Gigabit Powerline Adapter Not Even Close" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=VY7W7wdi8IA
Video "0x0010 - IDE CD Changer" is at 8.333333333333332% monetized views
https://www.youtube.com/edit?o=U&video_id=PeHOT2FCPNg
Video "0x0012.1 - Canon BJC-85 Portable Printer" is at 8.928571428571429% monetized views
https://www.youtube.com/edit?o=U&video_id=t80PduF9BAM
Video "0x0003 - Tiva Module Assembly" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=TF_MkvHy8tE
Video "0x000B- TView Presocard: Windows 95 Composite Video" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=aB3dHzgZQ-4
Video "0x000A - DE-5000 ESR Meter Diode Replacement" is at 8.333333333333332% monetized views
https://www.youtube.com/edit?o=U&video_id=pkbOTBbFplo
Video "0x0007 - USB Commodore PET Keyboard" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=FfIFVg9cpUY
Video "0x0004 - MATRIX on Commodore PET" is at 0.0% monetized views
https://www.youtube.com/edit?o=U&video_id=CiNxjIW1DTo
```

## Roadmap
This is program is functional but not complete. I still have several more 
features to add to it:

 - Confidence value: If views are too low to be sure this would be low as well
 - Better structured output: Using confidence values to sort into "likely" and 
	"unlikely" categories 

After I get those done I will start working on a version with a GUI and a local 
database. That should will improve general usability and drastically reduce the
time needed to check the videos.

At this point I don't plan on making a service out of this functionality. It
would be possible to setup a server with a web login that let's people add their
youtube accounts and be notified when a video has been demonetized. There would 
also be a recurring cost of server time so I would need to find a way to fund 
it. If this garners enough interest I can look into setting this up.

