## Matthew Chiappa
## Computer Hacking Revealed CSC 223
## 9/28/14

## Part 1
string = raw_input('Enter a string: ')
count = 0

for letter in string:
    if letter in "aeiou":
        count += 1

print 'Number of vowels:', count

## Part 2
string = raw_input('Enter a string: ')
count = 0

for i in range(len(string)):
    if string[i:i+3] == "bob":
        count += 1

print 'Number of times bob occurs:', count

## Part 3
string = raw_input('Enter a string: ')
start = 1
string2 = ''
real_string = ''

while start <= len(string) -1:

    if len(string2) < 1:
        string2 = string[start - 1] 

    if string[start - 1] <= string[start]:
        string2 += string[start]
        if len(string2) > len(real_string):
            real_string = string2
    else:
        string2 = ''

    start += 1

if real_string == '':
    real_string = string[0]

print 'Longest substring in alphabetical order is:', real_string