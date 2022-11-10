import pyperclip

line=pyperclip.paste()
new_line=line.split('\r\n')

for i in range (len(new_line)):
    new_line[i]=('* '+new_line[i])
    bullet="\n".join(new_line)

pyperclip.copy(bullet)