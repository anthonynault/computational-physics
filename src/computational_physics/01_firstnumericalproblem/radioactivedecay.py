 
 # time step used in caluating differential decay
dt: float = 0.05

# the time at which to end the decay simulation
end_time: float = 5.0

# store results (time -> remaning nuclei)
data: dict[float, float] = {}

total_steps = end_time / dt

def radioactive_decay(nuclei: float, time: float = 0.0) -> dict[float, float]:
    """Radioactive decay calculation.

    Computes change in quantiy of nuclei over time as a result of radioactive decay.
    The current implementation uses the euler method and tail recursion.

    Args:
        nuclei: Initual quantity of nuclei. As fractions of nucli may not make sense
            this may be interpreted as a continuous mass distribution.
        time: the current time from which to compute the change in remaining nuclei.

    Returns:
        A map of time to remaning nucei.

    Example:
        >>> results = decay(nuceli=100.0)
        >>> results[1]
        >>> ???
    """
    data[time] = nuclei
    
    if (time >= end_time): return data
    else:
        remaining_nuclei = nuclei * (1 - dt)
        return radioactive_decay(remaining_nuclei, time + dt)
    

def main():   
    data = radioactive_decay(nuclei=100.0, time=0.0)
    
