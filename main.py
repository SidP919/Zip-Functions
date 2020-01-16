list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']
zipped = list(zip(list1,list2))
print(zipped)

unzipped = list( zip(*zipped))

print(unzipped)
print()
print()

for (list1_item, list2_item) in zip(list1,list2):
  print(list1_item)
  print(list2_item)

print()
print()

items = ['Apple','Banana','Orange']
counts = [3, 6, 4]
prices = [40, 10, 15]

sentences = []
for (item, count, price) in zip(items, counts, prices):
  sentences.append("I bought " + str(count) + " " +str(item) + " for " + str(price*count) + " Rupees.")

print(sentences)