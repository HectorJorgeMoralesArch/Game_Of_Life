import sys
import argparse
import numpy as np
import random as rdm
import matplotlib.pyplot as plt
import matplotlib.animation as ani
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
LightWeightSpaceShipA=np.array([[255,0,0,255,0],[0,0,0,0,255],[255,0,0,0,255],[0,255,255,255,255]])
LightWeightSpaceShipB=np.array([[0,0,255,255,0],[255,255,0,255,255],[255,255,255,255,0],[0,255,255,0,0]])
LightWeightSpaceShipC=np.array([[0,255,255,255,255],[255,0,0,0,255],[0,0,0,0,255],[255,0,0,255,0]])
LightWeightSpaceShipD=np.array([[0,255,255,0,0],[255,255,255,255,0],[255,255,0,255,255],[0,0,255,255,0]])
#Living Thing
Living=[BlinkerA,Beehive,Loaf,Boat,Tub,BlinkerA, BlinkerB,ToadA,ToadB,BeaconA,BeaconB,GliderA,GliderB,GliderC,GliderD,LightWeightSpaceShipA,LightWeightSpaceShipB,LightWeightSpaceShipC,LightWeightSpaceShipD]
#Visited Matrix that determines the values of life
visited=None
#Log
Log=""
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
        Grid[i:i+2,j:j+4]=ToadB
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
    elif Name=="LightWeightSpaceShipA":
        Grid[i:i+4,j:j+5]=LightWeightSpaceShipA
    elif Name=="LightWeightSpaceShipB":
        Grid[i:i+4,j:j+5]=LightWeightSpaceShipB
    elif Name=="LightWeightSpaceShipC":
        Grid[i:i+4,j:j+5]=LightWeightSpaceShipC
    elif Name=="LightWeightSpaceShipD":
        Grid[i:i+4,j:j+5]=LightWeightSpaceShipD
    else:
        print("Unabailable Figure")
    return Grid
#returns a grid of NxN randint values
def CreateUniverse(N):
    return np.zeros(N*N).reshape(N,N)
#returns a grid of NxN randint values
def randomUniverse(N):
    return np.random.choice([0,255], N*N, p=[0.2, 0.8]).reshape(N, N)
#Checks how many Neighbours have
def Neighbors(I,J,Grid,N):
    neighbors=0
    for i in range(I-1,I+2):
        for j in range(J-1,J+2):
            if i==I and j==J:
                continue
            elif i>=N or j>=N or i<0 or j<0:
                continue
            elif Grid[i][j]!=0:
                neighbors-=-1
    return neighbours
#Changes the grid with the Rules
def NextGeneration(universe,N):
    nextUniverse=CreateUniverse(N)
    for i in range(N):
        for j in range(N):
            if universe[i][j]==255:
                neighbors=Neighbors(i,j,universe,N)
                if neighbors==2 or neighbors==3:
                    nextUniverse[i][j]=255
            if universe[i][j]==0 and Neighbors(i,j,universe,N)==3:
                nextUniverse[i][j]=255
    return nextUniverse
#Populate the Universe with the file Input
def PopulateUniverseFile(Universe,File,N):
    f=open(FILE, 'r')
    for line in f.readlines:
        instruction=line.split(" ")
        if len(instruction)!=3:
            continue
        name,x,y=instruction[0],int(instruction[1]),int(instruction[2])
        if x<0 or x>=N-5 or y<0 or y>=N-5:
            continue
        Universe=AddFigure(name,x,y,Universe)
    return
#Populates the Universe with a range of 5% to 10% of the dimension of living patterns
def PopulateUniverse(Universe,N):
    for i in range(rdm.randint(int(N/20),int(N/10))):
        randint=rdm.randint(0,2)
        fig=name=None
        if randint==0:
            fig==rdm.randint(0,4)
            if fig==0:
                name="Block"
            elif fig==1:
                name="Beehive"
            elif fig==2:
                name="Loaf"
            elif fig==3:
                name="Boat"
            else:
                name="Tub"
        elif randint==1:
            fig=rdm.randint(0,5)
            if fig==0:
                name="BlinkerA"
            elif fig==1:
                name="BlinkerB"
            elif fig==2:
                name="ToadA"
            elif fig==3:
                name="ToadB"
            elif fig==4:
                name="BeaconA"
            else:
                name="BeaconB"
        else:
            fig=rdm.randint(0,7)
            if fig==0:
                name="GliderA"
            elif fig==1:
                name="GliderB"
            elif fig==2:
                name="GliderC"
            elif fig==3:
                name="GliderD"
            elif fig==4:
                name="LightWeightSpaceShipA"
            elif fig==5:
                name="LightWeightSpaceShipB"
            elif fig==6:
                name="LightWeightSpaceShipC"
            else:
                name="LightWeightSpaceShipD"
        Universe=AddFigure(name,rdm.randint(0,N-6),rdm.randint(0,N-6),Universe)
    return
