users =[
{"ID":1,"Total":120,"coupon":"P10"},
{"ID":2,"Total":120,"coupon":"F50"},
{"ID":3,"Total":120,"coupon":"P30"},
]
discounts={
"P10":(0.2,0),
"F50":(0.5,0),
"P30":(0,0),
}

for user in users:
    percentage,fixed=discounts.get(user["coupon"],(0,0))
    discount=user["Total"]*percentage+fixed
    print(f"{user["ID"]} paid total of {user["Total"]} for next time discount of {discount}")
