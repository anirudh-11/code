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
  <title>Admin Staff</title>
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
      width: 100%;
      border-image-source: none;
      border-image-width: 1;
      border-image-outset: 0;
      border-image-repeat: stretch;
      border-color: rgba(0, 0, 0, 0);
      top: 0%;
      background-image: none;
      background-color: rgb(189, 189, 189);
      height: 14.86%;
      opacity: 0;
    }
    .gwd-img-kj77 {
      position: absolute;
      width: 20%;
      height: 12%;
      left: 1%;
      top: 1%;
      opacity: 0;
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
      background-image: none;
      background-color: transparent;
      overflow: visible;
      visibility: visible;
      opacity: 0;
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
    .gwd-p-1s9b {
      font-size: 20px;
      font-style: italic;
      height: 5.82%;
      left: 10%;
      top: 38%;
      opacity: 0;
    }
    .gwd-p-bqs7 {
      font-size: 20px;
      font-style: italic;
      left: 10%;
      top: 63.29%;
      opacity: 0;
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
      opacity: 0;
    }
    .gwd-p-1hjf {
      position: absolute;
      top: 9%;
      width: 11.3%;
      height: 4.52%;
      left: 75%;
      font-size: 20px;
      opacity: 0;
    }
    .gwd-img-1qtk {
      position: absolute;
      left: 0%;
      width: 100%;
      height: 85%;
      top: 15.22%;
      opacity: 0;
    }
    @keyframes gwd-gen-fzeigwdanimation_gwd-keyframes {
      0% {
        opacity: 0;
        transform: translate3d(0px, 0px, 0px);
        animation-timing-function: linear;
      }
      50% {
        opacity: 0;
        transform: translate3d(0px, 0px, 0px);
        animation-timing-function: linear;
      }
      100% {
        opacity: 0.2;
        transform: translate3d(0px, -5px, 0px);
        animation-timing-function: linear;
      }
    }
    .htmlNoPages .gwd-gen-fzeigwdanimation {
      animation: gwd-gen-fzeigwdanimation_gwd-keyframes 1s linear 0s 1 normal forwards running;
    }
    @keyframes gwd-gen-1lqdgwdanimation_gwd-keyframes {
      0% {
        opacity: 0;
        animation-timing-function: linear;
      }
      50% {
        opacity: 0;
        animation-timing-function: linear;
      }
      100% {
        opacity: 1;
        animation-timing-function: linear;
      }
    }
    .htmlNoPages .gwd-gen-1lqdgwdanimation {
      animation: gwd-gen-1lqdgwdanimation_gwd-keyframes 1s linear 0s 1 normal forwards running;
    }
    @keyframes gwd-gen-kctogwdanimation_gwd-keyframes {
      0% {
        opacity: 0;
        animation-timing-function: linear;
      }
      50% {
        opacity: 0;
        animation-timing-function: linear;
      }
      100% {
        opacity: 1;
        animation-timing-function: linear;
      }
    }
    .htmlNoPages .gwd-gen-kctogwdanimation {
      animation: gwd-gen-kctogwdanimation_gwd-keyframes 1s linear 0s 1 normal forwards running;
    }
    @keyframes gwd-gen-19c4gwdanimation_gwd-keyframes {
      0% {
        opacity: 0;
        animation-timing-function: linear;
      }
      50% {
        opacity: 0;
        animation-timing-function: linear;
      }
      100% {
        opacity: 1;
        animation-timing-function: linear;
      }
    }
    .htmlNoPages .gwd-gen-19c4gwdanimation {
      animation: gwd-gen-19c4gwdanimation_gwd-keyframes 1s linear 0s 1 normal forwards running;
    }
    @keyframes gwd-gen-16slgwdanimation_gwd-keyframes {
      0% {
        opacity: 0;
        animation-timing-function: linear;
      }
      50% {
        opacity: 0;
        animation-timing-function: linear;
      }
      100% {
        opacity: 1;
        animation-timing-function: linear;
      }
    }
    .htmlNoPages .gwd-gen-16slgwdanimation {
      animation: gwd-gen-16slgwdanimation_gwd-keyframes 1s linear 0s 1 normal forwards running;
    }
    @keyframes gwd-gen-i37vgwdanimation_gwd-keyframes {
      0% {
        opacity: 0;
        animation-timing-function: linear;
      }
      50% {
        opacity: 0;
        animation-timing-function: linear;
      }
      100% {
        opacity: 1;
        animation-timing-function: linear;
      }
    }
    .htmlNoPages .gwd-gen-i37vgwdanimation {
      animation: gwd-gen-i37vgwdanimation_gwd-keyframes 1s linear 0s 1 normal forwards running;
    }
    @keyframes gwd-gen-18xbgwdanimation_gwd-keyframes {
      0% {
        opacity: 0;
        animation-timing-function: linear;
      }
      50% {
        opacity: 0;
        animation-timing-function: linear;
      }
      100% {
        opacity: 1;
        animation-timing-function: linear;
      }
    }
    .htmlNoPages .gwd-gen-18xbgwdanimation {
      animation: gwd-gen-18xbgwdanimation_gwd-keyframes 1s linear 0s 1 normal forwards running;
    }
    @keyframes gwd-gen-1kp1gwdanimation_gwd-keyframes {
      0% {
        opacity: 0;
        animation-timing-function: linear;
      }
      50% {
        opacity: 0;
        animation-timing-function: linear;
      }
      100% {
        opacity: 1;
        animation-timing-function: linear;
      }
    }
    .htmlNoPages .gwd-gen-1kp1gwdanimation {
      animation: gwd-gen-1kp1gwdanimation_gwd-keyframes 1s linear 0s 1 normal forwards running;
    }
  </style>
  <link href="https://fonts.googleapis.com/css?family=Quicksand:300,regular,500,700|Lobster:regular|Dancing+Script:regular,700|Great+Vibes:regular|Libre+Baskerville:regular,italic,700" rel="stylesheet" type="text/css">
  <script type="text/javascript" gwd-events="handlers">
    window.gwd = window.gwd || {};
    gwd.click = function(event) { < a href = "www.google.com" > academics < /a>};
  </script>
</head>

<body class="htmlNoPages">
  <img src="staff-bg.jpg" id="staff-bg" class="gwd-img-1qtk gwd-gen-fzeigwdanimation">
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx gwd-gen-i37vgwdanimation" id="R1"></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77 gwd-gen-16slgwdanimation">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation gwd-gen-19c4gwdanimation" id="n1">Staff Portal</p>
  <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-bqs7 gwd-gen-kctogwdanimation" id="2"><a href="Staff-Admin-DelUser.php">Delete user</a>
  </p>
  <p class="gwd-p-f3o9 gwd-p-ty1l gwd-p-1s9b gwd-gen-1ibrgwdanimation gwd-gen-1kp1gwdanimation" id="ele_1"><a href="Staff-Admin-AddUser.php">Add user</a>
  </p>
  <form method='POST'>
  <input type='Submit' id="button_1" class="gwd-button-1jw7 gwd-gen-18xbgwdanimation" name='sub' value='Logout' ><br>
  
  <p class="gwd-p-1hjf gwd-gen-1lqdgwdanimation" id="1"><?php echo $_SESSION['ID'];?></p>
</form>
</body>

</html>