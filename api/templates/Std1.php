<?php
if(isset('sub'))
  header("Location:Login.php");
?>
<html>

<head>
  <meta charset="utf-8">
  <title>Std-Acheivements-Edit</title>
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
      height: 0%;
      position: absolute;
      text-align: center;
      width: 0%;
      left: 13%;
      top: 19%;
    }
    .gwd-span-1psi {
      font-family: Lobster;
      font-size: 22px;
      text-align: center;
    }
    .gwd-br-56st {
      font-family: Lobster;
      font-size: 30px;
      text-align: center;
    }
    .gwd-h2-j5pc {
      position: absolute;
      text-align: center;
      font-weight: normal;
      font-family: Arial;
      height: 14.75%;
      width: 50%;
      left: 27%;
      top: 40%;
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
  <img src="assets/logo.png" id="logo" class="gwd-img-kj77">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation" id="n1">Student Portal</p>
  <p class="gwd-p-bifg"><span class="gwd-span-1psi">Acheivements:</span><br>
    
  </p>
  <form method='POST'>
  <h2 class="gwd-h2-j5pc">SUCCESS!!<br>SENT FOR VALIDATION<br><br></h2>
  <input type='Submit' id="button_1" class="gwd-button-1jw7 text-tool-feedback" name='sub' value='Logout'><br>
  <p class="gwd-p-1hjf" id="1"><?php echo $_SESSION['ID'];?></p>
</form>
</body>

</html>