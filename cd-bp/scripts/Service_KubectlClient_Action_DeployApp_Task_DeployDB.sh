export KUBECONFIG=/home/centos/@@{cluster_name}@@-kubectl.cfg
echo "Verify connection to the k8s cluster"
kubectl get nodes
echo "Generating deployment manifest"

kubectl -n default create secret generic mysql-pass --from-literal=password='@@{mysql_password.secret}@@'

rm db_deploy.yaml

echo "

apiVersion: v1
kind: Service
metadata:
  name: wordpress-mysql
  labels:
    app: wordpress
spec:
  ports:
    - port: 3306
  selector:
    app: wordpress
    tier: mysql
  clusterIP: None
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claimdemo
  labels:
    app: wordpress
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
---
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: wordpress-mysql
  labels:
    app: wordpress
spec:
  selector:
    matchLabels:
      app: wordpress
      tier: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
        tier: mysql
    spec:
      containers:
        #  Replace it as shown below: @@{docker_registry}@@:@@{docker_port}@@/@@{project_name}@@/mongodb:0.1.@@{build_number}@@
      - image: mysql:@@{build_number}@@
        name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-persistent-storage
        persistentVolumeClaim:
          claimName: mysql-pv-claimdemo
" > db_deploy.yaml

echo "Applying the manifest to k8s cluster"

kubectl apply -f db_deploy.yaml
