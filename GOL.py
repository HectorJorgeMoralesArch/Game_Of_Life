import numpy as np
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
#returns a grid of NxN random values
def CreateUniverse(N):
    return np.zeros(N*N).reshape(N,N)

def main():
    universe=CreateUniverse(int(input("Universe Size = ")))
    return
main()