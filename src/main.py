import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    np.random.seed(123)
    print(np.random.rand())
    print(np.random.randint(1, 7))  # Generates a dice output 1 to 6

    # step = 50

    # Roll the dice
    # dice = np.random.randint(1, 7)

    # if dice <= 2:
    #     step = step - 1
    # elif 2 < dice <= 5:
    #     step = step + 1
    # else:
    #     step = step + np.random.randint(1, 7)
    #
    # # Print out dice and step
    # print(dice)
    # print(step)

    # NumPy is imported, seed is set

    # Initialize random_walk

    # random_walk = [0]
    # # Complete the ___
    # for x in range(100):
    #     # Set step: last element in random_walk
    #     step = random_walk[-1]
    #
    #     # Roll the dice
    #     dice = np.random.randint(1, 7)
    #
    #     # Determine next step
    #     if dice <= 2:
    #         step = max(0, step - 1)
    #     elif dice <= 5:
    #         step = step + 1
    #     else:
    #         step = step + np.random.randint(1, 7)
    #
    #     # append next_step to random_walk
    #     random_walk.append(step)
    #
    # # Print random_walk
    # plt.plot(random_walk)
    # plt.xlabel("dice throw")
    # plt.ylabel("steps")
    # plt.title("Random Walk")
    # plt.show()

# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
# all_walks = []
# for i in range(10) :
#     random_walk = [0]
#     for x in range(100) :
#         step = random_walk[-1]
#         dice = np.random.randint(1,7)
#         if dice <= 2:
#             step = max(0, step - 1)
#         elif dice <= 5:
#             step = step + 1
#         else:
#             step = step + np.random.randint(1,7)
#         random_walk.append(step)
#     all_walks.append(random_walk)
#
# # Convert all_walks to NumPy array: np_aw
# np_aw = np.array(all_walks)
#
# # Plot np_aw and show
# plt.plot(np_aw)
# plt.plot(random_walk)
# plt.xlabel("dice throw")
# plt.ylabel("steps")
# plt.title("Random Walk")
# plt.show()
# plt.show()
# # Clear the figure
# plt.clf()
#
# # Transpose np_aw: np_aw_t
#
# np_aw_t = np.transpose(np_aw)
# print(np_aw_t)
# # Plot np_aw_t and show
# plt.plot(np_aw_t)
# plt.show()


# numpy and matplotlib imported, seed set

# Simulate random walk 250 times
# all_walks = []
# for i in range(250) :
#     random_walk = [0]
#     for x in range(100) :
#         step = random_walk[-1]
#         dice = np.random.randint(1,7)
#         if dice <= 2:
#             step = max(0, step - 1)
#         elif dice <= 5:
#             step = step + 1
#         else:
#             step = step + np.random.randint(1,7)
#
#         # Implement clumsiness
#         if np.random.rand() <= 0.001 :
#             step = 0
#
#         random_walk.append(step)
#     all_walks.append(random_walk)
#
# # Create and plot np_aw_t
# np_aw_t = np.transpose(np.array(all_walks))
# plt.plot(np_aw_t)
# plt.show()

# numpy and matplotlib imported, seed set

# Simulate random walk 500 times and find how many times the user has possibility to reach 60 steps
all_walks = []
for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
