<?php 
 $connect =mysqli_connect("localhost","root","","project1");
 if(!$connect)
 {
  echo mysqli_connect_error();
 }
 else
 {
    if(isset($_POST['sub']))
    {
    $name=mysqli_real_escape_string($connect,$_POST['cid']);
       $sql2="DELETE from courses where cid='".$name."'";
       $qry2=mysqli_query($connect,$sql2);
       $sql4="DELETE from scf where scf.cid='".$name."'";
       $qry4=mysqli_query($connect,$sql4);
}
}
?>
<html>

<head>
  <meta charset="utf-8">
  <title>Staf-acad-Delcourse</title>
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
      left: 84%;
      position: absolute;
      top: 9%;
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
    .gwd-p-11p5 {
      font-size: 18px;
      height: 4.83%;
      left: 27%;
      position: absolute;
      top: 32.17%;
      width: 20.03%;
      transform-origin: 24.1796px 9px 0px;
    }
    .gwd-input-nfm1 {
      display: block;
      height: 2.95%;
      left: 38.52%;
      position: absolute;
      top: 40.21%;
      width: 15.41%;
      transform-origin: 38px 48px 0px;
    }
    .gwd-input-1klb {
      display: block;
      height: 2.95%;
      left: 38.52%;
      position: absolute;
      top: 32.17%;
      width: 15.41%;
      transform-origin: 38px 48px 0px;
    }
    .gwd-button-s2e7 {
      display: block;
      height: 5%;
      position: absolute;
      width: 10%;
      left: 39%;
      top: 45%;
    }
  </style>
  <link href="https://fonts.googleapis.com/css?family=Lobster:regular" rel="stylesheet" type="text/css">
</head>

<body class="htmlNoPages">
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx" id="R1" data-gwd-tl-locked=""></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77" data-gwd-tl-locked="">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation" id="n1" data-gwd-tl-locked="">Staff Portal</p>
  <p class="gwd-p-bifg" data-gwd-tl-locked=""><span class="gwd-span-1psi">Delete Course:</span><br>
    
  </p>
  </body>
  <form method="POST">
  <input type="Submit" name='sub1' id="button_1" class="gwd-button-1jw7" data-gwd-tl-locked="">Logout</button>
  <p class="gwd-p-1hjf" id="1" data-gwd-tl-locked="">Krish rewant</p>
  <p class="gwd-p-11p5" data-gwd-tl-locked="">CID:</p>
  <input type="text" id="text_5" class="gwd-input-nfm1 gwd-input-1klb gwd-input-19lk gwd-gen-3hg8gwdanimation gwd-input-13xv" data-gwd-tl-locked="" name='cid'>
  <input type="Submit" name='sub' id="button_2" class="gwd-button-s2e7" data-gwd-tl-locked="">Delete</button>
</form>
</body>

</html>