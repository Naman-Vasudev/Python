import requests
city_name=input("Enter a name of city: ")

def generate_report(c):
    url="https://wttr.in/{}".format(c)
    try:
        data=requests.get(url)
        T=data.text
    except:
        T="Error Occurred"
    
    print(T)

generate_report(city_name)