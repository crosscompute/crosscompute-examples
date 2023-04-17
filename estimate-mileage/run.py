from datetime import datetime

# from matplotlib import pyplot as plt
from numpy import interp


rows = [
    (datetime(2021, 10, 16), 77107),
    (datetime(2022, 2, 12), 82176),
    (datetime(2022, 6, 9), 87267),
    (datetime(2022, 6, 20), 87617),
    (datetime(2022, 9, 15), 92544),
    (datetime(2022, 10, 26), 93945),
    (datetime(2023, 3, 2), 98638)]
xs = [_[0].timestamp() for _ in rows]
ys = [_[1] for _ in rows]


# plt.plot(xs, ys)
# plt.show()


datetimes = [
    datetime(2022, 1, 1),
    datetime(2022, 6, 30),
    datetime(2022, 7, 1),
    datetime(2022, 12, 31)]
ts = [_.timestamp() for _ in datetimes]
for t in ts:
    print(datetime.fromtimestamp(t), int(interp(t, xs, ys)))