#Checks for any form of life (Still Lifes, Oscilators, Spaceships)
def Life(Universe,N):
    Livingform=np.zeros(19)
    FormOfLive=0
    for i in range(N-6):
        for j in range(N-6):
            if Universe[i][j]==255 and visited[i][j]==False:
                for life in Living:
                    livingform=True
                    for i2 in range(len(life)):
                        for j2 in range(len(life[0])):
                            if Universe[i+i2][j+j2]==life[i2][j2]:
                                continue
                            livingform=False
                    if livingform:
                        for i2 in range(len(life)):
                            for j2 in range(len(life[0])):
                                visited[i+i2][j+j2]=True
                        Livingform[FormOfLive]-=-1
                FormOfLive=0
    Log+="Blocks = "+Livingform[0]+"\n"
    Log+="Beehive = "+Livingform[1]+"\n"
    Log+="Loaf = "+Livingform[2]+"\n"
    Log+="Boat = "+Livingform[3]+"\n"
    Log+="Tub = "+Livingform[4]+"\n"
    Log+="Blinker = "+str(int(Livingform[5]+Livingform[6]))+"\n"
    Log+="Toad = "+str(int(Livingform[7]+Livingform[8]))+"\n"
    Log+="Beacon = "+str(int(Livingform[9]+Livingform[10]))+"\n"
    Log+="Glider = "+str(int(Livingform[11]+Livingform[12]+Livingform[13]+Livingform[14]))+"\n"
    Log+="LightWeightSpaceShip = "+str(int(Livingform[15]+Livingform[16]+Livingform[17]+Livingform[18]))+"\n"
    return 
def CheckNeighbor(Universe,a,b,N):
    findOther=False
    for i in range(0,2):
        for j in range(0,2):
            if a-1+i<0 or b-1+j<0 or a-1+i>=N or b-1+j>=N:
                continue
            if Universe[a-1+i][-1+j]==255 and visited[a-1+i][-1+j]==False:
                findOther=True
                CheckNeighbor(Universe,a-1+i,b-1+j,N)
    return findOther
#Checks for any other form
def MaybeLife(Universe,N):
    OtherFormOfLive=0
    for i in range(N):
        for j in range(N):
            if Universe[i][j]==255 and visited[i][j]==False:
                if CheckNeighbor(Universe,i,j,N):
                    OtherFormOfLive-=-1
    Log+="Other Form Of Life = "+str(int(OtherFormOfLive))+"\n"
    return
#Update
def Update(Frame, img, Universe, ax,N):
    if Frame==0:
        sys.exit()
    Log+="メメメメメメメメ　　Generation "+str(int(Frame+1))+"　　メメメメメメメメ\n"
    Life(Universe,N)
    MaybeLife(Universe,N)
    Universe=NextGeneration(Universe,N)
    ax.set_title("Conway's Game of Life")
    img.set_data(Universe)
    img.set_cmap('binary')
    Frame-=1
    return img
#Starts The Simulation
def StartSimulation(Universe, Frames,N):
    NumFrames=Frames
    fig, ax = plt.subplots()
    ax.grid()
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, N - 1, 1))
    ax.set_yticks(np.arange(-.51, N - 1, 1))
    ax.set_xticklabels(np.arange(0, N, 1))
    ax.set_yticklabels(np.arange(0, N, 1))
    img = ax.imshow(Universe, interpolation='nearest')
    ax.set_title("Conway's Game of Life")
    img.set_cmap('binary')
    ani = animation.FuncAnimation(fig,Update,Frames,fargs=(NumFrames,img,Universe,ax,N))
    plt.show()
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
            Universe=PopulateUniverseFile(Universe,File,abs(parser.parse_args().dimensions))
        else:
            Universe=randomUniverse(abs(parser.parse_args().dimensions))
            Generations=abs(parser.parse_args().generations)
            Universe=PopulateUniverse(Universe,abs(parser.parse_args().dimensions))
    else:
        print("ERROR")
        sys.exit()
    visited=np.zeros(abs(parser.parse_args().dimensions)*abs(parser.parse_args().dimensions)).reshape([abs(parser.parse_args().dimensions),abs(parser.parse_args().dimensions)])
    StartSimulation(Universe,parser.parse_args().generations,abs(parser.parse_args().dimensions))
    text_file = open("report.txt", "w")
    n = text_file.write(Log)
    text_file.close()
    return

if __name__ == '__main__':
    main()