## check work later
import numpy as np

morning = np.array([1,2,3,4,5,6])
evening = np.array([7,8,9,10,11,12])
together = np.concatenate((morning, evening))
print("Here are the temps together: ", together)
meanBoth = np.mean(together)
print("Here's the mean of both:", meanBoth)
stdBoth = np.std(together)
print("Here's the STD of both: ", stdBoth)
print("Here's the total sum of both arrays: ", np.add(morning, evening))
print("Here's he meadian of both:", np.median(together))

print("Here's the mean of morning:", np.mean(morning))
print("Here's the STD of monring", np.std(morning))
print("Here's the median of morning", np.median(morning))
print("Here's the morning", np.sum(morning))

print("Here's the mean of evening:", np.mean(evening))
print("Here's the STD of evening", np.std(evening))
print("Here's the median of evening", np.median(evening))
print("Here's the evening", np.sum(evening))
