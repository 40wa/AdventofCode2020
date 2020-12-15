
# state is dictionary of all last spoken timesteps
def utter(lastnum, inputs, state, timestep):
    if timestep <= len(inputs):
        utterance = inputs[timestep-1]
        state[utterance] = [timestep,None]
    else:
        if state[lastnum][1]:
            utterance = timestep - 1 - state[lastnum][1]
        else:
            utterance = 0

        # Add the utterance
        if utterance in state.keys():
            state[utterance][1] = state[utterance][0]
            state[utterance][0] = timestep
        else:
            state[utterance] = [timestep, None]

    return utterance     

def main(ipt):
    print("live")

    inputs = ipt
    state = dict()
    timestep = 0
    
    print("Both Parts")
    u = 0
    for i in range(1,30000001):
        u = utter(u, inputs, state, i)
        if i % 1000 == 0:
            print(u)
    print(u)


if __name__=="__main__":
    main([3,1,2])
