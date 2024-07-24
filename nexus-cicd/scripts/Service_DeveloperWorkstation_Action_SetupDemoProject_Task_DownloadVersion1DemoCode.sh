set -x
filename=@@{initial_code_seed}@@
url=@@{initial_code_seed_location}@@
url=$(echo ${url}|sed 's/\/$//')

echo "Get Demo Code"
cd @@{initial_project_name}@@
wget ${url}/${filename}
tar xvfz ${filename}
rm ${filename}
