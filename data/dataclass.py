import os
import pickle

class Data:

    def __init__(self):
        if os.path.exists("data/data"):
            with open("data/data", "rb") as f:
                self.data, self.shape = pickle.load(f)
        else:
            self.data = {"objp": [], "imp": []}
            self.shape = None
    
    def save(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        with open("data/data", "wb") as f:
            pickle.dump((self.data, self.shape), f)
    
    def add(self, objp, imp, shape):
        if self.shape is None:
            self.shape = shape
        else:
            if self.shape != shape:
                raise Exception("shape mismatch")
        self.data["objp"].append(objp)
        self.data["imp"].append(imp)
        self.save()