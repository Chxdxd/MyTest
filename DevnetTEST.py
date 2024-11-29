import requests

def main():
    
    r = requests.get(url="https://api.restful-api.dev/objects").json()
    #print(r)
    for element in r:
        #print(f'{element}\n')
        if(element['id']=='9'):
            print(element['data']['Description'])
            
        if(element['id']=='12'):
            print(element['data']['Price'])
            
    
if __name__ == "__main__":
    main() 
    
    