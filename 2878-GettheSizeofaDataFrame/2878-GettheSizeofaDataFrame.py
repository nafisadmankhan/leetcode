import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows, column = players.shape
    return [rows, column]