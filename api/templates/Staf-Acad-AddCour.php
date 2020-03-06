<?php 
session_start();
 $connect =mysqli_connect("localhost","root","","project1");
 if(!$connect)
 {
  echo mysqli_connect_error();
 }
 else
 {
    if(isset($_POST['sub']))
    {
    $cid1=mysqli_real_escape_string($connect,$_POST['cid']);
    $cname1=mysqli_real_escape_string($connect,$_POST['cname']);
  $sql="INSERT INTO courses(cid,cname) VALUES('".$cid1."','".$cname1."')";
  $qry=mysqli_query($connect,$sql);
  }
  if(isset($_POST['sub1']))
  {
    header('Location:Login.php');
  }
}
?>
<html>

<head>
  <meta charset="utf-8">
  <title>Staf-Acad-AddCour</title>
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
      font-family: Lobster;
      font-size: 30px;
      height: 5%;
      left: 13%;
      position: absolute;
      text-align: left;
      top: 19%;
      width: 45%;
    }
    .gwd-span-1psi {
      font-family: Lobster;
      font-size: 22px;
      text-align: center;
    }
    .gwd-br-1576 {
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
      position: absolute;
      width: 12.29%;
      -webkit-appearance: none;
      left: 84%;
      top: 9%;
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
    .gwd-p-11p5 {
      font-size: 18px;
      height: 4.83%;
      position: absolute;
      width: 20.03%;
      transform-origin: 24.1796px 9px 0px;
      top: 32.17%;
      left: 27%;
    }
    .gwd-p-137k {
      font-size: 18px;
      height: 4.83%;
      position: absolute;
      width: 24.96%;
      transform-origin: 29.5698px 9px 0px;
      left: 27%;
      top: 40.21%;
    }
    .gwd-input-nfm1 {
      display: block;
      height: 2.95%;
      left: 40%;
      position: absolute;
      top: 48.26%;
      width: 15.41%;
      transform-origin: 38px 48px 0px;
    }
    .gwd-input-1klb {
      display: block;
      height: 2.95%;
      left: 40%;
      position: absolute;
      top: 52.82%;
      width: 15.41%;
      transform-origin: 38px 48px 0px;
    }
    .gwd-input-1t74 {
      left: 38.52%;
      top: 40.21%;
    }
    .gwd-input-13xv {
      left: 38.52%;
      top: 32.17%;
    }
    .gwd-button-s2e7 {
      position: absolute;
      left: 38.52%;
      top: 50.4%;
      height: 5%;
      width: 10%;
    }
  </style>
  <link href="https://fonts.googleapis.com/css?family=Lobster:regular" rel="stylesheet" type="text/css">
</head>

<body class="htmlNoPages">
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx" id="R1"></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation" id="n1">Staff Portal</p>
  <p class="gwd-p-bifg"><span class="gwd-span-1psi">Add Course:</span><br>
    
  </p>
  <form method='POST'>
  <input type='Submit' id="button_1" class="gwd-button-1jw7" value='Logout' name='sub1'><br>
  <p class="gwd-p-1hjf" id="1"><?php echo $_SESSION['ID'];?></p>
  <p class="gwd-p-11p5">CID:</p>
  <p class="gwd-p-137k">CNAME:</p>
  <input type="text" id="text_1" class="gwd-input-nfm1 gwd-input-1klb gwd-input-rum2 gwd-input-e7iq gwd-gen-1wdogwdanimation gwd-input-1t74" name='cname'>
  <input type="text" id="text_5" class="gwd-input-nfm1 gwd-input-1klb gwd-input-19lk gwd-gen-3hg8gwdanimation gwd-input-13xv" name='cid'>
  <input type='Submit' name='sub' id="button_2" class="gwd-button-s2e7">Add<br>
</form>
</body>

</html>