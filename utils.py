from collections import Iterable


def batching(iterable: Iterable, batch_size: int = 1) -> Iterable:
  length = len(iterable)
  
  for ndx in range(0, length, batch_size):
    yield iterable[ndx:min(ndx + batch_size, length)]