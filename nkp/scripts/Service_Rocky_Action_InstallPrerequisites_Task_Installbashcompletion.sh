#Install Bash Completion if not already installed
dnf install -y bash-completion

#Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

#Configure kubectl bash completion
source <(kubectl completion bash)

#Add autocomplete permanently to your bash shell.
echo "source <(kubectl completion bash)" >> ~/.bashrc

#Set up an alias so that instead of typing kubectl, we just type k
echo "alias k=kubectl" >> ~/.bashrc

#Setup bash completion for alias k
echo "complete -o default -F __start_kubectl k" >> ~/.bashrc

#Install Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

#Setup autocomplete in bash into the current shell
source <(helm completion bash) 
#Add autocomplete permanently to your bash shell.
echo "source <(helm completion bash)" >> ~/.bashrc
 
