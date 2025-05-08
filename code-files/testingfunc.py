'''
* Prologue
Created By: Ginny Ke
Date Created: 5/7/2025
Last Revised By: Jenna - added accept function to recognize string & reject otherwise
Date Revised: 5/8/2025
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
        for symbol in alphabet:
            transitions[state][symbol] = [] #initialize empty list for each symbol
    
    for line in lines[4:]:
        parts = line.split()
        if len(parts) == 3:
            start, element, destination = parts #stores 1st as the start, 2nd as the element, and 3rd as the destination
            if element in alphabet: #verify symbol in alphabet
                transitions[start][element].append(destination)
    
    return {
        "states": set(states),
        "alphabet": set(alphabet),
        "start_state": start_state,
        "accept_states": set(accept_states),
        "transitions": transitions
    }

def accept(A, w):
    #start with initial path (empty transitions, starting state)
    active_paths = [{
        'states': {A['start_state']},
        'transitions': []
    }]
    
    for char in w:
        new_paths = [] #keep track of the different paths to take
        
        for path in active_paths:
            # iterate over all current states
            for state in path['states']:
                #check if current character has transitions from current state
                if char in A['transitions'].get(state, {}):
                    #create new path for each transition
                    #if a state has multiple transitions for a character it will create a new path for each option to choose the path best fit
                    for next_state in A['transitions'][state][char]:
                        #copy exisiting transition and append the new transition
                        new_transitions = path['transitions'].copy()
                        new_transitions.append(f"{state} {char} {next_state}")
                        #create new path w/ updated state & transitions
                        new_paths.append({
                            'states': {next_state},
                            'transitions': new_transitions
                        })
        
        #if there are no valid transitions, reject
        if not new_paths:
            return "reject"
        active_paths = new_paths #update list of active paths to only successful transitions
    
    #check all completed paths
    accepting_paths = [] #stores all paths that reach an accept state
    #iterate through all valid paths and if the path's current state intersects with accept states then append to accepting paths
    for path in active_paths:
        if path['states'] & A['accept_states']:
            accepting_paths.append("\n".join(path['transitions']))
    
    #if accepting paths isn't empty, return accept with valid paths, else reject
    if accepting_paths:
        return "accept\n" + "\n".join(accepting_paths)
    else:
        return "reject"


if __name__ == "__main__": # helped function that brings in the txt file and asks user for a string input
    data = open_data("gymlanguage.txt")

    user_input = input("Enter workout string (e.g., 'splrspl'): ")
    result = accept(data, user_input)
    print(result)
