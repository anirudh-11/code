<?php

if(isset($_POST['sub']))
{
  header('Location:Login.php');
}
if(isset($_POST['sub1']))
{
  $connect =mysqli_connect("localhost","root","","project1");
  $e='coe17b019';
 $row['a']="";
 $sql="SELECT COUNT(sid) as c FROM achievements where sid='".$e."' and Validity=1";
 $qry=mysqli_query($connect,$sql);
 $row = mysqli_fetch_array($qry);
if($row[0]>0)
   header("Location:StdAchPend.php");
 else
   header("Location:StdAch1.php");

  // header("Location:StudentPortal.html");
}?>
<html>

<head>
  <meta charset="utf-8">
  <title>A7</title>
  <meta name="generator" content="Google Web Designer 5.0.4.0226">
  <style type="text/css" id="gwd-text-style">
    p {
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
    }
  </style>
  <style type="text/css">
    html, body {
      width: 100%;
      height: 100%;
      margin: 0px;
    }
    body {
      background-color: transparent;
      transform: perspective(1400px) matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
      transform-style: preserve-3d;
    }
    .gwd-rect-13rx {
      background-color: rgb(189, 189, 189);
      border-color: rgba(0, 0, 0, 0);
      border-style: solid;
      border-width: 0.984375px;
      border-image-outset: 0;
      box-sizing: border-box;
      display: block;
      height: 14.86%;
      left: 0%;
      position: absolute;
      top: 0%;
      width: 100%;
    }
    .gwd-img-kj77 {
      display: block;
      height: 12%;
      left: 1%;
      position: absolute;
      top: 1%;
      width: 20%;
    }
    .gwd-p-6368 {
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
      position: absolute;
      font-family: Lobster;
      font-size: 30px;
      text-align: center;
      left: 12.63%;
      top: 19.03%;
      width: 0%;
      height: 0%;
    }
    .gwd-span-1psi {
      font-size: 22px;
    }
    .gwd-p-3og6 {
      position: absolute;
      font-family: Lobster;
      font-size: 30px;
      text-align: left;
      transform-origin: 0px 0px 0px;
      width: 70.88%;
      height: 52.01%;
      left: 13%;
      top: 30%;
    }
    .gwd-button-i7qd {
      position: absolute;
      transform-origin: 0px 0px 0px;
      left: 68.41%;
      top: 86.6%;
      width: 15.41%;
      height: 5.9%;
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
    }
    .gwd-p-1hjf {
      font-size: 20px;
      height: 4.52%;
      left: 70%;
      position: absolute;
      top: 9.12%;
      width: 20%;
      transform: matrix(0.999995, 0.00310886, -0.00310886, 0.999995, 0, 0);
      transform-style: preserve-3d;
    }
  </style>
  <link href="https://fonts.googleapis.com/css?family=Lobster:regular" rel="stylesheet" type="text/css">
</head>

<body class="htmlNoPages">
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx" id="R1"></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation text-tool-feedback" id="n1">Student Portal</p>
  <p class="gwd-p-bifg text-tool-feedback"><span class="gwd-span-1psi">Acheivements:</span><br>
    
  </p>
  <p class="gwd-p-3og6 text-tool-feedback">
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

  $sql="SELECT * FROM achievements where sid='".$_SESSION['ID']."' and Validity=0";
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


?><br>
    <form method="POST">
  </p>
  <input type="submit" id="button_1" class="gwd-button-i7qd text-tool-feedback" name='sub1' value="Edit"></br>
  <input type="submit" id="button_2" class="gwd-button-1jw7 text-tool-feedback" name='sub' value="Logout"></br>
  <p class="gwd-p-1hjf" id="1"><?php echo $_SESSION['ID'];?></p>
</form>
</body>
</html>