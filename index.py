from bs4 import BeautifulSoup

# Open the HTML file
with open("index copy.html", "r") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Replace the text with Lorem Ipsum
for tag in soup.stripped_strings:
    tag.replace_with("Lorem Ipsum")

# Write the modified HTML content to a new file
with open("modified_file.html", "w") as file:
    file.write(str(soup))