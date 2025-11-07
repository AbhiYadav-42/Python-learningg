import json

password = {"abhi@Gmail":  "mypass@123",
            "github"    :  "supersecert",
            "outlook"   :  "ABHI@12"}
with open("Password.json", "w") as f:
  json.dumps(password,f)
  
