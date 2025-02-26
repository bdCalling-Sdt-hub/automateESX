def getItemsPrompt(sectionName):
    return """
    You are the best text to json converter in the world. You extract valuable json data from text based on the instructions that are given to you. I will give you some text you have to extract json data from that the structure of that json data should look like this "items": [
                {
                    "desc": "string - Full description of the line item",
                    "quantity": "number - Amount of work to be done",
                   
                }
            
            ] and here are some rules you must follow 
rules: 
- there should be no comment in the json data
- you will only return the items from this section""" + str(sectionName) + """
- you have to give every estimate item from this section to that json array

here is the text I was talking about
    """