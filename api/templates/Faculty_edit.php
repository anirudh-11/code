<?php 
session_start();
 $connect =mysqli_connect("localhost","root","","project1");
 if(!$connect)
 {
  echo mysqli_connect_error();
 }
 else
 {
    if(isset($_POST[sub]))
    {
    $name=$_POST['name'];
    $dob=$_POST['dob'];
    $mstatus=$_POST['mstatus'];
    $pwork=$_POST['pwork'];
    $deg=$_POST['deg'];
    $contact=$_POST['contact'];
  $sql="INSERT INTO faculty_info( name,dob,mstatus,pwork,contact,deg,fid) VALUES('".$name."','".$dob."','".$mstatus."','".$pwork."','".$contact."','".$deg."','".$_SESSION['ID']."')";
  $qry=mysqli_query($connect,$sql);
  }
}
?>


<!DOCTYPE html>
<html><head><meta name="GCD" content="YTk3ODQ3ZWZhN2I4NzZmMzBkNTEwYjJl51b22225b09f4bdac37397982308ece2"/>
  <meta charset="utf-8">
  <title>A5</title>
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
    border-width: 0.988924px;
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
    opacity: 0.8;
    position: absolute;
    text-align: center;
    width: 45.58%;
    left: 27%;
    top: 3%;
}
.gwd-p-jy67 {
    font-size: 18px;
    height: 4.83%;
    position: absolute;
    width: 4.01%;
    transform-origin: 13.174px 9px 0px;
    -webkit-transform-origin: 13.174px 9px 0px;
    -moz-transform-origin: 13.174px 9px 0px;
    top: 31%;
    left: 34%;
}
.gwd-p-7nue {
    font-size: 18px;
    height: 4.83%;
    position: absolute;
    width: 17.72%;
    transform-origin: 17.9482px 9px 0px;
    -webkit-transform-origin: 17.9482px 9px 0px;
    -moz-transform-origin: 17.9482px 9px 0px;
    top: 37%;
    left: 34%;
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
    top: 47.18%;
}
.gwd-p-hz0d {
    font-size: 18px;
    height: 4.83%;
    position: absolute;
    width: 27.73%;
    transform-origin: 69.4823px 9px 0px;
    -webkit-transform-origin: 69.4823px 9px 0px;
    -moz-transform-origin: 69.4823px 9px 0px;
    top: 53%;
    left: 34%;
}
.gwd-p-eens {
    font-size: 18px;
    height: 4.83%;
    position: absolute;
    width: 30.05%;
    transform-origin: 83.8209px 9px 0px;
    -webkit-transform-origin: 83.8209px 9px 0px;
    -moz-transform-origin: 83.8209px 9px 0px;
    top: 59%;
    left: 34%;
}
.gwd-span-18d9 {
    display: block;
    font-size: 18px;
    height: 0%;
    position: absolute;
    width: 0%;
    top: 42%;
    left: 34%;
}
.gwd-span-1vhc {
    display: block;
    height: 10.4628px;
    left: 212px;
    position: absolute;
    top: 0px;
    width: 6.01266px;
}
.gwd-input-nfm1 {
    border-width: 1.99763px;
    display: block;
    height: 2.95%;
    left: 40%;
    position: absolute;
    top: 48.26%;
    width: 15.41%;
    transform-origin: 38px 48px 0px;
    -webkit-transform-origin: 38px 48px 0px;
    -moz-transform-origin: 38px 48px 0px;
}
.gwd-input-1klb {
    border-width: 1.99763px;
    display: block;
    height: 2.95%;
    left: 54%;
    position: absolute;
    top: 75.87%;
    width: 15.41%;
    transform-origin: 38px 48px 0px;
    -webkit-transform-origin: 38px 48px 0px;
    -moz-transform-origin: 38px 48px 0px;
}
.gwd-input-rum2 {
    border-width: 1.99763px;
    display: block;
    height: 2.95%;
    left: 40%;
    position: absolute;
    top: 75.87%;
    width: 15.41%;
    transform-origin: 38px 48px 0px;
    -webkit-transform-origin: 38px 48px 0px;
    -moz-transform-origin: 38px 48px 0px;
}
.gwd-input-1a8q {
    border-width: 1.99763px;
    display: block;
    height: 2.95%;
    left: 40%;
    position: absolute;
    top: 101.88%;
    width: 15.41%;
    transform-origin: 38px 48px 0px;
    -webkit-transform-origin: 38px 48px 0px;
    -moz-transform-origin: 38px 48px 0px;
}
.gwd-input-1l8t {
    border-width: 1.99763px;
    display: block;
    height: 2.95%;
    left: 40%;
    position: absolute;
    top: 80.43%;
    width: 15.41%;
    transform-origin: 38px 48px 0px;
    -webkit-transform-origin: 38px 48px 0px;
    -moz-transform-origin: 38px 48px 0px;
}
.gwd-input-11fu {
    border-width: 1.99763px;
    display: block;
    height: 2.95%;
    position: absolute;
    top: 112.87%;
    width: 15.41%;
    transform-origin: 38px 48px 0px;
    -webkit-transform-origin: 38px 48px 0px;
    -moz-transform-origin: 38px 48px 0px;
    left: 48%;
}
.gwd-input-izy1 {
    border-width: 1.99763px;
    display: block;
    height: 2.95%;
    position: absolute;
    width: 15.41%;
    transform-origin: 38px 48px 0px;
    -webkit-transform-origin: 38px 48px 0px;
    -moz-transform-origin: 38px 48px 0px;
    top: 31%;
    left: 48%;
}
.gwd-input-1dmm {
    border-width: 1.99763px;
    display: block;
    height: 2.95%;
    position: absolute;
    width: 15.41%;
    transform-origin: 38px 48px 0px;
    -webkit-transform-origin: 38px 48px 0px;
    -moz-transform-origin: 38px 48px 0px;
    top: 37%;
    left: 48%;
}
.gwd-input-1jp9 {
    border-width: 1.99763px;
    display: block;
    height: 10.19%;
    left: 40%;
    position: absolute;
    top: 34.58%;
    width: 45.15%;
    transform-origin: 108.519px 124.235px 0px;
    -webkit-transform-origin: 108.519px 124.235px 0px;
    -moz-transform-origin: 108.519px 124.235px 0px;
}
.gwd-input-12z0 {
    border-width: 1.99763px;
    display: block;
    height: 10.19%;
    left: 40%;
    position: absolute;
    top: 58.98%;
    width: 45.15%;
    transform-origin: 108.519px 124.235px 0px;
    -webkit-transform-origin: 108.519px 124.235px 0px;
    -moz-transform-origin: 108.519px 124.235px 0px;
}
.gwd-input-m94g {
    border-width: 1.99763px;
    display: block;
    height: 10.19%;
    position: absolute;
    width: 45.15%;
    transform-origin: 108.519px 124.235px 0px;
    -webkit-transform-origin: 108.519px 124.235px 0px;
    -moz-transform-origin: 108.519px 124.235px 0px;
    left: 48%;
    top: 59%;
}
.gwd-input-6xp1 {
    top: 42%;
}
.gwd-input-1hlb {
    left: 48%;
    top: 47%;
}
.gwd-p-5nxj {
    position: absolute;
    transform-origin: 206.155px 63.2236px 0px;
    -webkit-transform-origin: 206.155px 63.2236px 0px;
    -moz-transform-origin: 206.155px 63.2236px 0px;
    width: 21.11%;
    height: 6.17%;
    left: 45%;
    top: 19%;
}
.gwd-span-oesz {
    font-size: 24px;
    font-family: Tahoma;
}
.gwd-select-16gn {
    position: absolute;
    left: 48%;
    top: 51.56%;
    width: 15.41%;
    height: 6.43%;
}
.gwd-button-f5s4 {
    position: absolute;
    left: 47.77%;
    top: 73.46%;
    width: 16%;
    height: 5%;
}</style>
  <link href="https://fonts.googleapis.com/css?family=Lobster:regular" rel="stylesheet" type="text/css">
