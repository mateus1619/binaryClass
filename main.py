from bs4 import BeautifulSoup
import requests

cookies = {
    'laravel_session': 'AdEsdDgOvLbkIT1zxo83OdyQZhhonP6dsVFrnnP4',
    '_ga': 'GA1.1.1330075857.1699994543',
    '_fbp': 'fb.2.1699994543339.690699131',
    '_clck': 'i0wsxo|2|fgp|0|1413',
    'cademi_auth_2831': 'eyJpdiI6Img0S3l3ekpxNGJ4VUh4S1dXRHNBUkE9PSIsInZhbHVlIjoiWVp0WHVEK3hsKzlaNUNjTndxeHNINHpKTnlSOXBhQmFsQWhqdkh6OWFCZVNTQkNxcnZMSmZFdG1EeUNMOXltd0puQUdyOVJKbndORWZBWEtLdi82ai94aHU1RlJITUtFdGFTayt0dm55SGtsVzZqVjVHcy9nYXgwVVFHaG5odVgiLCJtYWMiOiIyMDc3NTE0NzgyZTM2OTYyZjY3MDYzMjVjZDM4YzhhMmEwNTMxNGViMzM4NjgxMGJhMjE1ZWYyOGMwZTEyNGVhIn0%3D',
    'XSRF-TOKEN': 'eyJpdiI6IlNiVzJ5VFhXajhOTkFKMWpKcUgwemc9PSIsInZhbHVlIjoiMk05eFVRVDJjdlhsSVY1cWFHdEJBSHRKc2huK0h2ODZ6RlJ6c3B5ZnRNVTdpSHFFVXRzWjBaZUtzcHZSWjhBb0xESHN0SlFqb25NTGxucnUxQ0I0cWFLenNmb2RueXhUK3NDOVhFWGtMQVBaUDd0RTk5NXQ3SDdOV2tjdS9vVTIiLCJtYWMiOiI5YTliYTE4ZGEzN2E1ODJmOTZlZjlmYWI2OTE3MGQxZTM4MWZiNDVkMWM1ZDIxZWUwMjE0YjQzNmYyZDFjNGJmIn0%3D',
    '_ga_37GXT4VGQK': 'GS1.1.1699994542.1.1.1699994698.0.0.0',
    '_clsk': '6ly9l8|1699994699818|3|1|j.clarity.ms/collect',
}

headers = {
    'authority': 'binaryclass.cademi.com.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'laravel_session=AdEsdDgOvLbkIT1zxo83OdyQZhhonP6dsVFrnnP4; _ga=GA1.1.1330075857.1699994543; _fbp=fb.2.1699994543339.690699131; _clck=i0wsxo|2|fgp|0|1413; cademi_auth_2831=eyJpdiI6Img0S3l3ekpxNGJ4VUh4S1dXRHNBUkE9PSIsInZhbHVlIjoiWVp0WHVEK3hsKzlaNUNjTndxeHNINHpKTnlSOXBhQmFsQWhqdkh6OWFCZVNTQkNxcnZMSmZFdG1EeUNMOXltd0puQUdyOVJKbndORWZBWEtLdi82ai94aHU1RlJITUtFdGFTayt0dm55SGtsVzZqVjVHcy9nYXgwVVFHaG5odVgiLCJtYWMiOiIyMDc3NTE0NzgyZTM2OTYyZjY3MDYzMjVjZDM4YzhhMmEwNTMxNGViMzM4NjgxMGJhMjE1ZWYyOGMwZTEyNGVhIn0%3D; XSRF-TOKEN=eyJpdiI6IlNiVzJ5VFhXajhOTkFKMWpKcUgwemc9PSIsInZhbHVlIjoiMk05eFVRVDJjdlhsSVY1cWFHdEJBSHRKc2huK0h2ODZ6RlJ6c3B5ZnRNVTdpSHFFVXRzWjBaZUtzcHZSWjhBb0xESHN0SlFqb25NTGxucnUxQ0I0cWFLenNmb2RueXhUK3NDOVhFWGtMQVBaUDd0RTk5NXQ3SDdOV2tjdS9vVTIiLCJtYWMiOiI5YTliYTE4ZGEzN2E1ODJmOTZlZjlmYWI2OTE3MGQxZTM4MWZiNDVkMWM1ZDIxZWUwMjE0YjQzNmYyZDFjNGJmIn0%3D; _ga_37GXT4VGQK=GS1.1.1699994542.1.1.1699994698.0.0.0; _clsk=6ly9l8|1699994699818|3|1|j.clarity.ms/collect',
    'referer': 'https://binaryclass.cademi.com.br/area/vitrine',
    'sec-ch-ua': '"Chromium";v="115", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

response = requests.get('https://binaryclass.cademi.com.br/area/produto/item/2078932', cookies=cookies, headers=headers)



soup = BeautifulSoup(response.content, 'html.parser')

all_module = soup.find_all('div', class_='section-group')


info_aulas = {
    "binary": []
}

for module in all_module:
    all_aulas = []
    module_title = module.find('div', class_='item-titulo').text
    module_title = module_title.split('\n')[1]

    aulas = module.find_all('a', class_='layer-link')

    for aula in aulas:
        aula_title = aula.find('div', class_='item-titulo').text
        aula_title = aula_title.split('\n')[1]
        aula_link = aula['href']
        all_aulas.append([aula_title, aula_link])

    info_aulas['binary'].append(dict(module_title=module_title, aulas=all_aulas))