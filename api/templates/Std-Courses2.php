<!DOCTYPE html>
<?php
if(isset($_POST['s']))
{
  header("Location:Login.php");
}?>
<html><head>  <style>
  table {
    position:absolute ;
   border-collapse: collapse;
   width: 80%;
   color: #588c7e;
   font-family: monospace;
   font-size: 25px;
   text-align: left;
   left: 13%;
   top: 30%;
     } 
  th {
   background-color: #588c7e;
   color: white;
    }
  tr:nth-child(even) {background-color: #f2f2f2}
 </style>
 	<meta name="GCD" content="YTk3ODQ3ZWZhN2I4NzZmMzBkNTEwYjJlcb4cfa700421a7740b640973f6970669"/>
  <meta charset="utf-8">
  <title>Courses</title>
  <meta name="generator" content="Google Web Designer 5.0.4.0226">
  <style type="text/css" id="gwd-text-style">p {
    margin: 0px;
}
h1 {
    margin: 0px;
}
h2 {
    margin: 0px;
}
h3 {
    margin: 0px;
}</style>
  <style type="text/css">html,
body {
    width: 100%;
    height: 100%;
    margin: 0px;
}
body {
    background-color: transparent;
    transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
    -webkit-transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
    -moz-transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
    perspective: 1400px;
    -webkit-perspective: 1400px;
    -moz-perspective: 1400px;
    transform-style: preserve-3d;
    -webkit-transform-style: preserve-3d;
    -moz-transform-style: preserve-3d;
}
.gwd-rect-13rx {
    background-color: rgb(189, 189, 189);
    border-color: rgba(0, 0, 0, 0);
    border-style: solid;
    border-width: 0.984375px;
    border-image-outset: 0;
    box-sizing: border-box;
    cursor: auto;
    display: block;
    height: 14.86%;
    left: 0%;
    position: absolute;
    top: 0%;
    width: 100%;
}
.gwd-img-kj77 {
    cursor: auto;
    display: block;
    height: 12%;
    left: 1%;
    position: absolute;
    top: 1%;
    width: 20%;
}
.gwd-p-6368 {
    cursor: auto;
    font-family: Lobster;
    font-size: 30px;
    height: 7.83%;
    left: 27%;
    opacity: 0.8;
    position: absolute;
    text-align: center;
    top: 3%;
    width: 45.58%;
}
.gwd-p-bifg {
    cursor: auto;
    font-family: Lobster;
    height: 0%;
    left: 12.63%;
    position: absolute;
    text-align: center;
    top: 19.03%;
    width: 0%;
    font-size: 22px;
}
.gwd-span-1psi {
    cursor: auto;
    font-family: Lobster;
    font-size: 22px;
    text-align: center;
}
.gwd-br-1xsd {
    cursor: auto;
    font-family: Lobster;
    font-size: 30px;
    text-align: center;
}
.gwd-p-3og6 {
    cursor: auto;
    font-family: Lobster;
    font-size: 30px;
    height: 52.01%;
    left: 13%;
    position: absolute;
    text-align: left;
    top: 30%;
    width: 70.88%;
    transform-origin: 0px 0px 0px;
    -webkit-transform-origin: 0px 0px 0px;
    -moz-transform-origin: 0px 0px 0px;
}
.gwd-br-1xuy {
    cursor: auto;
    font-family: Lobster;
    font-size: 30px;
    text-align: left;
}
.gwd-button-1jw7 {
    border-color: rgba(0, 0, 0, 0);
    border-radius: 15px;
    border-image-outset: 0;
    display: block;
    height: 5.06%;
    left: 83.78%;
    position: absolute;
    top: 8.65%;
    width: 12.29%;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
}
.gwd-p-1hjf {
    font-size: 20px;
    height: 4.52%;
    left: 70%;
    position: absolute;
    top: 9.12%;
    width: 20%;
    transform: matrix(0.999995, 0.00310886, -0.00310886, 0.999995, 0, 0);
    -webkit-transform: matrix(0.999995, 0.00310886, -0.00310886, 0.999995, 0, 0);
    -moz-transform: matrix(0.999995, 0.00310886, -0.00310886, 0.999995, 0, 0);
    transform-style: preserve-3d;
    -webkit-transform-style: preserve-3d;
    -moz-transform-style: preserve-3d;
}</style>
  <link href="https://fonts.googleapis.com/css?family=Lobster:regular" rel="stylesheet" type="text/css">
</head>

<body class="htmlNoPages">
  <table>
 <tr>
  <th>course id</th> 
  <th>course name</th> 
  <th>faculty id</th>
  <th>faculty name</th>
 </tr>
 <?php
 session_start();
$conn = mysqli_connect("localhost", "root", "", "project1");
  // Check connection
  if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
  } 
  $sql = "SELECT DISTINCT courses.cid as cid,courses.cname as cname,scf.fid as fid,faculty_info.name as fname FROM courses,scf,faculty_info  where sid='".$_SESSION['ID']."' and courses.cid=scf.cid and faculty_info.fid=scf.fid";
  $result = $conn->query($sql);
  if ($result->num_rows > 0) {
   // output data of each row
   while($row = $result->fetch_assoc()) {
    echo "<tr><td>" . $row["cid"]. "</td><td>" . $row["cname"] . "</td><td>".$row["fid"]."</td><td>" . $row["fname"]. "</td></tr>";
}
echo "</table>";
} else { echo "0 results";}
$conn->close();
?>
</table>
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx" id="R1"></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation" id="n1">Student Portal</p>
  <p class="gwd-p-bifg">Courses:</p>
  <p class="gwd-p-3og6"><br>
    
  </p>
  <form method='POST'>
  <input type='Submit' id="button_1" class="gwd-button-1jw7" value='Logout' name='s'><br>
  <p class="gwd-p-1hjf" id="1"><?php echo $_SESSION['ID'];?></p>
  </form>


</body></html>
