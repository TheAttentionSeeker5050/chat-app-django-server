# from .models import AppUser
import json


# Create your tests here.
def createMockData():
    with open("mock_data.json", "r") as f:
        data = json.load(f)
        
    print(data)
    
    
createMockData()