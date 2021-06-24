from rpsmodel import *

if __name__ == "__main__":
    batches = 1000
    games = 1000
    results = []

    for bid in range(batches):
        result = []
        for gid in range(games):
            randomgame()
            result.append((bid, gid, getP1P(), getP2P()))
        results.append(result)
        reset()
