from datetime import datetime

# from matplotlib import pyplot as plt
from numpy import interp


rows = [
    (datetime(2020, 11, 15), 60646),
    (datetime(2021, 10, 16), 77107),
    (datetime(2022, 2, 12), 82176),
    (datetime(2022, 6, 9), 87267),
    (datetime(2022, 6, 20), 87617),
    (datetime(2022, 9, 15), 92544),
    (datetime(2022, 10, 26), 93945),
    (datetime(2023, 3, 2), 98638),
    (datetime(2023, 8, 15), 104435),
    (datetime(2024, 1, 27), 109685),
    (datetime(2024, 3, 27), 112211),
    (datetime(2024, 5, 21), 115158),
    (datetime(2024, 10, 5), 120688),
    (datetime(2024, 10, 11), 121046),
    (datetime(2024, 11, 30), 123079),
    (datetime(2025, 1, 29), 126248),
    (datetime(2025, 5, 10), 129887),
    (datetime(2025, 9, 24), 132082),
    (datetime(2026, 1, 12), 136215),
    (datetime(2026, 2, 2), 137130),
    (datetime(2026, 4, 12), 140566),
]
xs = [_[0].timestamp() for _ in rows]
ys = [_[1] for _ in rows]


# plt.plot(xs, ys)
# plt.show()


datetimes = [
    datetime(2022, 12, 31),
    datetime(2023, 12, 31),
    datetime(2024, 12, 31),
    datetime(2025, 12, 31),
    datetime(2026, 12, 31)]
ts = [_.timestamp() for _ in datetimes]
for t in ts:
    print(datetime.fromtimestamp(t), int(interp(t, xs, ys)))
