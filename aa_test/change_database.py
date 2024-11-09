azure_data = []
metadatafiles_data = []

extra = []
for a in azure_data:
    if a not in metadatafiles_data:
        extra.append(a)

print(extra)
print(len(extra))
