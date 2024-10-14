from utils.ext_int import ext_num
from utils.date_format import date_formatter

s = "34gghhd6uu888"
print(ext_num(s)) 

date1 ="2024-10-14"
date2 ="10-15-2024"
date3 ="2024/10/14"

print(date_formatter(date1))  
print(date_formatter(date2))  
print(date_formatter(date3)) 