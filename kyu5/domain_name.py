"""
Write a function that when given a URL
 as a string, parses out just the 
 domain name and returns it as a 
 string
"""
def domain_name(url):
    prefixes = ["https://", "http://", "www."]

    for i in prefixes:
        if url.startswith(i):
            url = url[len(i):]

    domain = url.split("/")[0].split(".")[0]
    print(domain)

domain_name("http://codewars.com")