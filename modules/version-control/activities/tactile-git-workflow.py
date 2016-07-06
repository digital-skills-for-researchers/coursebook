from random import randint

animals = ["cat","dog","bunny","moose"]
colours = ["red", "green", "blue", "yellow"]

working = []
staging = []
repo = []

# define the possible commands

def create():
  animal = animals[ randint(0, len(animals)-1) ]
  colour = colours[ randint(0, len(colours)-1) ]
  
  if animal not in repo && animal not in staging && animal not in working:
    print("create a", colour, animal)
    working.append([colour, animal])
    
  
  
def changeColour():
  animal = working[ randint(0, len(animals)-1) ]
  
  
def stageAll():
  
  if( len(working) == 0 ):
    return
  
  print("git stage -a")
  
  
  
def commit():
  
  if( len(staging) == 0 ):
    return
  
  print("git commit -m")
  

# define the commands available in each mode

easyCommands = [
  create,
  stageAll,
  commit
]
  

# define the game loop for each mode
def playEasy():
  
  for i in range(20):
    commandNumber = randint( 0, len(easyCommands)-1 )
    easyCommands[commandNumber]()
    
  printStatus()


def printStatus():
  
  print()
  print("working directory:")
  print(working)
  
  print()  
  print("git status:")
  print(staging)
  
  print()
  print("repo status:")
  print(repo)



mode = input("select mode")
playEasy()



  