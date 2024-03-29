import sys
import requests

url = "http://google.com"


def brute(url, wordlist):
    try:
        for word in wordlist:
            url_final = "{}/{}".format(url, word.strip())
            response = requests.get(url_final)
            code = response.status_code
            if code != 404:
                print("{} -- {}".format(url_final, code))
    except Exception as Error:
        print("Algo de errado aconteceu")

if __name__ == "__main__":
    url = sys.argv[1]
    wordlist = sys.argv[2]

    with open(wordlist, "r") as file:
        wordlist = file.readlines()
        brute(url, wordlist)
