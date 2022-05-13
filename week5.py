colors=['Red','Blue','Green','Yellow','Black']
states=['Andhra','Karnataka','Tamilnadu','Kerala']
neighbours={}
neighbours['Andhra']=['Karnataka','Tamilnadu']
neighbours['Karnataka']=['Andhra','Tamilnadu','Kerala']
neighbours['Tamilnadu']=['Andhra','Karnataka','Kerala']
neighbours['Kerala']=['Karnataka','Tamilnadu']
colors_of_states={}
def promising(state,color):
    for neighbour in neighbours.get(state):
        color_of_neighbour=colors_of_states.get(neighbour)
        if color_of_neighbour==color:
            return False
    return True
def get_color_for_state(state):             
    for color in colors:
        if promising(state,color):
            return color
def main():
    for state in states:
        colors_of_states[state]=get_color_for_state(state)
    print (colors_of_states)
main()                       
