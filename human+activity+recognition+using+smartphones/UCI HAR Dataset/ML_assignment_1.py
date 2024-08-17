from MakeDataset import X_train,X_test,y_test,y_train
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# print(X_train)
# for i in range(5):
#     # plt.scatter(i,X_train[y_train == i, 0][0])
#     plt.scatter(X_train[y_train == i, 0], X_train[y_train == i, 1], label=f"Class {i}")
# a=X_train[y_train == 1, 0]
# b=X_train[y_train == 1, 1]
# print(a)
# print(b)
a = np.linspace(0, 10, 500, endpoint=False)
fig, ax = plt.subplots(6, figsize=(10, 12))

# Plot the waveforms
# ax[0].plot(a, X_train[y_train==1][0,:,0],color='r')
# ax[0].plot(a, X_train[y_train==1][0,:,1],color='g')
# ax[0].plot(a, X_train[y_train==1][0,:,2],color='b')
ax[0].plot(a, (X_train[y_train==1][0,:,:]**2).sum(axis=1),color='r')
ax[0].set_title('Walking')

# ax[1].plot(a, X_train[y_train==2][0,:,0],color='r')
# ax[1].plot(a, X_train[y_train==2][0,:,1],color='g')
# ax[1].plot(a, X_train[y_train==2][0,:,2],color='b')
ax[1].plot(a, (X_train[y_train==2][0,:,:]**2).sum(axis=1),color='r')
ax[1].set_title('Climbing up')

# ax[2].plot(a, X_train[y_train==3][0,:,0],color='r')
# ax[2].plot(a, X_train[y_train==3][0,:,1],color='g')
# ax[2].plot(a, X_train[y_train==3][0,:,2],color='b')
ax[2].plot(a, (X_train[y_train==3][0,:,:]**2).sum(axis=1),color='r')
ax[2].set_title('Climbing down')

# ax[3].plot(a, X_train[y_train==4][0,:,0],color='r')
# ax[3].plot(a, X_train[y_train==4][0,:,1],color='g')
# ax[3].plot(a, X_train[y_train==4][0,:,2],color='b')
ax[3].plot(a, (X_train[y_train==4][0,:,:]**2).sum(axis=1),color='r')
ax[3].set_title('sitting')

# ax[4].plot(a, X_train[y_train==5][0,:,0],color='r')
# ax[4].plot(a, X_train[y_train==5][0,:,1],color='g')
# ax[4].plot(a, X_train[y_train==5][0,:,2],color='b')
ax[4].plot(a, (X_train[y_train==5][0,:,:]**2).sum(axis=1),color='r')
ax[4].set_title('standing')

# ax[5].plot(a, X_train[y_train==1][0,:,0],color='r')
# ax[5].plot(a, X_train[y_train==1][0,:,1],color='g')
# ax[5].plot(a, X_train[y_train==1][0,:,2],color='b')
ax[5].plot(a, (X_train[y_train==6][0,:,:]**2).sum(axis=1),color='r')
ax[5].set_title('laying')

# Adjust layout and show the plot
# ax[0].plot(a, (X_train[y_train==1][0,:,:]**2).sum(axis=1),color='r')

plt.show()
