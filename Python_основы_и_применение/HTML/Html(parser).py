from html.parser import HTMLParser
import urllib.request
import re

sp = []
sp_final = []

def find(s):
    find_rez = [-1]
    slash = s.find('/')
    colon = s.find(':')
    quotes = s.find("'")
    double_quotes = s.find('"')
    if slash != -1:
        find_rez.append(slash)
    if colon != -1:
        find_rez.append(colon)
    if quotes != -1:
        find_rez.append(quotes)
    if double_quotes != -1:
        find_rez.append(double_quotes)
    find_rez.sort()
    if len(find_rez) == 1:
        return find_rez[0]
    elif find_rez[1] != -1:
        return find_rez[1]



# Import HTML from a URL
url = urllib.request.urlopen(input())
html = url.read().decode()
url.close()


class Parse(HTMLParser):
    def __init__(self):
        # Since Python 3, we need to call the __init__() function of the parent class
        super().__init__()
        self.reset()

    # Defining what the method should output when called by HTMLParser.
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            for name, link in attrs:
                #print(link)
                if name == "href":
                    if link.startswith(".."):
                        continue
                    elif link.startswith("www"):
                        sp.append(link)
                    elif link.startswith("http://"):
                        r = find(link[7:])
                        if r != -1:
                            #print(link[7:7 + r])
                            sp.append(link[7:7 + r])
                        else:
                            sp.append(link[7:])
                    elif link.startswith("https://"):
                        r = find(link[8:])
                        if r != -1:
                            sp.append(link[8:8 + r])
                        else:
                            sp.append(link[8:])
                    elif link.startswith("ftp://"):
                        r = find(link[6:])
                        if r != -1:
                            sp.append(link[6:6 + r])
                        else:
                            sp.append(link[6:])


p = Parse()
p.feed(html)
sp.sort()
for i in range(len(sp)):
    if sp[i] not in sp_final:
        sp_final.append(sp[i])
for j in range(len(sp_final)):
    print(sp_final[j])
