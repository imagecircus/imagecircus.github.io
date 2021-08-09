title: Tekkit Classic with Minecraft 1.6.2
date: 2013-09-14
category: Projects
tags: 1-6-2, forge, minecraft, mods, server, tekkit-classic

**Note: This post was originally published on iamianwright.com it's been moved here for archival purposes.**

Following on from my [previous post](/building-a-custom-forge-minecraft-1-6-2-server/ "Previous post") I wanted to write a little more about the issues I found trying to get all of the Tekkit Classic mods working with Minecraft 1.6.2.

Having discussed everyone's requirements, my friends and I agreed that we wanted all the features of Tekkit Classic with the additions of Stargate, Twilight Forest, Archimedes Ships, Useful Foods, Treecapitator and a few others. I read a lot of guides and figured out [how to set up a custom Forge server for Minecraft 1.6.2](/building-a-custom-forge-minecraft-1-6-2-server/ "How to build a custom Forge server with Minecraft 1.6.2").

Now we can install any mods we want but there are some caveats. Firstly not all mods work with Minecraft 1.6.2 and secondly not all mods work with each other. This is where we hit the first problem, Tekkit Classic is built on Minecraft 1.2.5 so all of the mods that come with it are designed for that. Some of them have been updated to 1.6.2 but unfortunately not all.

| Mod Name                    | 1.6.2 | Download                                                                                                                              |
|-----------------------------|-------|---------------------------------------------------------------------------------------------------------------------------------------|
| Balkon's Weapon Mod         | Yes   | [Here](http://www.minecraftforum.net/topic/211517-162forge-balkons-weaponmod-v113-now-with-flintlock-pistol/ "Balkon's Weapon Mod")   |
| BuildCraft                  | Yes   | [Here](http://minecraft.curseforge.com/mc-mods/buildcraft/files/4-build-craft-4-0-2/ "Buildcraft 4.0.2")                              |
| BuildCraft Additional Pipes | No    |                                                                                                                                       |
| ccSensors                   | No    |                                                                                                                                       |
| ComputerCraft               | Yes   | [Here](http://www.computercraft.info/2013/07/11/computercraft-1-55/ "ComputerCraft 1.55 for MC 1.6.2")                                |
| IC2 Charging Bench          | Yes   | [Here](http://forum.industrial-craft.net/index.php?page=Thread&threadID=929)                                                          |
| Dimensional Anchors         | Yes   | [Here](http://immibis.com/mcmoddl/ "All Immibis' Mods")                                                                               |
| Equivalent Exchange 2       | No    |                                                                                                                                       |
| Ender Storage               | Yes   | [Here](http://www.chickenbones.craftsaddle.org/Files/New_Versions/links.php "All ChickenBones' Mods")                                 |
| Industrial Craft 2          | Yes   | [Here](http://www.9minecraft.net/industrial-craft-2-mod/)                                                                             |
| IC2 Advanced Machines       | Yes   | [Here](http://forum.industrial-craft.net/index.php?page=Thread&threadID=4907)                                                         |
| IC2 Compact Solars          | Yes   | [Here](http://forum.industrial-craft.net/index.php?page=Thread&threadID=4827)                                                         |
| IC2 Nuclear Control         | Yes   | [Here](http://forum.industrial-craft.net/index.php?page=Thread&threadID=5915)                                                         |
| Immibis Core                | Yes   | [Here](http://immibis.com/mcmoddl/ "All Immibis' Mods")                                                                               |
| Inventory Tweaks            | Yes   | [Here](http://www.minecraftforum.net/topic/1720872-162-inventory-tweaks-156-august-21/)                                               |
| Iron Chests                 | Yes   | [Here](http://www.9minecraft.net/iron-chests-mod/)                                                                                    |
| MAtmos                      | Yes   | [Here](http://www.minecraftforum.net/topic/379925-162-matmos-r25-environmental-sound-atmosphere-simulator/)                           |
| Modular Force Field System  | Yes   | [Here](http://immibis.com/mcmoddl/ "All Immibis' Mods")                                                                               |
| Not Enough Items            | Yes   | [Here](http://www.chickenbones.craftsaddle.org/Files/New_Versions/links.php "All ChickenBones' Mods")                                 |
| Nether Ores                 | No    |                                                                                                                                       |
| Power Converters            | Yes   | [Here](http://www.minecraft12.com/power-converters-mod/)                                                                              |
| Railcraft                   | Yes   | [Here](http://www.9minecraft.net/railcraft-mod/)                                                                                      |
| Red Power                   | No    |                                                                                                                                       |
| Rei's Minimap               | Yes   | [Here](http://www.9minecraft.net/reis-minimap-mod/)                                                                                   |
| Tube Stuff                  | Yes   | [Here](http://immibis.com/mcmoddl/ "All Immibis' Mods")                                                                               |
| Wireless Redstone WR-CBE    | Yes   | [Here](http://www.chickenbones.craftsaddle.org/Files/New_Versions/links.php "All ChickenBones' Mods")                                 |

Of the modules missing the Additional Pipes for Buildcraft and the Sensors for ComputerCraft were no big deal as I don't think any of us have ever used them.  Equivalent Exchange 2 not being available is a bigger problem as one of my friends is very keen on that mod.  EE3 is available for 1.6.2 but it is arguably not as good (or perhaps it's just more balanced). Nether Ores are no big loss either as none of us really mine in the nether.

Red Power is an issue though as it includes so many features. There are some modders working on creating similar mods for 1.6.2, Immibis has [RedLogic](http://www.minecraftforum.net/topic/1852277-162-redlogic-wip-replacement-for-rp2-wiringlogiccontrollighting/ "RedLogic WIP replacement for RedPower") and I came across a few others.

Unfortunately I was unable to get RedLogic or Equivalent Exchange 3 to install with the other mods on my server.  I'm hoping there will be some updates that may resolve that in the near future as they make up a large chunk of the features of Tekkit Classic.

This is my final set of mods, including what I could from Tekkit Classic and the additional ones that we wanted.

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
