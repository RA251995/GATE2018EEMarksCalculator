import re
import csv
import numpy as np

with open('response.txt', 'r') as content_file:
    content = content_file.read()
content = re.sub('(Not Answered)', '0', content)
content = re.sub('(Answered|Marked For Review)', '1', content)
matches = re.findall( r'Question ID : (\d{10})\n\nStatus : (\d)\n\n(?:Chosen Option|Given Answer) : (.+)\n', content)
with open('response.csv','w') as out:
    csv_out=csv.writer(out)
    for row in matches:
        csv_out.writerow(row)
		
response_arr = np.genfromtxt('response.csv', delimiter=',')
response_arr = response_arr[response_arr[:,0].argsort()]

key_arr = np.genfromtxt('key.csv', delimiter=',')

ans = response_arr[:,2]
min_ans = key_arr[:,1]
max_ans = key_arr[:,2]

correct_ans = (ans>=min_ans)&(ans<=max_ans)
pos_marks = sum(correct_ans*key_arr[:,3])
neg_marks = sum(np.invert(correct_ans)*response_arr[:,1]*key_arr[:,4])
print("Your marks is",pos_marks+neg_marks+2)
