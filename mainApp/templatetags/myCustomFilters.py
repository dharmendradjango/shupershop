from django import template
register= template.Library()

@register.filter(name="paymentMode")
def paymentMode(Request,num):
    if(num==0):
        return "COD"
    else:
        return "NetBanking"
    

@register.filter(name="paymentStatus")
def paymentStatus(Request,num):
    if(num==0):
        return "Pending"
    else:
        return "Done"
    

@register.filter(name="orderStatus")
def orderStatus(Request,num):
    if(num==0):
        return "Order is Placed"
    if(num==1):
        return "Order is Packed"
    if(num==2):
        return "Ready is Dispatch"
    if(num==3):
        return "Dispatched"
    if(num==4):
        return "Out for Delivery"
    else:
        return "Delivered"
    

@register.filter(name="paymentCondition")
def paymentCondition(mode,status):
    if(mode=="1" and status=="0"):
        return "True"
    else:
        return "False"