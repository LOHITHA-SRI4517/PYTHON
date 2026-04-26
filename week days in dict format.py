#WEEK DAY IN DICT FORMAT
day=int(input("Enter day number:"))
switch={
    1:"Monday",
    2:"Tueday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"}
print(switch.get(day,"Invalid day"))
