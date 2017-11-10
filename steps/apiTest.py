import requests

x = requests.get("http://samples.openweathermap.org/data/2.5/weather?zip=07110,us&appid=b1b15e88fa797225412429c1c50c122a1").json()


for i in x['weather']:
    try:
        assert("id" in i), "There is no ID"
    except Exception as e:
        print(e)
    try:
        assert("main" in i), "There is no main"
    except Exception as e:
        print(e)
    try:
        assert("description" in i), "There is no description"
    except Exception as e:
        print(e)

assert(x["name"] == 'Mountain View'), "Invalid Name"
