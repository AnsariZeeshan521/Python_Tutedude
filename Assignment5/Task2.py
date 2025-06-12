original_list = [x for x in range(1,11)]

print(f"Original list: {original_list}")

extracted = original_list[:5]

print(f"Extracted first five elements: {extracted}")

extracted.reverse()
print(f"Reverse extracted elements: {extracted}")