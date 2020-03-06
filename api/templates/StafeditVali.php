
<html>
<head>
 <title>Table with database</title>
 <style>
  table {
   border-collapse: collapse;
   width: 70%;
   color: #588c7e;
   font-family: monospace;
   font-size: 25px;
   text-align: left;
     } 
  th {
   background-color: #588c7e;
   color: white;
    }
  tr:nth-child(even) {background-color: #f2f2f2}
 </style>
</head>
<body>
 <table>
 <tr>
  <th>SID</th> 
  <th>Achievement</th> 
  <th>Validation</th>
 </tr>
 <?php
$conn = mysqli_connect("localhost", "root", "", "project1");
  // Check connection
  if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
  } 
  $sql = "SELECT * FROM achievements where Validity=1";
  $result = $conn->query($sql);
  if ($result->num_rows > 0) {
   // output data of each row
   $row = $result->fetch_assoc(); 
    echo "<form method='POST'><tr><td>" . $row["sid"]. "</td><td>" . $row["achieve"] . "</td><td><input type='Submit' value='Accept' name='sub1'></td><td><input type='Submit' value='Decline' name='sub'></td></tr></form>";
if(isset($_POST['sub']))
{
  $sql="DELETE FROM achievements where sid='".$row['sid']."' and Validity=1";
  $result = $conn->query($sql);
}
else if(isset($_POST['sub1']))
{
  $sql="UPDATE achievements set Validity=0 where sid='".$row['sid']."'";
  $result = $conn->query($sql);
}
echo "</table>";
}
$conn->close();
header('refresh:5');
?>
</table>
</body>
</html>