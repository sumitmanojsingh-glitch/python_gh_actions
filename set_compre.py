favourite_chai=[

    "Masala Tea","Elaichi Tea","Masala Tea"
]

unique_chat={chai for chai in favourite_chai}
print(unique_chat)

Teas={

    "Masala Chai":["ginger","clove","pe,pper"],
     "spicy Chai":["ginger","clove"],
      "kadak Chai":["ginger","clove","cardamom"]
}

pure_chai={ spice for ingridients in Teas.values() for spice in ingridients}

print(pure_chai)