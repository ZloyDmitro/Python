# def pig_latin(*args, suffix="ay", single=False):
#     vowels = "aeiou"
#     result = []

#     for phrase in args:
#         for word in phrase.split(" "):
#             if word[0].lower() in vowels:
#                     new_word = word + suffix
#                     result.append(new_word)
#             else:
#                     new_word = word[1:].lower() + word[0].upper()+suffix
#                     result.append(new_word)
                
#     if single:
#         return (" ".join(result))
#     return (result)



# test1_data = ["Word", "Apple"]
# test1_config = {}

# test2_data = ["Python", "Functions"]
# test2_config = {"suffix": "oy"}

# test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
# test3_config = {"single": True, "suffix": "ey"}

# result1 = pig_latin(*test1_data, **test1_config)
# result2 = pig_latin(*test2_data, **test2_config)
# result3 = pig_latin(*test3_data, **test3_config)

# print(result1)
# print(result2)
# print(result3)
### Differenz klären
# def pig_latin(*wordsList, suffix='ay', single=False):
#     # set variables
#     result=[]
#     vowels = 'aeiou'
    
#     # break down the input to strings
#     for word in wordsList:
#         # print(word)
#         if word[0].lower() in vowels: 
            
#             pig_word=word+suffix
#             result.append(pig_word)
#         else: # if word does not start with a vowel
#             pig_word = word[1:]+word[0].upper()+suffix
#             result.append(pig_word)
        
#     if single: 
#         return ' '.join(result)
#     return result
            
            

# # test cases 
# test1_data = ["Word", "Apple"]
# test1_config = {}

# test2_data = ["Python", "Functions"]
# test2_config = {"suffix": "oy"}

# test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
# test3_config = {"single": True, "suffix": "ay"}

# print(pig_latin(*test1_data,**test1_config ))
# print(pig_latin(*test2_data, **test2_config))
# print(pig_latin(*test3_data, **test3_config))