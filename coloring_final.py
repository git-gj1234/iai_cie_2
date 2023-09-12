colors = ['Red','Blue', 'Green']
states = ['Telangana', 'Karnataka', 'Tamil Nadu', 'Kerala']
neighbours = {
    'Telangana': ['Karnataka', 'Tamil Nadu'],
    'Karnataka': ['Telangana', 'Tamil Nadu', 'Kerala'],
    'Tamil Nadu': ['Telangana', 'Karnataka', 'Kerala'],
    'Kerala': ['Karnataka', 'Tamil Nadu']
}

colours_of_states = {}

def promising(state, color):
    for neighbour in neighbours[state]:
        color_of_neighbour = colours_of_states.get(neighbour)
        if color_of_neighbour == color:
            return False
    return True

def get_state_color(state):
    for color in colors:
        if promising(state, color):
            return color
    return None  

def main():
    for state in states:
        color = get_state_color(state)
        if color is None:
            print("No solution found!")
            break  
        colours_of_states[state] = color
    
    if len(colours_of_states) == len(states):
        print(colours_of_states)

main()