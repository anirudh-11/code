<?php
session_start();
if(isset($_POST['sub']))
  header("Location:Login.php");
?>
<html>

<head>
  <meta charset="utf-8">
  <title>Faculty portal</title>
  <meta name="generator" content="Google Web Designer 5.0.4.0226">
  <script type="text/javascript" src="https://gc.kis.v2.scr.kaspersky-labs.com/1A06D1F2-A129-144D-A5C7-0F753C9CACC6/main.js" charset="UTF-8"></script><style type="text/css" id="gwd-text-style">
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
      border-width: 1px;
      border-image-outset: 0;
      box-sizing: border-box;
      cursor: auto;
      display: block;
      position: absolute;
      width: 100%;
      height: 14.85%;
      left: 0%;
      top: 0%;
    }
    .gwd-img-kj77 {
      cursor: auto;
      display: block;
      position: absolute;
      width: 20.02%;
      height: 11.92%;
      left: 0.98%;
      top: 1.05%;
    }
    .gwd-p-6368 {
      cursor: auto;
      font-family: Lobster;
      font-size: 30px;
      opacity: 0.8;
      position: absolute;
      text-align: center;
      width: 45.54%;
      height: 7.74%;
      left: 28.45%;
      top: 2.93%;
    }
    .gwd-p-f3o9 {
      cursor: auto;
      font-size: 20px;
      font-style: italic;
      height: 5.82%;
      left: 10%;
      position: absolute;
      top: 44%;
      width: 18.02%;
    }
    .gwd-a-1y8a {
      font-size: 20px;
      font-style: italic;
    }
    .gwd-p-ty1l {
      cursor: auto;
      font-size: 20px;
      font-style: italic;
      height: 5.82%;
      left: 10%;
      position: absolute;
      top: 50%;
      width: 18.02%;
    }
    .gwd-a-1j6j {
      font-size: 20px;
      font-style: italic;
    }
    .gwd-p-1jpe {
      cursor: auto;
      font-size: 20px;
      font-style: italic;
      height: 5.82%;
      left: 10%;
      position: absolute;
      top: 56%;
      width: 21.48%;
      transform-origin: 89.9125px 14.4875px 0px;
    }
    .gwd-a-bjf5 {
      font-size: 20px;
      font-style: italic;
    }
    .gwd-p-trwc {
      width: 18.07%;
      height: 5.86%;
      left: 11%;
      top: 34%;
    }
    .gwd-p-mh8d {
      width: 21.49%;
      height: 5.86%;
      left: 11%;
      top: 50.84%;
    }
    .gwd-p-grjj {
      width: 21.49%;
      height: 5.86%;
      left: 10.99%;
      top: 42.47%;
    }
    .gwd-p-ikjp {
      left: 11%;
      top: 59.21%;
    }
    .gwd-img-7400 {
      position: absolute;
      width: 100%;
      height: 100.39%;
      opacity: 0.4;
      left: 0%;
      top: 15%;
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
  </style>
  <link href="https://fonts.googleapis.com/css?family=Lobster:regular" rel="stylesheet" type="text/css">
</head>

<body class="htmlNoPages">
  <img src="faculty-bg.jpg" id="faculty-bg" class="gwd-img-7400" data-gwd-tl-locked="">
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx" id="R1" data-gwd-tl-locked=""></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77" data-gwd-tl-locked="">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation" id="n1" data-gwd-tl-locked="">Faculty Portal</p>
  <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-bqs7 gwd-p-trwc" id="ele_2" data-gwd-tl-locked=""><a href="faculty_disp.php" class="gwd-a-1y8a">Personal life</a>
  </p>
  <!-- <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-1jpe gwd-p-1lix gwd-p-mh8d gwd-p-ikjp" id="ele_1" data-gwd-tl-locked=""><a href="http://www.google.com">Attendance</a> -->
  </p>
  <!-- <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-1jpe gwd-p-1lix gwd-p-mh8d" id="ele_4" data-gwd-tl-locked=""><a href="http://www.google.com">Qualifications</a> -->
  <!-- </p> -->
  <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-1jpe gwd-p-grue gwd-p-grjj" id="ele_3" data-gwd-tl-locked=""><a href="faculty_cou_view.php">Courses</a>
  </p>
  <form method="POST">
  <input type="Submit" id="button_1" class="gwd-button-1jw7" data-gwd-tl-locked="" name="sub" value="Logout"></br>
</form>
</body>

</html>