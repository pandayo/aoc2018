Hello together, here I post my work on the advent of code. :D

### 1st Dec ###
It takes 143 complete iterations to get to a doubled value :)

### 2nd Dec ###
It took a while to understand, what the hash sum is supposed to be. You are not supposed to count every letter just once (maximizing the hash sum at 26^2 but instead only count every ID once for having two and once for having three letters occuring. D'oh.

### 3rd Dec ###
Solved it completly unoptimised. Hacked together a solution :/ It takes len(lines)^2 + len(lines) * id.x_length * id.y_lenght as it is not optimised. There is probably a solution using only a single loop, but i can't wrap my head around it using only lists, dicts, booleans, strings and integers. :(

### 4th Dec ###
Sad panda is sad. No solution today. I can't quite grasp the problem it seems.

### 5th Dec ###
Reading the assignment would help a lot in improving time to produce a solution. -.-

### 6th Dec ###
Took me forever to solve the first problem. Pretty sure I wasn't deciding whether a coordinate was infinite or not. Yet with the help of reddit, I got it working. And afterwards, getting Part II was like adding 7 lines of code and took like 2 minutes. I'm pretty happy about that :)

### 7th Dec ###
Reading the assignment would be helpful again. I was not checking all available tasks alphabetically but just the available ones in this task tree at first. Figured the solution out afterwards pretty quickly and the part II was fairly easy afterwards :)

### 8th Dec ###
This one was pretty easy and straight forward. :)

### 9th Dec ###
The first part was pretty straight forward, for the second part, the puzzle input was extremly large and my first solution would have taken probably about an hour to determine the solution. With the help of reddit, I updated to deque and it run super fast. :)

Short update: My naiive solution takes 2.5h to process 1.4 million marbles. It seems like this would be no good use for the handheld you took with you to save christmas :D

### 10th Dec ###
Was sick and also had no idea how to solve the problem.

### 11th Dec ###
Learned some numpy today :)

### 12th Dec ###
Puzzle was a type of Game of Life. The most confusing was I had to add the negative indices as well, which was not coming out of the instructions initially. Luckily, this time I'm not the only one having this problem :D
As usually since day 9, I had to get help with the approach to part II, solving it afterwards was pretty straight forward :)

### 13th Dec ###
I'm kinda sick, it's kinda late, but I took the last two hours to solve the first part of todays puzzle. I hate not being able to determine left from right -.-

### 14th Dec ###
Part I was pretty straight forward, Part II took me a while. Reddit helped again, my solution of using Strings was inefficent.

### 15th Dec ###
Whilst I got the right solution on the example input, I guess my a* runtime takes to long on the 30x30 grid of the puzzle input. How unforetunate, I thought that might be a fast algorithm :(

### 16th Dec ###
Fun little puzzle

### 18th Dec ###
Part II was obviously impossible to brute force, so I looked at the first 1000 Values and notices, that as of somewhere 700ish, values repeat. So I used to check in the range of 800:829 if a value is equal to 799, if so, it means it takes this long to go through a season, therefore, I can than calculate int((1000000000-800) / *length_of_season* % 1 x *length_of_season*). If I then add 800, I get an index of a product that is equal to the one 1000000000 has :)

### 19th Dec ###
Can't wrap my head around part II. I uploaded my input this time, as you have to reverse engineer it in part II.  

### 20th Dec ###
I tried to get all possible ways from the regex, which was quite complicated, so instead, i build a cartesian coordinate system with (0,0) being the startpoint and each step adding a door and a coordinate in the system. A dict with the coordinates as key and a list of doors as value then got sorted by the maximum value of the minimum of each list. :)
