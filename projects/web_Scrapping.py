# Web Scrapping

import requests
from bs4 import BeautifulSoup as bs

# https://www.swiggy.com/collections/46147?type=rcv2

flipk_url = ["https://www.flipkart.com/mobiles/~cs-peapbg1n6e/pr?sid=tyy%2C4io&collection-tab-name=Motorola+G31&param=5893&otracker=clp_banner_2_31.bannerX3.BANNER_mobile-phones-store_ILSWZ2597MY0&fm=neo%2Fmerchandising&iid=M_61d497d7-e85c-4052-9709-18176b34989c_31.ILSWZ2597MY0&ppt=clp&ppn=mobile-phones-store&ssid=3xdnr0lx6o0000001643616713434&sort=price_asc"]

headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36" } 

req = requests.get(flipk_url[0],headers=headers)

# cont = req.content
# print(cont)  To print the whole content of the particular web page

soup = bs(req.content,"html.parser")


mobile_props = soup.find_all(name="div",attrs={"class":"_3pLy-c"})

for props in mobile_props:
    title = props.find( name="div" , attrs={"class" : "_4rR01T"} ).get_text()
    star_rating = props.find( name="div" , attrs={"class" : "_3LWZlK"} ).get_text()
    ratings_reviews = props.find( name="span" , attrs={"class" : "_2_R_DZ"} ).get_text()
    mobile_specs  = props.find( name="ul" , attrs={"class" : "_1xgFaf"} )
    price = props.find( name="div" , attrs={"class" : "_25b18c"} ).get_text()
    delivery_date = props.find( name="div" , attrs={"class" : "_3tcB5a p8ucoS"} ).get_text()
    exchage_off = props.find( name="div" , attrs={"class" : "_2ZdXDB"} ).get_text()
    
    specsl = []
    for specs in mobile_specs:
        specsl.append(specs.get_text())


    print("\n    Web Srapping - Flipkart Webpage about a mobile   ")
    print("***************   Mobile Info  ************************  ")
    print("Name               : ",title)
    print("Star ratings       : ",star_rating)
    print("Ratings & Reviews  : ",ratings_reviews)
    print("Price in Rs.       : ",price)
    print("Delivery date      : ",delivery_date)
    print("Exchange Offer     : ",exchage_off)    
    print("Storage|SD details : ",specsl[0])
    print("Dimension| Display : ",specsl[1])
    print("Camera feautres    : ",specsl[2])
    print("Battery Strength   : ",specsl[3])
    print("OS Processor       : ",specsl[4])
    print("Warranty Details   : ",specsl[5])
    print("******************************************************  ")










"""
Alternative tto the last print Statement

for i in range(6):
    print("Specification ",i+1,"  : ",specsl[i])

"""