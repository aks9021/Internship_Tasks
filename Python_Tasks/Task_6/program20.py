#Validating phone numbers

#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
import re

n = int(input())

pattern = r'^[789]\d{9}$'

for _ in range(n):
    mobile = input().strip()
    if re.match(pattern, mobile):
        print("YES")
    else:
        print("NO")
