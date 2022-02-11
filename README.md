## University of Pittsburgh's Robotics and Automation Society's Website
Access it at https://www.pittras.org

Find deployment status here: https://github.com/Pitt-RAS/PittRAS/deployments/activity_log?environment=github-pages

## Viewing your website changes locally
Two options:
1) You can past the file path to any html file in the browser and it will open. Alternatively, on windows at least, you can just double click the html file and it will open in the browser automatically. Or you can do right click and then open with > your choice of browser. 

2) If you are a VScode user, add the extension called "Live Server". Once it's installed, close and reopen VScode. If you go to any html file, you will now see a "Go Live" button in the bottom right corner. You can click that to preview the current html file you are on.

## Navigating through the website locally
Every site page has a file extension of .html. You can see this by looking through the repo. However, you might notice when navigating through the website on a browser, you do not see the .html extension. This is because the .htaccess file redirects any file (/filename) that doesn't resolve to /filename.html. So, when published all the links will work properly with the help of .htaccess. 

Locally however, the links will remain broken making it kind of difficult to navigate through the site when working on a local copy. A simple solution would just be to append .html to broken file path in the browser. Just something to be aware of when working on the website locally. 

## Pre-publishing checklist
1) Ensure that no .html extensions are included in href's. **Note that if it's a link to an external webpage (base url is not wwww.pittras.org), then do not remove the .html extension. It is also okay to leave elements.html any other page or template pages that is not public (no hyperlink leads to them) as is.**
2) Spell check any modifications. Use VS code extension called "Code Spell Checker" for this.