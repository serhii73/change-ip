from random import choice
import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    r = requests.get(
        "https://raw.githubusercontent.com/cvandeplas/pystemon/master/user-agents.txt")
    with open('useragents.txt', 'w') as output_file:
        output_file.write(r.text)

    useragents = open("useragents.txt").read().split("\n")
    proxies = open("proxylist.txt").read().split("\n")
    url = 'http://sitespy.ru/my-ip'
    proxy = {"http": choice(proxies)}
    useragent = {"User-Agent": choice(useragents)}
    r = requests.get(url, headers=useragent, proxies=proxy)
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup.find("div", {"class", "ip-block"}).text.strip())
