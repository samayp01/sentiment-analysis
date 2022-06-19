import base64
import os

# take an input string and encode it in base64
def encode(string):
  return base64.b64encode(string.encode()).decode()


CMD = 'aws sagemaker-runtime invoke-endpoint --endpoint-name market-insights-bestmodel --body '
FMT = ' --content-type text/csv result.txt'

str = ''

# while user doesnt type in quit, run the encode function
while str != 'quit':
  str = input('> ')

  encoded_str = encode(str)
  print(encoded_str)

  to_shell = CMD + encoded_str + FMT
  os.system(to_shell)

  # open file "result" and print the contents
  raw_output = ''
  with open('result.txt', 'r') as f:
    raw_output = f.read().split("}",1)[1].strip()
    f.close()
  
  print("Positive") if raw_output == '-1' else print("Negative")
  









# aws sagemaker-runtime invoke-endpoint --endpoint-name market-insights-bestmodel --body <> --content-type text/csv f