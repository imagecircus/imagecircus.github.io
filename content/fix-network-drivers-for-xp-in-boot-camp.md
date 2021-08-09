title: Fix Network Drivers for XP in Boot Camp
date: 2013-08-23
category: Advice
tags: boot-camp, drivers, internet, leopard, network, windows-xp

**Note: This post was originally published on iamianwright.com it's been moved here for archival purposes.**

Just a quick tip today.  I had a client that asked me to do the unthinkable.  She bought an iMac several years ago but had only ever used it for Windows XP under boot camp.  She asked me to give her more space on the windows side, it was originally configured with the default 32Gb.  So after backing up her data I removed the windows partition then created a new, larger one. I reinstalled Windows XP and followed [Apple's instructions (PDF)](http://manuals.info.apple.com/en/boot_camp_install-setup.pdf "Apple's instructions (PDF)") by installing the drivers from the Leopard disc.

Windows XP would not recognise the network drivers (ethernet or airport). After several futile attempts and one other copy of Windows it was still stubbornly uncooperative. Everything I could find on the web just reiterated Apple's advice to install the drivers. In a last act I tried installing the drivers from a Snow Leopard disc and it worked perfectly.

So if you can't get an internet connection in Windows XP under boot camp try installing the drivers from a Snow Leopard disc as the Leopard ones don't seem to work (alternately learn to use Mac OS X, just saying).