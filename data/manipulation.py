from data.dataclass import Data

def supp():
    data = Data()
    data.data = {"objp": [], "imp": []}
    data.shape = None
    data.save()

def info():
    data = Data()
    print("shape:", data.shape)
    print("number of data:", len(data.data["objp"]))