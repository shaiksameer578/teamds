<?php
  $username = $_post['username'];
  $email = $_post['email'];
  $password = $_post['password'];
  $confirmpassword = $_post['confirmpassword'];

  $conn = new mysqli('localhost', 'root','', 'test');

if ($conn->connect_error) {

    die('Connection Failed : '.$conn->connect_error);

}else{

$stmt = $conn->prepare("insert into registration1 (username, email, , email, password, confirmpassword) values(?, ?, ?, ?, ?, ?)");

$stmt->bind_param("sssssi", $username, $email, $Password, $confirmpassword);

$stmt->execute();

echo "registration Successfully...";

$stmt->close();

$conn->close();
}
?>