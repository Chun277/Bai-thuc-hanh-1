import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
bangdanhgia = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
def getsoup(url):
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    return BeautifulSoup(res.text, "html.parser")
def gettheloai(url):
    soup = getsoup(url)
    breadcrumb = soup.select("ul.breadcrumb li a")
    if len(breadcrumb) >= 3:
        return breadcrumb[2].get_text(strip=True)
    return "Unknown"
def scrapetrang(url):
    soup = getsoup(url)
    ds = []
    for sach in soup.select("article.product_pod"):
        ten = sach.select_one("h3 > a")["title"]
        gia = float(sach.select_one("p.price_color").text.strip()[2:])
        danhgia = bangdanhgia[sach.select_one("p.star-rating")["class"][1]]
        tinhtrang = sach.select_one("p.availability").text.strip()
        link = "https://books.toscrape.com/catalogue/" + sach.select_one("h3 > a")["href"].replace("../", "")

        ds.append({
            "ten": ten,
            "gia": gia,
            "danhgia": danhgia,
            "tinhtrang": tinhtrang,
            "link": link
        })
    return ds, soup.select_one("li.next > a")
dulieu = []
trang = "https://books.toscrape.com/catalogue/page-1.html"
for i in range(10):
    print(f"Dang lay du lieu cua trang {i + 1}...")
    ds, trangtiep = scrapetrang(trang)
    dulieu.extend(ds)
    if trangtiep:
        trang = "https://books.toscrape.com/catalogue/" + trangtiep["href"]
    else:
        break
    time.sleep(0.5)
print("Dang lay the loai cua tung quyen sach...")
for i in range(len(dulieu)):
    dulieu[i]["theloai"] = gettheloai(dulieu[i]["link"])
    if (i + 1) % 20 == 0:
        print(f"  {i + 1}/{len(dulieu)}")
    time.sleep(0.3)
df = pd.DataFrame(dulieu)
df = df[["ten", "gia", "danhgia", "tinhtrang", "theloai", "link"]]
df.to_csv("datasach.csv", index=False, encoding="utf-8")
print(df)
