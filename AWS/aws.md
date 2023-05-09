# launch an instance

aws ec2 run-instances --key-name fla-may09  --image-id ami-09744628bed84e434 --instance-type t2.micro --subnet-id  subnet-060d9d8d8896b1e03 --security-group-ids <xxyy> --associate-public-ip-address

InstanceId": "i-0170f98ac07885469",

aws ec2 terminate-instances --instance-ids i-0170f98ac07885469