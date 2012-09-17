<html>
<head>
</head>

<body>
<?php

echo "this is atest";
echo "<p>";
//phpinfo();
$filename = '../password.txt';
if (move_uploaded_file($filename, "uploads/password.txt")) {
  echo "yay success";
} else {
  echo "did not work";
}

chmod($filename, 0644);
$combination = trim(file_get_contents($filename));
echo "<p>";
echo substr(sprintf('%o', fileperms('/tmp')), -4);
echo "<p>";
echo "the password is $combination";
?>
</body>
</html>
