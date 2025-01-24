import re

email_data="surendra  <surendrakorivi@gmail.com>, satya <satya@gmail.com>, Harish <Harish@gmail.com>"
result= re.search(r"surendra", email_data)
print(result)

result= re.search(r"surendra", email_data)
print(result)

result= re.findall(r"sure", email_data)
print(result)

result= re.search(r"sure[n,m]", email_data)
print(result)


result= re.search(r"sure[n,m,i]{2}", email_data)
print(result)

result= re.search(r"sure[a-z]", email_data)
print(result)

result= re.search(r"sure[a-z]{2}", email_data)
print(result)

result= re.search(r"sure[a-z]+", email_data)
print(result)

result= re.search(r"sure[a-z,A-Z,0-9]+", email_data)
print(result)

print("\nWith search function")
result= re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)

print("\nWith find function")
result= re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)

result= re.findall(r"sure[a-zA-z@.]+", email_data)
print(result)

result= re.search(r"sure[a-zA-z@.]+", email_data)
print(result)


result= re.search(r"\w+@\w+\.\w+", email_data)
print(result)

result= re.search(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
print(result[0])

result= re.findall(r"(\w+)@(\w+)\.(\w+)", email_data)
print(result)
print(result[0])
