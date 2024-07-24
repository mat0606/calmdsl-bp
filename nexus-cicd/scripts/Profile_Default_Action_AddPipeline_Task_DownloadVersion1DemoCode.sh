echo "Get Demo Code"
cd @@{new_project_name}@@
wget @@{new_code_seed_location}@@/@@{new_code_seed}@@
tar xvfz @@{new_code_seed}@@
rm @@{new_code_seed}@@
