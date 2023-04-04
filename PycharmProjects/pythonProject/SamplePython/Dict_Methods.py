car = {
    "Brand": "Ford",
    "model": "Mustang",
    "year": 1994
}

# copy
Vehicle = car.copy()

# get
print(car.get("year"))

# items
print(car.items())

# values
print(car.values())

# keys
print(car.keys())

# pop
print(car.pop("Brand"))
print(car)

# update
car.update({"color": "red", "Type": "4"})
print(car)


# removes last inserted
car.popitem()
print(car)
