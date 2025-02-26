<?php
session_start();
$admin_user = "admin";
$admin_pass = "admin123";
$mysqli = new mysqli("localhost", "root", "password","vulnerable_db");
function makeInsecureRequest($url)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1 );
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    $resonse = curl_exec($ch);
    curl_close($ch);
    return $resonse;
}
if($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $query ="SELECT * FROM users WHERE username ='$username' AND password = '$password'";
    $result =$mysqli->query($query);
    if($result-> num_rows > 0){
        $_SESSION["user"]= $username;
        echo"<script>alert('Login successful!');</script>";
    }
    else {
        echo "Invalid credentials";
    }
}
?>
<form method="POST" action="">
    Username:<input type="text" name="username"><br>
    Password:<input type="password" name="password"><br>
    <input type="submit" value="Login">
</from>
<?php if(isset($_SESSION["user"])):?>
    <p>Welcome,<?php echo $_SESSION["user"];?></p>
<?php endif;
?>    