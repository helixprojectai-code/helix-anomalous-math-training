```python
     import os
     from urllib.request import urlopen
     from bs4 import BeautifulSoup

     def validate_links(directory="website"):
         for filename in os.listdir(directory):
             if filename.endswith(".html"):
                 with open(os.path.join(directory, filename), "r") as f:
                     soup = BeautifulSoup(f, "html.parser")
                     for link in soup.find_all("a"):
                         href = link.get("href")
                         if href.startswith("http"):
                             try:
                                 response = urlopen(href)
                                 if response.getcode() != 200:
                                     print(f"Broken link in {filename}: {href}")
                             except Exception as e:
                                 print(f"Error checking {href} in {filename}: {e}")
                         else:
                             local_path = os.path.join(directory, href)
                             if not os.path.exists(local_path):
                                 print(f"Broken local link in {filename}: {href}")

     if __name__ == "__main__":
         validate_links()
