<?php 
 $connect =mysqli_connect("localhost","root","","project1");
 $row['Name']="123";
 $row['dob']="123";
 $row['fid']="123";
 $row['deg']="123";
 $row['contact']="123";
 $row['mstatus']="123";
 $row['pwork']="123";
 if(!$connect)
 {
  echo mysqli_connect_error();
 }
 else
 {
  $sql="SELECT * FROM faculty_info where fid='".$_SESSION['ID']."' LIMIT 1";
  $qry=mysqli_query($connect,$sql);
  $row=mysqli_fetch_array($qry);
}
?>




















<!DOCTYPE html>
<html><head><meta name="GCD" content="YTk3ODQ3ZWZhN2I4NzZmMzBkNTEwYjJl81f9fd77f7b7d7d9da1d0c9f06c42669"/>
  <meta charset="utf-8">
  <title>A6</title>
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
.gwd-p-jy67 {
    font-size: 18px;
    height: 4.83%;
    position: absolute;
    width: 4.01%;
    transform-origin: 13.174px 9px 0px;
    -webkit-transform-origin: 13.174px 9px 0px;
    -moz-transform-origin: 13.174px 9px 0px;
    left: 34%;
    top: 21.45%;
}
.gwd-p-7nue {
    font-size: 18px;
    height: 4.83%;
    left: 34%;
    position: absolute;
    width: 17.72%;
    transform-origin: 17.9482px 9px 0px;
    -webkit-transform-origin: 17.9482px 9px 0px;
    -moz-transform-origin: 17.9482px 9px 0px;
    top: 32%;
}
.gwd-p-1dl9 {
    font-size: 18px;
    height: 4.83%;
    position: absolute;
    width: 21.88%;
    transform-origin: 53.4279px 9px 0px;
    -webkit-transform-origin: 53.4279px 9px 0px;
    -moz-transform-origin: 53.4279px 9px 0px;
    left: 34%;
    top: 43%;
}
.gwd-p-hz0d {
    font-size: 18px;
    height: 4.83%;
    left: 34%;
    position: absolute;
    width: 27.73%;
    transform-origin: 69.4823px 9px 0px;
    -webkit-transform-origin: 69.4823px 9px 0px;
    -moz-transform-origin: 69.4823px 9px 0px;
    top: 48%;
}
.gwd-p-eens {
    font-size: 18px;
    height: 4.83%;
    left: 34%;
    position: absolute;
    width: 30.05%;
    transform-origin: 83.8209px 9px 0px;
    -webkit-transform-origin: 83.8209px 9px 0px;
    -moz-transform-origin: 83.8209px 9px 0px;
    top: 53%;
}
.gwd-span-18d9 {
    display: block;
    font-size: 18px;
    height: 0%;
    position: absolute;
    width: 0%;
    left: 34%;
    top: 37.53%;
}
.gwd-span-1vhc {
    display: block;
    height: 10.4531px;
    left: 212px;
    position: absolute;
    top: 0px;
    width: 6px;
}
.gwd-p-649j {
    position: absolute;
    width: 40%;
    height: 5%;
    left: 48.07%;
    font-size: 18px;
    top: 21.45%;
}
.gwd-p-3oti {
    position: absolute;
    width: 40%;
    height: 5%;
    font-size: 18px;
    left: 48%;
    top: 32%;
}
.gwd-p-pu74 {
    position: absolute;
    width: 40%;
    height: 5%;
    font-size: 18px;
    left: 48%;
    top: 37.53%;
}
.gwd-p-1jri {
    position: absolute;
    width: 40%;
    height: 5%;
    font-size: 18px;
    left: 48%;
    top: 43%;
}
.gwd-p-f6da {
    position: absolute;
    height: 18.5%;
    width: 40%;
    font-size: 18px;
    left: 48%;
    top: 53%;
}
.gwd-p-1f0u {
    position: absolute;
    width: 0%;
    height: 0%;
    left: 48%;
    top: 48%;
}
.gwd-span-17bd {
    font-size: 18px;
}
.gwd-span-7983 {
    position: absolute;
    font-size: 18px;
    left: 34.05%;
    top: 26.81%;
    width: 40%;
    height: 5%;
}
.gwd-span-8u0t {
    position: absolute;
    font-size: 18px;
    left: 48.07%;
    top: 26.81%;
    width: 0%;
    height: 0%;
}</style>
  <link href="https://fonts.googleapis.com/css?family=Lobster:regular" rel="stylesheet" type="text/css">
</head>

<body class="htmlNoPages">
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx" id="R1"></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation" id="n1">Faculty Portal</p>
  <p class="gwd-p-jy67">Name:</p>
  <p class="gwd-p-7nue">Date of Birth:</p>
  <p class="gwd-p-1dl9 gwd-gen-19h9gwdanimation">Contact:</p>
  <p class="gwd-p-hz0d gwd-gen-1euigwdanimation">Martial Status:</p>
  <p class="gwd-p-eens gwd-gen-kit9gwdanimation">Previous Work:</p><span class="gwd-span-18d9">Degree:</span><span class="gwd-span-1vhc"><br></span>
  <p class="gwd-p-649j"><?php echo $row['name'];?></p>
  <p class="gwd-p-3oti"><?php echo $row['dob'];?></p>
  <p class="gwd-p-pu74"><?php echo $row['deg'];?></p>
  <p class="gwd-p-1jri"><?php echo $row['contact'];?></p>
  <p class="gwd-p-f6da"><?php echo $row['pwork'];?><br></p>
  <p class="gwd-p-1f0u"><span class="gwd-span-17bd"><?php echo $row['mstatus'];?></span><br>
    
  </p>
  <span class="gwd-span-7983">Faculty ID:</span><span class="gwd-span-8u0t"><?php echo $row['fid'];?></span>


</body></html>
