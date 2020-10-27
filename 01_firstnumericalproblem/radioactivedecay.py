from dataclasses import dataclass


nuclei: list[float] = [100]
time: list[float] = [0]
data: dict[float, float] = {}
dt: float = 0.05

def decay(nuclei: float, time: float) -> dict[float, float]:
    if (time >= 5): return data
    else:
        data[time] = nuclei
        remaining_nuclei = nuclei - (nuclei * dt)
        return decay(remaining_nuclei, time + dt)
    
results = decay(nuclei=100, time=0.0)

for time, nuclei in results.items(): print(time, nuclei)