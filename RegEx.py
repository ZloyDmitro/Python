#import re
#text = "The cost_of tomatoes is 23 \tdollars and the cost of potatoes is 12 dollars.\nSo total value in your basket amounts to 35 bucks."

##bracket notation
## [a-zA-Z]
## omits punctuation Underscore is not a punctuation symbol
# "\w"
## include punctuation
# "/S"
## boundry delimiter
# pattern = r"toes\b"
##metachars
# pattern = "." return all caracters except /n
# kleene star
# pattern = ".*" search all except new line
# text = "Über mogen"
# pattern = ".*"
# matches = re.findall(pattern, text)
# print(matches)

##RegEX
import re
re.findall
re.search
re.sub
re.split
re.compile

# text = "Out of the night that covers me, Black as the pit from pole to pole, I thank whatever gods may be For my unconquerable soul. In the fell clutch of circumstance I have not winced nor cried aloud. Under the bludgeonings of chance My head is bloody, but unbowed."

# pattern = re.findall("out",text, flags=re.IGNORECASE) #ignorecase give alls words with out despite capital letter.
# print(pattern) #return a list of matches
# pattern1 = re.search("out",text, flags=)
# #print(pattern1.span()) #shows only first one
# pattern2 = re.split("\.",text)
# #print(pattern2)
# sub_pattern = re.sub("\s","*",text)
# #print(sub_pattern)

#String Regex 1
# Task 1
# text = "Berlin is a world city of culture, politics, media and science."
# white_space = re.search("\s",text)
# print(f"The first white-space character is located at position: ", white_space.span())

# Task2
# text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
# findall = re.findall("Frankfurt", text)
# print(findall)
# Task3
# text = "Berlin-is-a-city-of-culture."
# replace = re.sub("\s", "-",text)
# print(replace)
# Task4
# text = "Berlin is a city of culture."
# search = re.search("in",text)
# print(search)
# Task5
# text = "Berlin is a city of culture."
# search = re.search(r"\bB",text)
# print(search.span())
# Task6
# text = "The rain in Spain."
# count = text.count("ai")
# print(count)
# #or
# matches = re.findall("ai", text)
# count = len(matches)
# print(count)



    # colou?r
    # --> color or colour
    #Answer: Here you can search by color or color in spite of being written.

    # (\W|^)[\w.-]{0,25}@(gmail|deliveryhero).com(\W|$)
    # (Filters Emails a match where the string DOES NOT contain any email which contain "-" ant the beginning, Characters
    # from 0 till 25 which are from gmail or deliveryhero end ends with .com
    # --> emails with TLD gmail.com or deliveryhero.com

    # ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$
    # --> PW
    # 6 to 12 characters in length
    # Must have at least one uppercase letter
    # Must have at least one lower case letter
    # Must have at least one digit
    # Should contain other characters
    #there are defaults for the password

    #^?([a-f0-9]{6}|[a-f0-9]{3})$
    # --> hex color code
    #

    # done$
    # --> a text that ends with "done"
    # search after a string that contain done at the end.



# remove leading and trailing zeros
##########
# input = "0023.07623070"
# parts = re.split(".",input)
# #parts = input.split(".")
# integer = str(int(parts[0]))
# if len(parts) > 1:
#     decimal = integer[1].rstrip("0")
#     result = f"{integer}.{decimal}" if decimal else integer
# else: 
#     result = integer

# print(result)
#########

# def remove_zeros(input):
#     parts = input.split(".")
input_str = input(f"Please provide a number:\n")
def remove_leading_trailing_zeros(input_str):
    # Split the string into its integer and fractional parts
    parts = input_str.split(".")
    # Handle the integer part (remove leading zeros)
    integer_part = str(int(parts[0]))
    # Handle the fractional part (remove trailing zeros)
    if len(parts) > 1:
        fractional_part = parts[1].rstrip("0")
        result = f"{integer_part}.{fractional_part}" if fractional_part else integer_part
    else:
        result = integer_part

    return result

output = remove_leading_trailing_zeros(input_str)
print(output)