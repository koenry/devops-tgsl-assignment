## DevOps assingment
### API project usage:
```
git clone git@github.com:koenry/devops-tgsl-assignment.git
cd devops-tgsl-assignment/
docker build -t tgslapi .
docker run -dt --network=host --name tgslapi tgslapi

python3 test_api/main.py

output:
New order: <random uuid> created
pending
done
done
...
Exception: Error: 404
```

### Ansible project usage:
```
git clone git@github.com:koenry/devops-tgsl-assignment.git
cd devops-tgsl-assignment/
ansible-playbook ansible/tgsl.yaml --ask-become-pass
```


