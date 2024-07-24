echo "-------------------------"
echo ""
echo "Initial Authorization Password:"
echo $(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)
echo ""
echo "-------------------------"
echo "jenkins_authorization="$(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)
echo ""
