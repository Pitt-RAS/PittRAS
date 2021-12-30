## University of Pittsburgh's Robotics and Automation Society's Website
Access it at https://www.pittras.org

Find deployment status here: https://github.com/Pitt-RAS/PittRAS/deployments/activity_log?environment=github-pages

## Navigating through the website locally
Every site page has a file extension of .html. You can see this by looking through the repo. However, you might notice when navigating through the website on a browser, you do not see the .html extension. This is because the .htaccess file redirects any file (/filename) that doesn't resolve to /filename.html. So, when published all the links will work properly with the help of .htaccess. 

Locally however, the links will remain broken making it kind of difficult to navigate through the site when working on a local copy. A simple solution would just be to append .html to broken file path in the browser. Just something to be aware of when working on the website locally. 

## Pre-publishing checklist
1) Ensure that no .html extensions are included in href's. **Note that if it's a link to an external webpage (base url is not wwww.pittras.org), then do not remove the .html extension. It is also okay to leave elements.html any other page or template pages that is not public (no hyperlink leads to them) as is.**
2) Spell check any modifications. Use VS code extension called "Code Spell Checker" for this.