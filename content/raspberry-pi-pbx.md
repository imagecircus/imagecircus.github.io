title: Raspberry Pi PBX
date: 2013-05-04
category: Projects
tags: pbx, raspberry-pi

**Note: This post was originally published on iamianwright.com it's been moved here for archival purposes.**

I’ve been looking at a cheap and flexible solution to having a separate phone number for business calls. I recently came across a post detailing how to use the Raspberry Pi as a PBX. It seems like it will more than cover my needs and as it comes in at under £50 for everything I figured it was worth a go.

I had planned to write a detailed post explaining what was involved in setting it up but it was much easier than I expected.  Essentially you download the image for the SD card use PiWriter to [copy img to SD card from the Mac.](http://sourceforge.net/projects/piwriter/ "PiWriter")  Plug in power and ethernet, SSH into the Pi to make a few changes and then everything else can be done via the web interface.

I followed the [instructions for installing Incredible PBX on the Raspberry Pi](http://nerdvittles.com/?p=5527 "Incredible PBX 3.11 for Raspberry Bi") from Nerd Vittles.  Next I needed a VoIP account and as I'm in the UK sadly google voice wasn't an option.  So I signed up for a [free SIP account](http://www.sipgate.co.uk/user/ "Free phone service over your broadband line") at Sipgate and then followed these [steps to set up a Sipgate trunk](http://sysadminman.net/blog/2012/asterisknow-setting-up-a-trunk-and-outbound-calls-with-sipgate-4259 "Setting up a Sipgate trunk in FreePBX").

I'm using [X-Lite](http://www.counterpath.com/x-lite.html "X-lIte") on my macbook air as my soft phone at the moment.  I have incoming and outgoing calling working perfectly.  Currently calls do go to voicemail if unanswered but no messages are recorded.

The next plan is to set up a VPN tunnel into my home network so I can run a SIP client on my iPhone that will work as an extension of the PBX.  The upside is that as it's an internal extension there won't be any charge to pass the call on.  The downside is that it requires my phone to have an internet connection which is a rare thing in Thanet.

Ultimately I want the system to recognise if I'm home or not and automatically divert calls to the appropriate extension.  I'm sure this should be possible by looking to see if my iPhone's MAC address is connected to the network.  Now I just need to figure out how to make a change in asterisk based on network information.

The project [continues...](/figuring-out-freepbx/ "Figuring out FreePBX")