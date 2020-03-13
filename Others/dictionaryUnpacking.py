values = {
    "left": "right",
    "up": "down"
}

#values = {**values, **{v: k for k, v in values.items()}}

values.update({v: k for k, v in values.items()})

print(values)

print(values["right"])
print(values["down"])