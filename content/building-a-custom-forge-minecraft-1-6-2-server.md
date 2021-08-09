title: Building a Custom Forge Minecraft 1.6.2 Server
date: 2013-09-14
category: Projects
tags: 1-6-2, custom, forge, minecraft, mods

**Note: This post was originally published on iamianwright.com it's been moved here for archival purposes.**

Having played through [Tekkit Classic](http://www.technicpack.net/tekkit-classic "Tekkit Classic"), [Voltz](http://www.technicpack.net/voltz "Voltz"), [YogCraft](http://ftbwiki.org/YogCraft_Pack "YogCraft") and [Tekkit](http://www.technicpack.net/tekkit/ "Tekkit (in space)") my friends and I decided it was time for a custom mod pack. This of course meant that I had to figure out how to build it. After reading a bunch of tutorials of differing quality and reliability I was left under the impression that I would need to use a PC. Fortunately for us Mac users with Minecraft 1.6.2 and the new Forge installer this is not the case.

## Installing Minecraft Server 1.6.2 and Forge

Head to the [minecraft site](http://minecraft.net/download "Minecraft Downloads") and grab a copy of minecraft\_server.1.6.2.jar. Make a folder to store your server and copy the jar into it. Double click to run the server and continue passed any warnings that may pop up. Once the server has finished loading type "Stop" in the console.

Now we need to install Forge so head over to [their site](http://www.minecraftforge.net/forum/index.php/topic,10075.0.html "Forge 9.10.0 for MC 1.6.2") and grab the latest installer. Download it to your desktop or anywhere else that isn't your minecraft server folder. Double click to the launch the installer. Chose "Install Server" and then make sure it's got the correct path to your server folder. Hit Ok. This seems to take ages, I have a 70mb connection and yet the bar still crawls along and stops repeatedly. After waiting a while you will probably receive an error like the one below:

_**Error downloading**_ _These libraries failed to download. Try again._ _org.scala-lang:scala-library:2.10.2,_ _org.scala-lang:scala-compiler:2.10.2_

If this happens [WontWorld on Youtube](http://www.youtube.com/watch?v=LbN4wh5HGrk "Minecraft Server 1.6.2 Forge Modloader Install Error (Error Downloading)") has got you covered. For me it only failed to download one of the libraries but his instructions fixed it.

Now you will need a launcher batch file so that you can configure how much RAM is assigned to the server at launch. Open up textedit (or similar), make sure you are in Plain Text (Format > Make Plain Text), then copy and paste the following code.

<pre>#!/bin/bash cd "$(dirname "$0")" exec java -Xmx4G -Xms4G -jar minecraftforge-universal-1.6.2-9.10.0.804.jar</pre>

This will assign 4Gb of RAM for your server but you can change it accordingly for your system. My server runs 24/7 on a Mac Mini with 8Gb of RAM that I use as HTPC as well so I leave half the RAM free for other applications.

Save the file as launch.command. Now you need to set permissions for the file so that it can be executed. Open terminal, navigate to your server folder by typing "cd" without the quotes, then a space, then drag and drop your server folder onto the terminal window. That should complete the command with the full path to your server folder. Hit return and then type the following code.

<pre>chmod a+x launcher.command</pre>

Excellent. Now quit terminal as it's scary in there and we won't need it anymore. Next double click on launcher.bat and your MinecraftForge server should start. This would be a good time to test that you can connect to your new server.

## Installing Forge for your Minecraft Client

Before connecting to the server you'll need to install forge but before you can so that you must run Minecraft once. You'll need a copy of [Minecraft 1.6.2 from the Downloads page](http://minecraft.net/download "Minecraft Downloads"). Install it as normal and then open it. Once you get to the screen with a button that says "Play" you can quit and then install Forge.

This is fairly simple, just run the [Forge installer you downloaded](http://www.minecraftforge.net/forum/index.php/topic,10075.0.html "Forge Installer") earlier choose "Install Client" make sure that the installer has the right path to your minecraft install and hit OK. This is generally very quick and painless.

Now open Minecraft again, choose the new Forge profile at the bottom left and hit Play. In Minecraft click Multiplayer, then add your server and test that it works.

If you've got this far and everything is working then it's time to move on to the fun bit.

## Installing Mods into FML in Minecraft 1.6.2

So now that you have your list of mods, download them all into a working directory somewhere other than your server folder. When you download them be sure that your browser is not unzipping them, if it is you should be able to find the zips in the trash.  All of the mods will be either ZIP files or JAR files.

All that's left to do now is install the mods by moving the mod file into the mods folder inside your server folder.  It would be nice if you could just drag them all in at once and it worked but that was not my experience.  I found that it was best to add one at a time and check I could still login. **Remember that any mod installed on your server also needs to be installed on your client.**

Some mods have different files for server and client but most are universal.  So add a mod to your server, start the server, add the mod to your client, start your client and join the server.  Sometimes after adding a mod to the server it will die horribly and throw a SEVERE error. If that happens read the log file, read the forums, check for dependencies and try again.

You may need to copy the contents of the server's config folder to your client's config folder if you encounter ID mismatches between client and server.

It would also be a good idea to make backups of your server every time you successfully install a mod. This may seem like overkill but I finished this project once and was happily playing online when I decided I should add one more mod.  It threw a severe error, removing the bad mod didn't fix it neither did reinstalling the server and copying the last backup of mods. Moral of the story backup everything all the time.

In the end I managed to get the following mods installed and living happily side by side.

- Advanced Repulsion Systems 56.0.0
- Advanced Machines 56.0.0
- Arhimede's Ships 1.6.2
- BuildCraft 4.0.2
- ChickenChunks 1.3.3.2
- CodeChickenCore 0.9.0.5
- ComputerCraft 1.5.6
- Dimensional Anchor 56.0.1
- Dyeable Beds 1.6.2
- EnderStorage 1.4.2.2
- Greg's SG Craft Mod 1.6.2
- Immibis Core 56.0.5
- Immibis MicroBlocks 56.0.5
- Industrial Craft 2
- Infinitubes 56.0.1
- Iron Chests 1.6.2
- IC2 Charging Bench 1.90
- Not Enough Items 1.6.1.3
- Teleport Pipes Mod 1.6.2
- Timber! 1.6.2
- Twilight Forst 1.19.3
- Useful Food 1.6.2
- Weapon Mod

Now it's up to my friends to play test it and see if it breaks horribly.
