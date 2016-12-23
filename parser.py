import numpy as np
import matplotlib.pyplot as plt

train_loss = []
test_loss = []
norms = []
steps = []
with open('results.txt','r') as f:

	for line in f.readlines():
		if 'train_loss' in line:
			tokens = line.split(" ")
			step = tokens[1].split("/")[0]
			steps.append(step)
			loss = tokens[5]
			norm = tokens[9]
			train_loss.append(loss)
			norms.append(norm)
		elif 'test_loss' in line:
			tokens = line.split(" ")
			lloss = tokens[5]
			test_loss.append(loss)

x = np.arange(len(steps))
print(x)
plt.imshow(x,train_loss)
plt.savefig('train_loss.png')
# plt.plot(x,train_loss)
