"""We store the data in a dictionary such that key corresponds to category name and
value corresponds to products in 
categories={"food_grains":["rice", "dal", "wheat"],
	"furniture":["table", "sofa", "chair"],
	"electronics":["mobile", "tv", "tablet"],
	"cosmetics":["cream", "perfume", "lotion"]}
			
user_input= str(input("Please Enter the quantity, product name and initial cost: \n"))
quantity, product, cost=user_input.split(" ")

def findGst(key):
	if (key=="food_grains"):
		gst=0
	elif (key=="furniture"):
		gst=0.05
	elif (key=="electronics"):
		gst=0.18
	elif (key=="cosmetics"):
		gst=0.28
	else:
		print("Product Not Found!")
	final_cost= int(quantity)*(float(cost)+(float(cost)*gst))
	gst_amount= float(cost)*gst
	print("The amount of GST applied is: ", round(gst_amount,2))
	print("The final cost of the product is : ",final_cost)
			
for key, value in categories.items():
	if product.lower() in value:
		findGst(key)# your code goes here