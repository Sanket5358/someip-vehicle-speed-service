"""
Simulates vehicle speed for the SOME/IP project.
"""

SPEED_PROFILE = [
    0, 20, 40, 60, 80, 100, 80, 60, 40, 20, 0
]


def get_speed_for_step(step: int) -> int:
    """Return the simulated speed for the current step."""
    return SPEED_PROFILE[step % len(SPEED_PROFILE)]
