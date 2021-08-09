title: Over-engineering #firstworldproblems
date: 2015-04-27
category: Web Development
tags: alert, automation, kickstarter, pebble, push, python

I have finally backed a kickstarter campaign for the first time. It's a [3D printer called Tiko](https://www.kickstarter.com/projects/tiko3d/tiko-the-unibody-3d-printer) and I'm really excited about receiving it. So excited in fact that I would really like to get it earlier than the February ETA I originally pledged for.

Some of the early backers have been concerned about the lack of updates, photos and videos from the Tiko team and have been cancelling their pledges. This has opened spaces in the pledges with earlier estimated shipping dates. The other day I was fortunate that I refreshed the page at just the right moment and managed to change my pledge to one with a January shipment. That got me wondering if I could come up with something that would alert me when the slots opened up.

It turns out I was not alone in my thinking as there is a [project on github](https://github.com/birla/kickstarter-pledge-watch-and-manage) that automates the whole process, including managing your pledge. The author notes that it is somewhat dubious and probably goes against kickstarter's T's & C's. So I decided that I'd have a go at rolling my own version that would just alert me.

Everything I read said that for scraping Python was the way to go. Having never written a line of python I thought it would be an interesting project to play with a new language. I quickly found [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) and after a few visits to a number of [tutorials](http://kennyledet.github.io/tutorials/2013/12/19/web-scraping-with-python-and-beautifulsoup.html) I had a script that would output the info I wanted to the command line.

## Automating and alerting

This first script would have been fine if I was always sat at my laptop but ultimately isn't anymore useful than hitting cmd-r on the kickstarter page itself. So I needed a way for the script to alert me. I remembered playing with [PushOver](https://pushover.net/) a while back to get alerts from my minecraft server. I created an account with them and set up an application, looked at their [python documentation](https://pushover.net/faq#library-python), installed the iOS app on my phone and that was that.

All that was left was to automate running the script. I've heard of cron jobs but had never needed to create one until now. A quick google lead me to [a simple tutorial](http://www.maclife.com/article/columns/terminal_101_creating_cron_jobs) and I was up and running.

## Putting it all together

The cron job triggers the script, the script scrapes for all of the reward info from the kickstarter page. If there is a reward with a ship date in November and there are currently less than the maximum number of backers it triggers a PushOver notification. My phone then receives the notification and pushes it to my pebble.

Within five hours of launching the cron job my pebble buzzed to tell me the November slot was available and after some over-excited mashing of the keyboard I secured the slot.

Win!

## The script itself

As I mentioned earlier I have never written a line of python before this project. The code below works but it definitely could be refactored and improved (try not to judge me).

    #!python
    import requests
    from bs4 import BeautifulSoup
    import httplib, urllib

    url = "https://www.kickstarter.com/projects/tiko3d/tiko-the-unibody-3d-printer/description"
    r = requests.get(url)

    soup = BeautifulSoup(r.content)

    rewards = soup.find_all("li", {"class": "NS-projects-reward"})

    print "nn"

    for reward in rewards:
        rewardCost = str(reward.find("h5").find("span").text)
        shipDate = str(reward.find("time").text)
        numBackers = str(reward.find("span", "num-backers").text)
        x = int(numBackers.replace(" backers", "").replace(",", ""))

        # backersClean = backers.rstrip()
        if shipDate == "Nov 2015" and rewardCost == "$179 USD":
          if x < 2500:
            conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
              urllib.urlencode({
                "token": "[TOKEN]",
                "user": "[USER]",
                "message": "$179 reward now available",
                "device": "iphone",
              }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()
        if shipDate == "Nov 2015" and rewardCost == "$139 USD":
          if x < 400:
            conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
              urllib.urlencode({
                "token": "[TOKEN]",
                "user": "[USER]",
                "message": "$139 reward now available",
                "device": "iphone",
              }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()
        if shipDate == "Nov 2015" and rewardCost == "$99 USD":
          if x < 100:
            conn = httplib.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
              urllib.urlencode({
                "token": "[TOKEN]",
                "user": "[USER]",
                "message": "$99 reward now available",
                "device": "iphone",
              }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()


**UPDATE:** Disappointingly it looks like [my Tiko is never going to arrive](https://www.kickstarter.com/projects/tiko3d/tiko-the-unibody-3d-printer/posts/1809879) as the creators seem to have run out of money.

**ADDITIONAL UPDATE (2021):** Tiko 3D never delivered anything, the team behind it kept all the money and all the backers lost their investments. And that kids is why you shouldn't back projects on kickstarter!
