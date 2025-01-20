ssh-keyscan -t ECDSA @@{GitoliteVM.name}@@.@@{domain_name}@@

git ls-remote -h -- git@@@{GitoliteVM.name}@@.@@{domain_name}@@:@@{initial_project_name}@@.git