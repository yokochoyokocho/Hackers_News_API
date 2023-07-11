import requests
import time


def main():
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")

    dic = response.json()  # json形式にパース（解析）

    lists = []
    for list in range(0, 5):
        lists.append(dic[list])

    for number in lists:
        response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{number}.json?print=pretty")
        dic = response.json()

        title = dic["title"]

        if "url" in dic:
            url = dic["url"]
            print(f"'title': {title}, 'link': {url}")

        else:
            print(f"'title': {title}, 'link': NONE")

        time.sleep(1)  # ここで1秒止まる


if __name__ == "__main__":
    main()
