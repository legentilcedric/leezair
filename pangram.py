import string

def pangram_detector(s):

    # Split the text into lines
    list_of_lines = s.split('\n')

    # Get the number of sentences
    N = int(list_of_lines[0])

    # Creation of the list returned by this function
    output = []
    

    # For each sentence
    for line in list_of_lines[1:(N+1)]:
        
        # Remove the spaces
        t_line = line.replace(" ","")

        # Create a dictionary of each lowercase characters
        presence = dict.fromkeys(string.ascii_lowercase,0)

        # Actualize the precence dictionary for each character of the sentence
        for char in list(t_line):
            presence[char] = 1;

        # If all the characters are in the sentence, append '1' to the output
        if(sum(presence.values()) == 26):
            output.append('1')

        # Else, get all the missing characters and append them as a string to the output
        else:
            missing_char = ""
            for key, value in presence.items():
                if value != 1:
                    missing_char += key
            output.append(missing_char)

    return output


print(pangram_detector("4\nwe promptly judge antique ivory buckles for the next prize\nwe promptly judge antique ivory buckles for the prize\nthe quick brown fox jumps over the lazy dog\nthe quick brown fox jump over the lazi dog"))

