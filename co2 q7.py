import time
def build_sms(n):
    parts = []
    for i in range(n):
        parts.append(f"Item{i}: Rs. 50\n")
    result = "".join(parts)
    return result
start = time.perf_counter()
sms = build_sms(200000)
end = time.perf_counter()
print("Total characters:", len(sms))
print("Execution time:", end - start, "seconds")
