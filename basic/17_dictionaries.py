info = {"name":"Maitri",
        "age":22,
        "city":"London",
        "Eligible":True}

#accessing sinlgle value
print(info["name"])
#adding new key-value pair
info["profession"] = "Engineer"
print(info)
#accessing multi values
print(info["name"], info["age"], info["city"])
#accessing keys
print(info.keys())
#accessing values
print(info.values())


#update()
info.update({"age":20})
print(info)

#pop()
info.pop("city")
print(info)

#popitem()
info.popitem()# delete last item
print(info)

#clear()
info.clear()
print(info)