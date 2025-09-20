# kubernetes handles the scaling of containerization
# control plane host the whole server, everything is connected to it
# node is the 
# minikube is a single node cluster in a VM

# kubectl apply -f pod.yaml

# replica sets and deployments: deployments can be used for rolling updates
# you create a deployment with a yaml file
# roll out: when you've made changes and want to push it
# roll back: when you have made changes that you want to revert back to what they were previously before the change

'''KUBERNETES COMMAND'''

# kubectl apply -f (pod name): will run the pod
# kubectl get pod (pod name) -o wide: can be used to confirm if a pod is running
# kubectl describe (pod name): will provide details on the the pod
# kubectl delete pod (pod name): this command will delete a pod
# kubectl get pods: this will provide details on all currently running pods

# HOW TO DELETE/SHUT DOWN AN ECHO(DEPLOYMENT): kubectl delete deployment echo
# HOW TO TEMPORARILY STOP A DEPLOYMENT(SCALING): kubectl scale deployment echo --replicas=0

#kubectl port-forward svc/echo 8080:80