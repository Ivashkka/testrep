import requests
from bs4 import BeautifulSoup

avito_url = "https://www.avito.ru/moskva/odezhda_obuv_aksessuary/obuv_muzhskaya/krossovki-ASgBAgICAkTeArqp1gLOvQ68nJQC?cd=1&f=ASgBAQICAkTeArqp1gLOvQ68nJQCAUDkjg4UmJrOAQ&s=104"

def get_html_from_url(url):
    res = requests.get(url, timeout=5);
    res_code = res.status_code
    match res_code:
        case 200:
            print("code 200! It's ok!")
            res = res.text
        case 404:
            print("code 404! You made mistake!")
            res = "NONE"
        case 403:
            print("code 403! Access forbiden!")
            res = "NONE"
        case _:
            print("{res_code}! I don't know what does it mean!")
            res = "NONE"
    return res

def main():
    boots_html = get_html_from_url(avito_url)
    boots_bs = BeautifulSoup(boots_html, "html.parser")
    try:
        price = boots_bs.find("div", class_="iva-item-priceStep-uq2CQ").getText()
        print(f"boots price: {price}")
    except:
        print("ERROR!")


if __name__ == "__main__":
    main()
