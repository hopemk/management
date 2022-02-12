def is_valid(data):
    error={}
    index = 0
    for item in data:
        errors=[]
        product = Product.get_object(data['product'])
        if not product:
            errors.append({"product not available"})
        items_sold = data['items_sold'] 
        if not items_sold:
            errors.append({"missing parameter -> items sold"})
        paid = data['paid']
        if not paid:
            errors.append({"missing parameter -> paid"})
        if len(errors) > 0:
            error[index] = errors
        index += 1
    if not error == {}:
        return errors
    else:
        return False