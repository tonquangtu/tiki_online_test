This is repository for implement tiki interview online test in python3


Do follow steps to run it:
1. Create a input file with csv format and make its name is input.csv
2. Place input.csv file same dictionary with two .py file
3. Run file unique_phone_solution1.py or unique_phone_solution2.py via this command: python3 file_name and result will write into output1.csv or output2.csv file

<br>
<b>Explain my algorithm:</b><br>
I have 2 solution for this problem<br><br>
<b>Solution 1:</b>
I loop through all rows in input.csv file.
Each row, I check its activation and deactivation date is overlap with other tuple of activation and deactivation of current phone number in dictionary ?
If exist, it will combine each other.

For example:
with phone number is: <b>0987000004</b>, currently it have two item in list as a value of key <b>0987000004</b> in dictionary is
<b>[[2016-01-01, 2016-03-01], [2016-08-01, 2016-09-01]]</b><br>
current row is: 0987000004,2016-03-01,2016-04-01. <br>
 <b>--></b> Value of key <b>0987000004</b> is: <b>[[2016-01-01, 2016-04-01], [2016-08-01, 2016-09-01]]</b>
<br><br>
When loop done, the dictionary include list of unique (not overlap each other) activation and deactivation date of each phone number<br>
<b>--></b> Only need loop the dictionary and get maximum activation date in list of each phone number in dictionary


<br><br>
<b>Solution 2: </b>Easier than solution 1

<b>Step 1</b>: Loop through all rows in input.csv file and create a dictionary with phone number as key
and list of activation date and deactivation date as value<br>
<b>Step 2</b>: Sort list above by activation date<br>
<b>Step 3</b>: For each phone number, create a function to get real activation date from list of activation date and deactivation date of current phone number (value of key in dictionary)


    
   