</head>

<body class="htmlNoPages">
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx" id="R1"></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation gwd-gen-rs38gwdanimation" id="n1">Faculty Portal</p>
  <p class="gwd-p-jy67 gwd-gen-18g2gwdanimation">Name:</p>
  <p class="gwd-p-7nue gwd-gen-30legwdanimation">Date of Birth:</p>
  <p class="gwd-p-1dl9 gwd-gen-19h9gwdanimation gwd-gen-1rxegwdanimation">Contact:</p>
  <p class="gwd-p-hz0d gwd-gen-1euigwdanimation gwd-gen-poclgwdanimation">Martial Status:</p>
  <p class="gwd-p-eens gwd-gen-kit9gwdanimation gwd-gen-125tgwdanimation">Previous Work:</p><span class="gwd-span-18d9 gwd-gen-nuxlgwdanimation">Degree:</span><span class="gwd-span-1vhc"><br></span>
  <form method="POST">
  <input type="text" id="text_1" class="gwd-input-nfm1 gwd-input-1klb gwd-input-rum2 gwd-input-e7iq gwd-gen-1wdogwdanimation gwd-input-1hlb gwd-gen-14p0gwdanimation" name='contact'>
  <input type="text" id="text_10" class="gwd-input-nfm1 gwd-input-1klb gwd-input-rum2 gwd-input-1a8q gwd-input-1l8t gwd-input-11fu gwd-input-1e4u gwd-gen-jly0gwdanimation gwd-input-6xp1 gwd-gen-1a7ygwdanimation" name='deg'>
  <input type="text" id="text_4" class="gwd-input-nfm1 gwd-input-1klb gwd-input-izy1 gwd-gen-1b60gwdanimation" name='name'>
  <input type="text" id="text_3" class="gwd-input-nfm1 gwd-input-1klb gwd-input-1dmm gwd-gen-7k8ngwdanimation" name='dob'>
  <input type="text" id="text_11" class="gwd-input-nfm1 gwd-input-1klb gwd-input-1jp9 gwd-input-12z0 gwd-input-m94g gwd-gen-1jbqgwdanimation gwd-gen-1ndugwdanimation"name = 'pwork'>
  <p class="gwd-p-5nxj gwd-gen-o6fwgwdanimation"><span class="gwd-span-oesz">Edit Form</span><br>
    
  </p>
  <select id="select_1" class="gwd-select-16gn" data-gwd-name="Status" name='mstatus'>
    <option value="Married">Married</option>
    <option value="Single">Single</option>
    <option value="0" selected="">Select</option>
  </select>
  <input type="Submit" id="button_3" class="gwd-button-f5s4 gwd-gen-ysnygwdanimation" name='sub'>Save Changes</br>
</form>

</body></html>
