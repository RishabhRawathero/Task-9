#!/usr/bin/python3
print("content-type:text/html")
print()

import cgi
f=cgi.FieldStorage()
string = f.getvalue("x")
import subprocess
if string == "delete all":
    o = subprocess.getoutput("kubectl delete all --all --kubeconfig admin.conf")
    print(o)


if string == "create pod with name love and image httpd":
    o = subprocess.getoutput("kubectl run love --image=httpd --kubeconfig admin.conf")
    print(o)

if string == "list the pod":
    o = subprocess.getoutput("kubectl get pods --kubeconfig admin.conf")
    print(o)
if string == "list the deployment":
    o = subprocess.getoutput("kubectl get deployments --kubeconfig admin.conf")
    print(o)
if string == "run deployment myweb":
    o = subprocess.getoutput("kubectl create deployment myweb --image=httpd --kubeconfig admin.conf")
    print(o)

if string == "expose myweb at port 80":
    o = subprocess.getoutput("kubectl expose deployment myweb --port=80 --type=NodePort --kubeconfig admin.conf")
    print(o)

if string == "create 5 replicas for myweb":
    o = subprocess.getoutput("kubectl scale deployment myweb --replicas=5 --kubeconfig admin.conf")
    print(o)
if string == "delete myweb":
    o = subprocess.getoutput("kubectl delete deployment myweb --kubeconfig admin.conf")
    print(o)




