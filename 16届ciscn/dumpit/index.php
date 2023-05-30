<?php

$host = "localhost";
$user = "www";
$pass = "123456";
$db = "ctf";
// ?op=query&db=ctf&table=flag1 or ?op=dump&db=ctf&table=flag1

if(isset($_GET['op'])){
    $op = $_GET['op'];
    switch($op){
        case "query":
            $con = mysqli_connect($host,$user,$pass,$db);
            $sql = "select * from ".$_GET['db'].".".$_GET['table'];
            // echo $sql;
            $result = mysqli_query($con,$sql);
            print_r(mysqli_fetch_assoc($result));
            break;
        case "dump":
            $filename = "log/".time().".txt";
            $ret = system("mariadb-dump -u$user -p$pass $_GET[db] $_GET[table] > ".$filename);
            echo "success <a href='$filename'>log</a>";
            break;
    }
}else{
    echo "?op=query&db=ctf&table=flag1 or ?op=dump&db=ctf&table=flag1";
}


?>