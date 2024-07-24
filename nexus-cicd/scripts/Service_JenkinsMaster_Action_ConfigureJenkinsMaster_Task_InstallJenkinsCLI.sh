echo "Install Jenkins CLI"

while true ; do
  sudo wget http://@@{address}@@:8080/jnlpJars/jenkins-cli.jar
  if [ $? -eq 0 ]; then
    break
  else
    sleep 60
  fi
done

