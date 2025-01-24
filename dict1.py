mydict={
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "1",
    "Effect": "Allow",
    "Principal": {"AWS": ["arn:aws:iam::account-id:root"]},
    "Action": "s3:*",
    "Resource": [
      "arn:aws:s3:::amzn-s3-demo-bucket",
      "arn:aws:s3:::amzn-s3-demo-bucket/*"
    ]
  }]
}
print(mydict)
print(mydict["Statement"])
print(type(mydict["Statement"]))
print(mydict["Statement"][0])

print(mydict["Statement"][0]["Resource"])
print(mydict["Statement"][0]["Resource"][1])
