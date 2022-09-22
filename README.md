# University of Pittsburgh's Robotics and Automation Society's Website
Access it at https://www.raspitt.org. This is a static HTML website and can be edited on any computer that has access to an text editor - no setup or environment required. See section below for how to navigate the website locally.

Find deployment status here: https://github.com/Pitt-RAS/PittRAS/deployments/activity_log?environment=github-pages

# Making Modifications to the Website

## Important Note!

Anything put inside of this repo is public for everyone to see, including non-html files. If the user knows the relative file path, the file can be viewed. For example https://www.raspitt.org/LICENSE.txt will pull up the license file. **Proceed with caution! Do not store sensitive info in this repo!**

## Viewing your website changes locally
Two options:
1) You can paste the file path to any html file in the browser and it will open. Alternatively, on windows at least, you can just double click the html file and it will open in the browser automatically. Or you can do right click and then open with > your choice of browser. 

2) If you are a VScode user, add the extension called "Live Server". Once it's installed, close and reopen VScode. If you go to any html file, you will now see a "Go Live" button in the bottom right corner. You can click that to preview the current html file you are on. An alternative is "Live Preview" by microsoft which lets you preview the webpage inside of visual studio. Click on HTML file and then select preview in the upper right hand corner.

## Navigating through the website locally
Every site page has a file extension of .html. You can see this by looking through the repo. However, you might notice when navigating through the website on a browser, you do not see the .html extension. This is because the .htaccess file redirects any file (/filename) that doesn't resolve to /filename.html. So, when published all the links will work properly with the help of htaccess. 

Locally however, the links will remain broken making it kind of difficult to navigate through the site when working on a local copy. A simple solution would just be to append .html to the broken file path in the browser (but this might be different for say the projects file, which is both a directory and an html file). This also depends on the browser being used because some browsers are smart and try to autocomplete the link. Just something to be aware of when working on the website locally. 

Lastly, the contact page takes a bit to load locally. This is because the mailchimp form is trying to load its thing but it's unable to. 

## Pre-publishing checklist
1) Ensure that no `.html` extensions are included in href's. **Note that if it's a link to an external webpage (base url is not wwww.raspitt.org), then do not remove the `.html` extension. It is also okay to leave `elements.html` and any other page or template pages that is not public (no hyperlink leads to them) as is.**
2) Spell check any modifications. Use VS code extension called "Code Spell Checker" for this.
3) Test on commonly used web browsers. This typically includes Chrome, Safari, and Firefox. When testing, be sure to test resizing the window to ensure things scale properly
and to use preview the webpage on mobile as well.

## Post-publishing checklist
1) It's wise to check website performance on the pages that were modified using tools such as https://tools.pingdom.com/, https://gtmetrix.com/ (recommended), and https://www.webpagetest.org/ . Make sure any added content doesn't significantly impact load times and performance. 
2) Additionally, a script has been provided in `scripts/FileSizeScanner` that will flag any files that's over a certain size. See the README.md in `scripts/FileSizeScanner` for how it works. 

## Using the maintenance page
Only use this method when absolutely necessary. If only static HTML updates are needed, do your development on a branch other than main and then merge into main when finished. The use of the maintenance page is only for making modifications to the website where the changes cannot be tested on locally (requires the website being live). This means that development will have to be done on the main branch. Unfortunately, it doesn't seem like github pages supports hosting multiple branches so this will have to do for now. 

How it works:
1) The website will load the maintenance page instead of the original content of the website.
2) There is an invisible button in the bottom left corner of the webpage (might need to scroll down to get to it). This button will take you to the original content of the website where you can carry out testing as needed. Note that some hyperlinks might be broken (for obvious reasons) so it is recommended to test hyperlinks locally (see navigating trough the website locally section) and only use this method when testing performance (like website load times).

Steps:
1) Rename `index.html` to `indexbackup.html` (use the exact filename)
2) Rename `maintenance.html` to `index.html` (use the exact filename)
3) Commit and push changes to main
4) Update and test the website as you please
5) When finished with all the changes, first revert `index.html` to `maintenance.html` and then revert `indexbackup.html` to `index.html`

