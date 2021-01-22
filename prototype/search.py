from magic_google import MagicGoogle
import pprint
import sys
import os

def pretty(result):
  title = result['title']
  url = result['url']
  text = result['text']
  description = text.split('\n')[2][:80]

  return f'- [{title}]({url}): {description}'

def markdown(keyword, results):
  f = open("result.md", 'w')
  f.write(f'# {keyword}\n\n')
  print(f'# {keyword}')
  for x in results:
    f.write(f'{x}\n')
    print(x)
  f.close()

def search(keyword):

  print('\n-------     Search     -------\n')

  mg = MagicGoogle()

  raw = mg.search(query=keyword, language='en', num=5)

  filtered = []

  for x in raw:
    if (x['title'] != ''):
      filtered.append(x)

  print('\n-------     Result     -------\n')

  results = []

  for result in filtered:
    results.append(pretty(result))

  markdown(keyword, results)

  print()

if __name__ == "__main__":
  search(sys.argv[1])
