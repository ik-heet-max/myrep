import re
pattern = re.compile('(((www\.|https?:\/\/)|\.)\S{1,}($|(?=\s|\n)))|\S{1,}(?=@)\S{1,}')
string = "Please visit us at http://www.clickme.com or feel free to contact us by: blahblah@correo.mx, you're welcome!"
matches = pattern.findall(string)
match = [x[0] for x in matches]
print(pattern.sub('*', string))
