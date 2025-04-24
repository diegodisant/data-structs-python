import pstats
import cProfile
from functools import wraps

TOTAL_TIME_PROFILING = 'tottime'
CUMULATIME_TIME_PROFILING = 'cumtime'

def profile_test(test):
  @wraps(test)

  def wrapper(*args, **kwargs):
    profiler = cProfile.Profile()

    profiler.enable()

    result = test(*args, **kwargs)

    profiler.disable()

    test_name = test.__name__

    stats = pstats.Stats(profiler)

    stats.sort_stats(CUMULATIME_TIME_PROFILING)
    stats.dump_stats(f"./profiling/{test_name}.prof")

    return result

  return wrapper
