---
layout: post
permalink: /:title/
title: The fastest path to a single page website
tags: [DoOO]
---
This is a post I put together to show the ITS Tech Bar Students I work with how to quickly put a static page up on their domain. I am assuming almost no prior knowledge of HTML, CSS, or cPanel. The only thing you need ahead of time is a domain at [Reclaim Hosting](https://reclaimhosting.com). 

When we are finished you will have a page that looks like this: [demo.jadin.me](https://demo.jadin.me)

If you already have content on your root domain (ex: [jadin.me](https://jadin.me)) that you don't want to get rid of, you might want to [make a subdomain first](http://knight.domains/kb/creating-a-subdomain/). 

## Creating index.html

First, we will make an index.html file. The simplest way to do this will be to use cPanel's File Manager tool.

1. Log in at [reclaimhosting.com](reclaimhosting.com), click on **cPanel**, then the name of your domain.
2. Click on ![cPanel File Manager](https://i.imgur.com/0JXPNAK.png)
3. Select the folder named **public_html**, if you want to put this page on your subdomain (ex: **demo.jadin.me**), click folder named after that subdomain instead.
4. Click ![new file button](https://i.imgur.com/e5cOxXl.png)
5. Name the file **index.html** (case matters!) and click **Create New File**
6. Next, select the file and click ![edit button](https://i.imgur.com/ucduek5.png)
7. Click **Edit**
8. Paste the HTML below into your index.html file:

```html
<!DOCTYPE html>
<html>
        <head>
                <title>Demo Page</title>
                <link rel="stylesheet" type="text/css" href="css/main.css">
        </head>
        <body>
                <h1>Hello world!</h1>

                <h2>About this site</h2>

                <p>This simple page is used to demonstrate how HTML controls the content on a webpage, and how CSS applies styling to the page. You can view or download all (both) of the files needed for this page on my <a href="https://www.jadin.me/the-fastest-path-to-a-single-page-website/">blog</a>. The blog post also includes basic instructions on hosting these files on your domain or subdomain if you are using Reclaim Hosting.</p>

                <h2>About Domain of One's Own</h2>

                <p>You can find more information about Domain of One's Own at St. Norbert College at <a href="http://knight.domains">knight.domains</a>.</p>

                <h2>About my dog</h2>

                <p>Here is a picture of Annie. Feel free to use this picture on your own site. When you are making a website, only use images that you have permission to use.</p>

                <img src="https://i.imgur.com/gWfHJNJ.jpg" alt="picture of my dog">
        </body>
</html>
```

1. Click **Save Changes**
2.  Click **Close**
3.  Go to your site and take a look! 

## Creating main.css
We have the basic content there, but it should look a bit off if you compare it to my demo page at [demo.jadin.me](https://demo.jadin.me). It looks strange because it is missing style information, we can fix that by adding a main.css file!

1. Go back to the cPanel file manager
2. In the same folder where you have index.html, click ![new folder button](https://i.imgur.com/5vseFrE.png)
3. Name the folder **css** (case matters!) and click **Create New Folder**
4. Select the css folder you just created, and create a new file in this folder called **main.css**
5. You should now have an **index.html** file, a **css** folder, and a **main.css** folder inside it:
```
├── css
│   └── main.css
└── index.html
```
6. Edit **main.css** and paste the css below into the file:

```css
* {
    font-family:'Helvetica', 'Arial', 'Sans-Serif';
}
body {
    margin: 60px auto;
    width: 70%;
}
a {
    font-weight: bold;
    text-decoration: none;
    color: green;
}
a:hover {
    text-decoration: underline;
}
h1 {
    font-size: 3em;
}
h2 {
    font-size: 2em;
}
p {
    font-size: 1.5em;
    line-height: 1.4em;
    color: black;
}
```

7. Click **Save Changes** and **Close**
8. Check out your site again and see how it looks!