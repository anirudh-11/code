<?php 
session_start();
 $connect =mysqli_connect("localhost","root","","project1");
 $row['a']="";
 if(!$connect)
 {
  echo mysqli_connect_error();
 }
 else
 {
 	$uname='COE17F02';
  $sql="SELECT * FROM achievements where sid='COE07F02'";
  $result = $connect->query($sql);
  if ($result->num_rows > 0) {
   // output data of each row
   while($row = $result->fetch_assoc())
    {
    echo $row['achieve'];
    echo '<br>';

	}
}
}


?>