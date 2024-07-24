decoded_private_key=$(echo "@@{private_key}@@" | base64 -d)
echo "decoded_private_key="$decoded_private_key
echo "original_private_key=@@{original_private_key}@@"