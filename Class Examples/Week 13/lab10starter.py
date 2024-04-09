import re
"""
Lab 10 Starter
1. Find or create a directory for your project.
2. Download the dictionary to the directory.
3. Download first 200 lines of Alice In Wonderland to your directory.
4. Start a Python file for your project.
5. It is necessary to split apart the words in the story so that they may be checked individually. 
   It is also necessary to remove extra punctuation and white-space. Unfortunately, there is not 
   any good way of doing this with what the book has covered so far. The code to do this is short, 
   but a full explanation is beyond the scope of this class. Include the following function in your
   program. Remember, function definitions should go at the top of your program just after the imports. 
   We’ll call this function in a later step.
6. Read the file dictionary.txt into an array. Go back to Reading Into an Array for example code on how
   to do this. This does not have anything to do with the import command, libraries, or modules. Don’t 
   call the dictionary word_list or something generic because that will be confusing. Call it 
   dictionary_list or a different term that is specific.
7. Close the file.
8. Print --- Linear Search ---
9. Open the file AliceInWonderLand200.txt
10. We are not going to read the story into a list. Do not create a new list here like you did with 
    the dictionary.
11. Start a for loop to iterate through each line.
12. Call the split_line function to split apart the line of text in the story that was just read in. 
    Store the list that the function returns in a new variable named word_list. Remember, just calling 
    the function won’t do anything useful. You need to assign a variable equal (word_list) to the result. 
    If you’ve forgotten now to capture the return value from a function, see Capturing Returned Values.
13. Start a nested for loop to iterate through each word in the words list. This should be inside the 
    for loop that runs through each line in the file. (One loop for each line, another loop for each word 
    in the line.)
14. Using a linear search, check the current word against the words in the dictionary. See Linear Search 
    Algorithm for example code on how to do this. The linear search is just three lines long. When comparing 
    to the word to the other words in the dictionary, convert the word to uppercase. In your while loop just 
    use word.upper() instead of word for the key. This linear search will exist inside the for loop created 
    in the prior step. We are looping through each word in the dictionary, looking for the current word in 
    the line that we just read in.
15. If the word was not found, print the word. Don’t print anything if you do find the word, that would 
    just be annoying.
16. Close the file.
17. Make sure the program runs successfully before moving on to the next step.
18. Create a new variable that will track the line number that you are on. Print this line number along 
    with the misspelled from the prior step.
19. Make sure the program runs successfully before moving on to the next step.
20. Print --- Binary Search ---
21. The linear search takes quite a while to run. To temporarily disable it, it may be commented out 
    by using three quotes before and after that block of code. Ask if you are unsure how to do this.
22. Repeat the same pattern of code as before, but this time use a binary search. For the binary search, 
    go back to Binary Search. Much of the code from the linear search may be copied, and it is only necessary 
    to replace the lines of code that represent the linear search with the binary search.
23. Note the speed difference between the two searches.
24. Make sure the linear search is re-enabled, if it was disabled while working on the binary search.
25. Upload the final program or check in the final program.
"""
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("dictionary.txt")

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()
        words = split_line(line)
        for word in words:
            print(word)

main()