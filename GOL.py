import sys
import argparse
import numpy as np
import random as rdm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Still Lifes
Block=np.array([[255,255],[255,255]])
Beehive=np.array([[0,255,255,0],[255,0,0,255],[0,255,255,0]])
Loaf=np.array([[0,255,255,0],[255,0,0,255],[0,255,0,255],[0,0,255,0]])
Boat=np.array([[255,255,0],[255,0,255],[0,255,0]])
Tub=np.array([[0,255,0],[255,0,255],[0,255,0]])
#Oscilators
BlinkerA=np.array([[255],[255],[255]])
BlinkerB=np.array([[255,255,255]])
ToadA=np.array([[0,0,255,0],[255,0,0,255],[255,0,0,255],[0,255,0,0]])
ToadB=np.array([[0,255,255,255],[255,255,255,0]])
BeaconA=np.array([[255,255,0,0],[255,255,0,0],[0,0,255,255],[0,0,255,255]])
BeaconB=np.array([[255,255,0,0],[255,0,0,0],[0,0,0,255],[0,0,255,255]])
#Spaceships
GliderA=np.array([[0,255,0],[0,0,255],[255,255,255]])
GliderB=np.array([[255,0,255],[0,255,255],[0,255,0]])
GliderC=np.array([[0,0,255],[255,0,255],[0,255,255]])
GliderD=np.array([[255,0,0],[0,255,255],[255,255,0]])
LightWeightSpaceshipA=np.array([[255,0,0,255,0],[0,0,0,0,255],[255,0,0,0,255],[0,255,255,255,255]])
LightWeightSpaceshipB=np.array([[0,0,255,255,0],[255,255,0,255,255],[255,255,255,255,0],[0,255,255,0,0]])
LightWeightSpaceshipC=np.array([[0,255,255,255,255],[255,0,0,0,255],[0,0,0,0,255],[255,0,0,255,0]])
LightWeightSpaceshipD=np.array([[0,255,255,0,0],[255,255,255,255,0],[255,255,0,255,255],[0,0,255,255,0]])
#Adds the figure selected from above into the grid from the position I,J
def AddFigure(Name,i,j,Grid):
    #Add Still Lifes
    if Name=="Block":
        Grid[i:i+2,j:j+2]=Block
    elif Name=="Beehive":
        Grid[i:i+3,j:j+4]=Beehive
    elif Name=="Loaf":
        Grid[i:i+4,j:j+4]=Loaf
    elif Name=="Boat":
        Grid[i:i+3,j:j+3]=Boat
    elif Name=="Tub":
        Grid[i:i+3,j:j+3]=Tub
    #Add Oscilators
    elif Name=="BlinkerA":
        Grid[i:i+3,j:j+1]=BlinkerA
    elif Name=="BlinkerB":
        Grid[i:i+3,j]=BlinkerB
    elif Name=="ToadA":
        Grid[i:i+4,j:j+4]=ToadA
    elif Name=="ToadB":
        Grid[i:i+4,j:j+2]=ToadB
    elif Name=="BeaconA":
        Grid[i:i+4,j:j+4]=BeaconA
    elif Name=="BeaconB":
        Grid[i:i+4,j:j+4]=BeaconB
    #Add Spaceships
    elif Name=="GliderA":
        Grid[i:i+3,j:j+3]=GliderA
    elif Name=="GliderB":
        Grid[i:i+3,j:j+3]=GliderB
    elif Name=="GliderC":
        Grid[i:i+3,j:j+3]=GliderC
    elif Name=="GliderD":
        Grid[i:i+3,j:j+3]=GliderD
    elif Name=="LightWeightSpaceshipA":
        Grid[i:i+5,j:j+4]=LightWeightSpaceshipA
    elif Name=="LightWeightSpaceshipB":
        Grid[i:i+5,j:j+4]=LightWeightSpaceshipB
    elif Name=="LightWeightSpaceshipC":
        Grid[i:i+5,j:j+4]=LightWeightSpaceshipC
    elif Name=="LightWeightSpaceshipD":
        Grid[i:i+5,j:j+4]=LightWeightSpaceshipD
    else:
        print("Unabailable Figure")
    return Grid
#returns a grid of NxN random values
def CreateUniverse(N):
    return np.zeros(N*N).reshape(N,N)
#returns a grid of NxN random values
def randomGrid(N):
    return np.random.choice([0,255], N*N, p=[0.2, 0.8]).reshape(N, N)
#Checks how many Neighbours have
def Neighbors(I,J,grid):
    neighbors=0
    for i in range(I-1,I+2):
        for j in range(J-1,J+2):
            if i==I and j==J:
                continue
            elif i>len(grid) or j>len(Grid) or i<0 or j<0:
                continue
            elif Grid[i][j]!=0:
                neighbors-=-1
    return neighbours
#Changes the grid with the Rules
def NextGeneration(universe):
    nextUniverse=CreateUniverse(len(universe))
    for i in range(len(universe)):
        for j in range(len(universe)):
            if universe[i][j]==255:
                neighbors=Neighbors(i,j,universe)
                if neighbors==2 or neighbors==3:
                    nextUniverse[i][j]=255
            if universe[i][j]==0 and Neighbors(i,j,universe)==3:
                nextUniverse[i][j]=255
    return nextUniverse

def main():
    Universe=Generations=File=None
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life implementation.")
    parser.add_argument('-d', '--dimensions', type=int, required=True, help="Dimensions of the Universe N*N. Must be an INTEGER. Preferebly between 50 and 1000")
    parser.add_argument('-g', '--generations', type=int, required=True, help="Number of Generations. Must be an INTEGER.")
    parser.add_argument('-f', '--file', type=str, required=False, help="Name or path of the file with the Map to simulate.")
    if len(sys.argv) < 2:
        print("ERROR Arguments Missing.\nMUST be in ANY of this formats\npython conway.py -d <Dimensions> -g <Generations> -i <file>\npython conway.py -d <Dimensions> -g <Generations>")
        sys.exit()
    elif bool(parser.parse_args().dimensions) and bool(parser.parse_args().generations):
        if bool(parser.parse_args().file):
            Universe=CreateUniverse(abs(parser.parse_args().dimensions))
            Generations=abs(parser.parse_args().generations)
            File=parser.parse_args().file
            Universe=PopulateUniverseFile(File)
        else:
            Universe=randomUniverse(abs(parser.parse_args().dimensions))
            Generations=abs(parser.parse_args().generations)
            Universe=PopulateUniverse()
    else:
        print("ERROR")
        sys.exit()
    #StartSimulation(Universe)
    return

if __name__ == '__main__':
    main()