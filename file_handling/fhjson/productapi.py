import requests,json
data=requests.get('https://dummyjson.com/products')
product_data=data.json()
print(type(product_data))  #<class,dict>
products=product_data['products']
print(type(products)) #<class,list>
print(len(products))  #30

#Transform
beauty_products=[]
for prod in products:
    if prod['category'] == 'beauty':
        beauty_products.append({'id':prod['id'],'name':prod['title'],'price':prod['price']})


print(len(beauty_products))   # 5
#Load into json file
fp=open('beauty.json','w')
json.dump(beauty_products,fp)
print("New Json file created!")
fp.close()