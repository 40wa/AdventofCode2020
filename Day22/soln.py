from collections import deque

def parse(data):
    a_deck = deque([int(data[i+1]) for i in range((len(data) // 2) - 2)])
    b_deck = deque([int(data[i+1+len(data)//2]) for i in range((len(data) // 2) - 2)])
    return (a_deck, b_deck)

# Modify decks in place
# 0 entails move made
# 1 entails game end
def step(a_deck, b_deck):
    if a_deck and b_deck:
        a,b = a_deck.popleft(),b_deck.popleft()
        if a > b:
            a_deck.extend((a,b))
        else:
            b_deck.extend((b,a))
        return 0
    else:
        return 1

def play(a_deck, b_deck):
    ret = step(a_deck, b_deck)
    while not ret:
        ret = step(a_deck, b_deck)

def score(decks):
    for i in range(len(decks)):
        if decks[i]:
            return sum((len(decks[i]) - idx)*d for idx,d in enumerate(decks[i]))

# 0 entails move made
# 1 entails player 1 win
# 2 entails player 2 win
def recstep(a_deck, b_deck):
    ret = 0
    seen = set()
    while not ret:
        if (tuple(a_deck),tuple(b_deck)) in seen:
            ret = 1
            break
        seen.add((tuple(a_deck), tuple(b_deck)))
    
        if a_deck and b_deck:
            a,b = a_deck.popleft(),b_deck.popleft()
            if (len(a_deck) >= a) and (len(b_deck) >= b):
                as_deck,bs_deck = a_deck.copy(),b_deck.copy()
                as_deck = deque([as_deck.popleft() for _ in range(a)])
                bs_deck = deque([bs_deck.popleft() for _ in range(b)])
                s_res = recstep(as_deck, bs_deck)
                if s_res == 1:
                    a_deck.extend((a,b))
                elif s_res == 2:
                    b_deck.extend((b,a))
            else:
                if a > b:
                    a_deck.extend((a,b))
                else:
                    b_deck.extend((b,a))
        else:
            ret = 1 * bool(a_deck) + 2 * bool(b_deck)
    return ret

    

def main():
    with open('data') as f: data = f.read().split('\n')

    decks = parse(data)
    print("Part One")
    play(*decks)
    print(score(decks)) 

    decks = parse(data)
    print("Part Two")
    recstep(*decks)
    print(score(decks))

if __name__=="__main__":
    main()
