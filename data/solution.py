import yaml

def save_solution(param):
    ret, mtx, dist, rvecs, tvecs = param
    all = {"ret": ret, "mtx": mtx.tolist(), "dist": dist.tolist()},
    with open("solution.yml", "w") as f:
        yaml.dump(all, f)