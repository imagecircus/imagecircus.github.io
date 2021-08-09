title: Figuring out FreePBX
date: 2013-05-04
category: Projects
tags: freepbx, iphone, pbx, raspberry-pi, sip

**Note: This post was originally published on iamianwright.com it's been moved here for archival purposes.**

In a moment of clarity I realised I was massively overcomplicating how to go about directing calls.  I had wanted the PBX to know if I was out of the house and route calls to the extension on my iPhone instead of my Mac.  When I thought about it this evening I realised that's completely unnecessary as FreePBX lets you set a rule for what to do if an extension is unreachable.  So I have now set it up so that if the softphone on my Mac isn't signed in then the call forwards to the extension for my iPhone.

On the subject of the iPhone, it turns out there are a number of SIP clients out there.  I've tried a few of them but so far the most reliable one has been [3CXPhone](https://itunes.apple.com/gb/app/3cxphone-voip-sip-softphone/id392927995?mt=8 "3CXPhone / VoIP / SIP Softphone for iOS") as it has the ability to accept calls in the background and when the device is on standby.  The only downside is that the ringtone is Marimba which I can't stand and sadly there is no option to change it.

It's all coming together quicker than I expected but there are still a few things to tick off:-

- Setup a VPN so I can connect externally.
- Configure the PBX to only allow calls through between 9am and 5pm Monday to Friday.  All other calls should go to voicemail and the messages forwarded to my email account.
- Record better messages for any of the greetings or menus I'll be using rather than the robotic American voice currently being used.
