def get_domain_name(url):
    if url[0] == 'h':
        num = url.split('://')
        url = num[1].split('.')
        if len(url) == 3 and url[0][0] == 'w':
            return url[1]
        elif len(url) == 3:
            return url[0]
        else:
            return url[0]
    else:
        num = url.split('.')
        return num[1]


assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"
assert get_domain_name("http://github.com/carbonfive/raygun") == 'github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Correct')

# The get_domain_name function takes an 'url' string,
# extracts the domain name from it, and returns it as a string.