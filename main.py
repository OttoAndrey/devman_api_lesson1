import requests

offices = ['Лондон', 'Шереметьево', 'Череповец']
url_template = 'https://wttr.in/{}'
params = {'lang': 'ru',  # язык
          'm': '',  # метрические (СИ) (используются везде кроме США)
          'n': '',  # узкая версия (только день и ночь)
          'q': '',  # тихая версия (без текста "Прогноз погоды")
          'T': '',  # отключить терминальные последовательности (без цветов)
          }

for office in offices:
    url = url_template.format(office)
    response = requests.get(url, params=params)
    response.raise_for_status()

    print(response.text)
