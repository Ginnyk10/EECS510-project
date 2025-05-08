'''
* Prologue
Created By: Ginny Ke
Date Created: 5/7/2025
Last Revised By: Ginny - added helper function to read gymlanguage.txt file
Date Revised: 5/7/2025
Purpose: testing function for our Gym Language 
Input: gymlanguage.txt file and user input of a string
Output: accept and the accepting path or reject 
'''

def open_data(filename):
    with open(filename, 'r') as file: #open file in read mode only
        lines = [line.strip() for line in file if not line.strip().startswith("#") and line.strip()] #parses through each line, strips, and ignores lines that begin with #

    states = lines[0].split() #stores line 1 as the states as defined by the txt file
    alphabet = lines[1].split() # stroes line 2 as the elements of the alphabet 
    start_state = lines[2] #stores line 3 as the state state
    accept_states = lines[3].split() #stores line 4 as the accept state
    
    transitions = {} # stores lines 5-18 as the transitions
    for state in states:
        transitions[state] = {}
    
    for line in lines[4:]:
        start, element, destination = line.split() #stores 1st as the start, 2nd as the element, and 3rd as the destination
        if element not in transitions[start]:
            transitions[state][element] = []
        transitions[start][element].append(destination)
    
    return {
        "states": set(states),
        "alphabet": set(alphabet),
        "start_state": start_state,
        "accept_states": set(accept_states),
        "transitions": transitions
    }

if __name__ == "__main__": # helped function that brings in the txt file and asks user for a string input
    data = open_data("gymlanguage.txt")

    user_input = input("Enter workout string (e.g., 'splrspl'): ")

