randomData = {
    "insuranceCompany": "string",
    "mailingAddress": "string",
    "insured": {
        "name": "string it should look normal not in full capital letter or full small letter",
        "phone": "string",
        "email": "string it should be in all small letter",
        "street": "string it should not be in full uppercase or full lowercase also",
        "city": "string the first letter should be capital and other small",
        "state": "string this should be the code of that state like for Texas you will use TX",
        "zipCode": "string",
    },
 
    "claimDetails": {
        "claimNumber": "string",
        "policyNumber": "string",
        "typeOfLoss": "string",
        "dates": {
            "contacted": "M/D/YYYY H:MM A Look for the date carefully I don't want to see N/A or something else you have to give some date and if you don't find the date give a random date",
            "loss": "M/D/YYYY H:MM A Look for the date carefully I don't want to see N/A or something else you have to give some date and if you don't find the date give a random date",
            "received": "M/D/YYYY H:MM A Look for the date carefully I don't want to see N/A or something else you have to give some date and if you don't find the date give a random date",
            "inspected": "M/D/YYYY H:MM A Look for the date carefully I don't want to see N/A or something else you have to give some date and if you don't find the date give a random date",
            "entered": "M/D/YYYY H:MM A Look for the date carefully I don't want to see N/A or something else you have to give some date and if you don't find the date give a random date",
            "estimateCompleted": "M/D/YYYY H:MM A Look for the date carefully I don't want to see N/A or something else you have to give some date and if you don't find the date give a random date",
        },
        "priceList": "string",
        "tax_jurisdiction": "string it should be like 3% or 7% or None you cannot give it N/A if it is not available just give it a 'None' the None also should be a string",
    },
    "policyType":"either Homeowner or Commercial",
    "amount": "string this should be the Less Deductible amount and if it doesn't exist find something similar but it should not be net claim or  Total Recoverable Depreciation or  Replacement Cost Value or anything else this should be very accurate no exception accepted and it should be a number with some comma or something",
    "estimation": [
       {
            "section": "section name it should be the section in some places the section can be roof or front elivation or left elivation or something like those"  ,
        }

    ],
}
