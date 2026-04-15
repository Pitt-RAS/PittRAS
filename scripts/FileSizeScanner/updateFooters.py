import os
import re

# Set this to the folder containing your HTML files ('.' means current directory)
directory = '../' 

# The new HTML we want to inject
new_footer = '<div id="footer"></div>'
script_tag = '<script src="assets/js/loadCommonFooter.js"></script>\n\t\t\t<script src="assets/js/main.js">'

# Walk through all files and folders in the directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        # Only target HTML files, and ignore your new common footer file!
        if filename.endswith('.html') and filename != 'commonFooter.html':
            filepath = os.path.join(root, filename)
            
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 1. Replace the entire footer block (from <footer> to </footer>)
            # The re.DOTALL flag allows it to match across multiple lines
            # Modify the '<footer' part if your footer uses a different tag (like <div class="footer">)
            updated_content = re.sub(r'<footer.*?>.*?</footer>', new_footer, content, flags=re.DOTALL | re.IGNORECASE)
            
            # 2. Inject the script right before the closing </body> tag
            # We check if the script is already there so we don't accidentally add it twice
            if 'loadCommonFooter.js' not in updated_content:
                updated_content = re.sub(r'<script src=".*?main.js">', script_tag, updated_content, flags=re.IGNORECASE)
            
            # Write the changes back to the file
            if content != updated_content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                print(f"Updated: {filepath}")

print("Done updating files!")