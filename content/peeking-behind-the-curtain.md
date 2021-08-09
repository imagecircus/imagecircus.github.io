title: Peeking behind the curtain
date: 2015-05-03
category: Web Development
tags: hosting, ubuntu, vps, wordpress

Recently I've begun experimenting with things I would have thought impossible a few years ago. [The python script I wrote last week](/over-engineering-firstworldproblems/) and the data scraping project that I've yet to write about have both made me realise that none of this stuff is witchcraft. With my hosting renewal coming up I started wondering about moving from shared hosting to a VPS.

For the last decade my personal sites and email accounts have been hosted with the same shared hosting company. They have always provided me with excellent service for a reasonable price and I've always been happy to recommend them to my clients. Now that my requirements have reduced a little and I've been seeing VPS offered for a fraction of the cost I thought it worth investigating.

It's probably worth noting that none of my sites are high traffic or high importance. They consist of this blog and its predecessor, a domain I bought for my wedding, a development server and my mostly dormant company site. I'm not sure that I'd be confident deploying a client's site on a VPS yet but for my needs it works just fine.

## New adventures in hosting

For my first foray into configuring my own hosting I chose to go with [Digital Ocean's $10 VPS](https://www.digitalocean.com/?refcode=96d77d24bdc0). I had some teething troubles with their one-click WordPress installer so I decided to roll my own by following their excellent documentation.

- [Initial Server Setup with Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04)
- [Additional Recommended Steps for New Ubuntu 14.04 Servers](https://www.digitalocean.com/community/tutorials/additional-recommended-steps-for-new-ubuntu-14-04-servers)
- [Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04)
- [Install Wordpress on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-on-ubuntu-14-04)
- [Configure Secure Updates and Installations in WordPress on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-configure-secure-updates-and-installations-in-wordpress-on-ubuntu)

All of that got this site up and running and allowed me to use WordPress' auto update feature. The only thing left to do was to get a mail server set up. I decided to take the easy option and went with [Zoho](https://www.zoho.com/). All you have to do is create a CNAME record for the domain to prove to Zoho that you own it and then you need to set two MX records and it's good to go.

## The whole kit and caboodle

Having been encouraged by getting this blog working I span up another droplet and went through the first three tutorials again to get a LAMP stack up and running. This time I remembered to create a snapshot of it so in future I can just create a droplet with my preferences in one click.

Once it was up and running I looked at the content I needed to migrate:

- Company site: A few php files
- Old blog: A WordPress site
- Development server: Several sites, mostly php but a few also require MySQL databases
- Wedding site: A holding page

I guessed that it would be possible to host all of these on one droplet, as they're all fairly low traffic sites. I looked into setting up virtual hosts in apache and was relieved to find that again Digital Ocean's documentation didn't let me down.

- [Set Up Apache Virtual Hosts on Ubuntu 14.04 LTS](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-14-04-lts)

I had decided that there was no point continuing with the old blog as I hadn't posted in it for over a year. However I wanted to be a good net citizen and not break any old inbound links. So I decided to import the content of the old blog here and set up a redirect for old links. To redirect all requests from one domain to another all you need is these two lines in the .htaccess file on the old domain.

\[plain\] RewriteEngine on RewriteRule (.\*) http://www.newdomain.com/$1 \[R=301,L\] \[/plain\]

Having set up four virtual hosts, transferred all of the required files, set up my .htaccess file and pointed my name servers at Digital Ocean my hosting was done. Setting up Zoho for each domain was a little laborious but as they provide free mail servers I'm not about to complain.

## Was it worth it?

Compared to standard shared hosting you'll have a lot more passwords to keep track of, you'll spend most of your time in terminal rather than a web based control panel and you are your own tech support. It's definitely not for everyone and your mileage may vary but I learnt a lot from the process and have cut my hosting bill by about 66%.
