import urllib.request

web_url = urllib.request.urlopen('https://geoffreywu.me/')

print(str(web_url.getcode()))

data = web_url.read()
data = str(data)

actual_output = ''

for i in range(len(data)-3):
    bool_track = False
    if data[i:i+3] == '<p>':
        bool_track = True
        i = i+3

    while bool_track == True:
        if data[i] == '<' and data[i+1] == '/' and data[i+2] == 'p':
            bool_track = False
            i = i + 4
        actual_output += data[i]
        i = i + 1

with open('output.txt','w') as f:
    f.write(actual_output)