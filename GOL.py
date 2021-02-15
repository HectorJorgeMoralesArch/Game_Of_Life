import numpy as np
import random as rdm
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
        Grid[i:i+4,j:j+3]=Beehive
    elif Name=="Loaf":
        Grid[i:i+4,j:j+4]=Loaf
    elif Name=="Boat":
        Grid[i:i+3,j:j+3]=Boat
    elif Name=="Tub":
        Grid[i:i+3,j:j+3]=Tub
    #Add Oscilators
    elif Name=="BlinkerA":
        Grid[i,j:j+3]=BlinkerA
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
def main():
    Universe=np.array()
    Selection=int(input("Select the way to create the Universe.\n\t1) Random Universe No Defines Dimensions\n\t2) Random Universe With Dimensions\n\t3)Decide Own Size\n\t4) File Input (WIP)\n"))
    if Selection==1:
        Universe=RandomUniverse(rdm.randint(10,15))
    elif Selection==2:
        Universe=RandomUniverse(abs(int(input("Universe Size = "))))
    elif Selection==3:
        Universe=CreateUniverse(abs(int(input("Universe Size = "))))
    elif Selection==4:
        return
    grid = randomGrid(N)
    print(grid)
    return

if __name__ == '__main__':
    main()