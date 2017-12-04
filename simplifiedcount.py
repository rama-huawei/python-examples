counts = dict()
names = ["rama", "dakshit", "saritha", "rama", "dakshit", "saritha", "huawei", "google", "amazon", "facebook", "microsoft"]
for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)
