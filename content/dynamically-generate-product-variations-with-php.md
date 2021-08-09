title: Dynamically Generate Product Variations with PHP
date: 2013-08-16
category: Web Development
tags: dynamic, image, jquery, php, product, variations

**Note: This post was originally published on iamianwright.com it's been moved here for archival purposes.**

"Why can't I just dynamically generate product variations with PHP?", I thought, "Surely that must be how other people do this!".

I've been working on an ecommerce site, with Drupal Commerce, for a business that a friend and I have started up. We're selling sports clothing that is made to order. The customer is able to pick a style, two colours and a size. There are eighteen available colours so for each style there are over three hundred variations that could be chosen. As well as building the site I am creating artwork for the products. They are fairly simple vectors that use only two flat colours with a black outline on top.

As simple as they were generating over three hundred images per product was **not** an option.

It also turns out that all of the commerce platforms I looked at, including drupal commerce, expect you to define all of the variations and then assign an image to each. There are ways of importing product catalogues into DC but it seemed unnecessary as the products are all made to order so there's no stock to track.  So this became my [first challenge](http://www.drupalcommerce.org/comment/8102 "first challenge").  Eventually after reading half of the internet I found a drupal module called [Commerce Customizable Products](https://drupal.org/project/commerce_custom_product "Commerce Customizable Product").  It allows you to specify fields the user has to complete before adding a product to their cart. I used it to add size and colour options along with two image upload fields.

So that took care of capturing the information from the customer's order but I was no closer to generating the product images. After scouring yet more of the internet I posted to [stackoverflow](http://stackoverflow.com/questions/18244170/how-can-i-generate-two-colour-product-images-dynamically "stackoverflow") in the hope the wisdom of crowds would provide me an answer. Sadly there were none forthcoming. I continued reading everything I could about manipulating images with PHP and eventually I solved my own problem.

To create the images dynamically I have created one GIF that contains the white background, a pure red and pure blue region to define the primary and secondary areas. This is run through GD which changes the red and blue to the user selected colours. Then a transparent PNG is merged on top which contains the black outline and the company logo (see example at top of post).

I then created a page with selection boxes for colours and style and used a little jQuery to pass those options to the PHP that generates the image.  When the script receives the options it uses them to create a filename for the image that it will produce but first it checks to see if that file already exists.  If it does then it returns the existing file if not it creates it on the server for future use and returns it.

I have put up a demo with all the scripts that you need to [dynamically generate product variations with PHP](http://clients.imagecircus.com/color/index.php "dynamically generate product variations with PHP").  There's a [link to a zip file](http://clients.imagecircus.com/color/product-images.zip "link to a zip file") that includes all of the code and some images on that page too.
