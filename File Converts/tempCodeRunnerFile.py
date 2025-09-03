import json

if __name__=='__main__':
    with open('input.json','r') as f:
       data=json.loads(f.read())
       output=",".join([*data[0]])
       for obj in data:
           output+=f'\n{obj['Name']},{obj['age']},{obj['birthyear']}'
    print(output)
      