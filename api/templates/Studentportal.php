<!DOCTYPE html>
<?php
session_start();
if(isset($_POST['sub']))
{
  header("Location:Login.php");
}
?>
<html>
<head>
  <meta charset="utf-8">
  <title>Student page</title>
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
      position: absolute;
      box-sizing: border-box;
      border-width: 1px;
      border-style: solid;
      left: 0%;
      height: 14.86%;
      width: 100%;
      border-image-source: none;
      border-image-width: 1;
      border-image-outset: 0;
      border-image-repeat: stretch;
      border-color: rgba(0, 0, 0, 0);
      top: 0%;
      background-image: none;
      background-color: rgb(189, 189, 189);
    }
    .gwd-img-kj77 {
      position: absolute;
      width: 20%;
      height: 12%;
      left: 1%;
      top: 1%;
    }
    .gwd-p-6368 {
      position: absolute;
      font-weight: normal;
      font-size: 30px;
      text-align: center;
      left: 28.4%;
      top: 2.81%;
      width: 45.58%;
      height: 7.83%;
      font-family: Lobster;
      font-style: normal;
      opacity: 0.8;
      background-image: none;
      background-color: transparent;
      overflow: visible;
      visibility: visible;
    }
    .gwd-img-te41 {
      position: absolute;
      left: 0%;
      width: 100%;
      height: 94.65%;
      opacity: 0.2;
      top: 5%;
    }
    .gwd-p-1i6n {
      font-family: Lobster;
    }
    .gwd-p-1wbh {
      font-family: Tahoma;
    }
    .gwd-p-tjr1 {
      font-weight: normal;
    }
    .gwd-p-d0hj {
      font-style: normal;
    }
    .gwd-li-1fd4 {
      font-style: italic;
    }
    .gwd-p-f3o9 {
      position: absolute;
      left: 88px;
      top: 112px;
      width: 18.02%;
      height: 5.82%;
    }
    .gwd-span-3x0i {
      font-size: 20px;
      font-style: italic;
      color: rgb(255, 255, 255);
    }
    .gwd-p-ty1l {
      left: 10.74%;
      top: 21.89%;
    }
    .gwd-img-1ivb {
      left: 0%;
      top: 5%;
    }
    .gwd-p-1s9b {
      top: 38%;
      left: 10%;
    }
    .gwd-p-1jpe {
      left: 11%;
      top: 40%;
    }
    .gwd-p-bqs7 {
      font-size: 20px;
      font-style: italic;
      top: 44%;
      left: 10%;
    }
    .gwd-p-1lix {
      font-size: 20px;
      font-style: italic;
      top: 50%;
      left: 10%;
    }
    .gwd-p-grue {
      font-size: 20px;
      font-style: italic;
      width: 21.48%;
      transform-origin: 89.9125px 14.4875px 0px;
      top: 56%;
      left: 10%;
    }
    .gwd-img-81n3 {
      left: 0%;
      top: 5%;
    }
    .gwd-button-1jw7 {
      position: absolute;
      border-image-source: none;
      border-image-width: 1;
      border-image-outset: 0;
      border-image-repeat: stretch;
      border-color: transparent;
      border-radius: 15px;
      height: 5.06%;
      top: 8.65%;
      width: 12.29%;
      left: 83.78%;
    }
    .gwd-p-1hjf {
      position: absolute;
      top: 9%;
      width: 11.3%;
      height: 4.52%;
      left: 75%;
      font-size: 20px;
    }
  </style>
  <link href="https://fonts.googleapis.com/css?family=Quicksand:300,regular,500,700|Lobster:regular" rel="stylesheet" type="text/css">
  <script type="text/javascript" gwd-events="handlers">
    window.gwd = window.gwd || {};
    gwd.click = function(event) { < a href = "www.google.com" > academics < /a>};
  </script>
</head>

<body class="htmlNoPages">
  <img src="stdent_bg.png" id="stdent_bg" class="gwd-img-te41 gwd-img-81n3" data-gwd-tl-locked="">
  <img src="stdent_bg.png" id="stdent_bg_1" class="gwd-img-te41 gwd-img-1ivb gwd-gen-16i3gwdanimation" data-gwd-tl-locked="">
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx" id="R1" data-gwd-tl-locked=""></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77" data-gwd-tl-locked="">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation" id="n1" data-gwd-tl-locked="">Student Portal</p>
  <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-bqs7" id="ele_2" data-gwd-tl-locked=""><a href="plife">Personal life</a>
  </p>
  <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-1jpe gwd-p-1lix" id="ele_1" data-gwd-tl-locked=""><a href="sav">Achievements</a>
  </p>
  <!-- <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-1jpe gwd-p-grue" id="ele_3" data-gwd-tl-locked=""><a href="http://www.google.com">College participation</a> -->
  <!-- </p> -->
  <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-1s9b" id="ele" data-gwd-tl-locked=""><span class="gwd-span-3x0i"><a href="acadmain ">Academics</a></span><br>
    
  </p>
  <form method="POST">
  <input type='Submit' id="button_1" class="gwd-button-1jw7" data-gwd-tl-locked="" name='sub' value='Logout'><a href="acadmain">Logout</br>
  <p class="gwd-p-1hjf" id="1" data-gwd-tl-locked=""></p>
</form>
</body>

</html>
