from datetime import datetime
import csv
import bs4
import requests

User_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" # this is to identify on what kind of device the request is going to run and print the output accordingly.
Request_header={
                "user_agent":User_agent,
                "Accept-language":"en-US, en;q=0.5",
}
def get_page_html(url):
    res=requests.get(url,headers=Request_header)
    return res.content


def extract_product_price(soup):
    main_price_div=soup.find('div',attrs={"class":'product-price css-11s12ax is--current-price css-tpaepq'})
    price=main_price_div.text.strip().replace("MRP","").replace(":","").replace(" ","").replace("₹","")
    try:
        float(price) #check if the price can be converted to a number
        return price
    except ValueError:
        print("The content cant be converted to a number")
        exit()

def extract_product_name(soup):
    main_title_name=soup.find("h1",attrs={"id":"pdp_product_title","class":"headline-2 css-16cqcdq"})
    title=main_title_name.text.strip()
    return title

def extract_product_rating(soup):
    main_rating_part=soup.find("p",attrs={"class":"d-sm-ib pl4-sm"})
    main_rating=main_rating_part.text.strip()
    return main_rating

def extract_product_color(soup):
    main_details_part=soup.find("ul",class_="description-preview__features pt8-sm pb6-sm ncss-list-ul")
    details_section=main_details_part.find("li",class_="description-preview__color-description ncss-li")
    color=details_section.text.strip().replace("Colour Shown: ","")
    return color

def extract_product_style(soup):
    main_details_part=soup.find("ul",class_="description-preview__features pt8-sm pb6-sm ncss-list-ul")
    details_section=main_details_part.find("li",class_="description-preview__style-color ncss-li")
    color=details_section.text.strip().replace("Style: ","")
    return color  
    
def extract_product_info(url):
    productinfo={}
    print(f"Scraping URL:{url}")
    html = get_page_html(url=url)
    soup=bs4.BeautifulSoup(html, features="lxml") #Parse the HTML content with Beautiful
    productinfo["Name"]=extract_product_name(soup)
    productinfo["Price"]=extract_product_price(soup)
    productinfo["Rating"]=extract_product_rating(soup)
    productinfo["Color"]=extract_product_color(soup)
    productinfo["Style"]=extract_product_style(soup)
    return productinfo


if __name__ == "__main__":
    products_data = []
    with open("nikeurls.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            url = row[0]
            product_data = extract_product_info(url)
            products_data.append(product_data)


    if products_data:
        output_file_name = "output-{}.csv".format(datetime.today().strftime("%d-%m-%Y"))
        with open(output_file_name, "w", newline="") as outputfile:
            writer = csv.DictWriter(outputfile, fieldnames=products_data[0].keys())
            writer.writeheader()
            writer.writerows(products_data)
            print("Output written in a CSV file.")
