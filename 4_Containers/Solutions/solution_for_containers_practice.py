### This file contains solutions for the file containers_practice.py

# 1. Create a `list` called `my_list` and store the values `3,20,"hello","goodbye"` within it.

		my_list = [3,20,"hello","goodbye"]
        
# 2. Print the list in reverse.

		print(my_list[-1::-1])

# 3. Add `4.3` to the list.

		my_list.append(4.3)
        
# 4. Remove `3` from the list.

		my_list.remove(3)
        
# 5. Create a dictionary called `week_dict` that stores the days of the week as keys and whether or not they are part of the weekend as values.

		week_dict = {"Monday":False,"Tuesday":False,"Wednesday":False,"Thursday":False,"Friday":False,"Saturday":True,"Sunday":True}
        
# 6. Collect all of the weekdays into a list.

		week_dict.keys()
        
# 7. Delete `Monday` from `week_dict`.

		del week_dict["Monday"]

