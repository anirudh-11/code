<?php 
 session_start();
 $connect =mysqli_connect("localhost","root","","project1");
 $row['Name']="123";
 $row['Address']="123";
 $row['DOB']="123";
 $row['Rollno']="123";
 $row['Email']="123";
 $row['Phoneno']="123";
 $row['Fathername']="123";
 $row['Fatherocc']="123";
 $row['Fatherph']="123";
 $row['Fatheremail']="123";
 $row['Mothersname']="123";
 $row['Mothersocc']="123";
 $row['Motherph']="123";
 $row['Motheremail']="123";
 $row['Interest']="123";
 $row['Sports']="123";
 $row['Exc']="123";
 $n='123';
 if(!$connect)
 {
  echo mysqli_connect_error();
 }
else if(isset($_POST['sub']))
{
    // $sql1="INSERT INTO meta_pinfo(Name,Address,DOB,Email,Phoneno,Fathername,Fatherocc,Fatherph,Fatheremail,Mothersname,Mothersocc,Motherph,Motheremail,Interest,Sports,Exc) VALUES ('".$row['Name']."','".$row['Address']."','".$row['DOB']."','".$row['Rollno']."','".$row['Email']."','".$row['Phoneno']."','".$row['Fathername']."','".$row['Fatherocc']."','".$row['Fatherph']."','".$row['Fatheremail']."','".$row['Mothersname']."','".$row['Mothersocc']."','".$row['Motherph']."','".$row['Motheremail']."','".$row['Interest']."','".$row['Sports']."','".$row['Exc']."',)";
// $sqq="INSERT INTO meta_pinfo VALUES('123','123','123','123','123','123','123','123','123','123','123','123','123','123','123','123','123')";
$sql="INSERT INTO meta_pinfo VALUES('".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."','".$n."')";

   $qry=mysqli_query($connect,$sql);
}
?>
<html><head><meta name="GCD" content="YTk3ODQ3ZWZhN2I4NzZmMzBkNTEwYjJl06d9e13a096c9bf289275626e366dd3b"/>
  <meta charset="utf-8">
  <title>A4</title>
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
    border-width: 1px;
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
    left: 28.4%;
    opacity: 0.8;
    position: absolute;
    text-align: center;
    top: 2.81%;
    width: 45.58%;
}
.gwd-p-jy67 {
    font-size: 18px;
    height: 4.83%;
    left: 26%;
    position: absolute;
    width: 4.01%;
    transform-origin: 13.174px 9px 0px;
    -webkit-transform-origin: 13.174px 9px 0px;
    -moz-transform-origin: 13.174px 9px 0px;
    top: 20.64%;
}
.gwd-p-7nue {
    font-size: 18px;
    height: 4.83%;
    left: 26%;
    position: absolute;
    width: 17.72%;
    transform-origin: 17.9482px 9px 0px;
    -webkit-transform-origin: 17.9482px 9px 0px;
    -moz-transform-origin: 17.9482px 9px 0px;
    top: 26.81%;
}
.gwd-p-19st {
    font-size: 18px;
    height: 4.83%;
    left: 26%;
    position: absolute;
    width: 8.08%;
    top: 34.05%;
}
.gwd-p-11p5 {
    font-size: 18px;
    height: 4.83%;
    left: 26%;
    position: absolute;
    top: 48.26%;
    width: 20.03%;
    transform-origin: 24.1796px 9px 0px;
    -webkit-transform-origin: 24.1796px 9px 0px;
    -moz-transform-origin: 24.1796px 9px 0px;
}
.gwd-p-1dl9 {
    font-size: 18px;
    height: 4.83%;
    left: 26%;
    position: absolute;
    top: 75.07%;
    width: 21.88%;
    transform-origin: 53.4279px 9px 0px;
    -webkit-transform-origin: 53.4279px 9px 0px;
    -moz-transform-origin: 53.4279px 9px 0px;
}
.gwd-p-137k {
    font-size: 18px;
    height: 4.83%;
    left: 26%;
    position: absolute;
    top: 53.62%;
    width: 24.96%;
    transform-origin: 29.5698px 9px 0px;
    -webkit-transform-origin: 29.5698px 9px 0px;
    -moz-transform-origin: 29.5698px 9px 0px;
}
.gwd-p-hz0d {
    font-size: 18px;
    height: 4.83%;
    left: 26%;
    position: absolute;
    top: 80.43%;
    width: 27.73%;
    transform-origin: 69.4823px 9px 0px;
    -webkit-transform-origin: 69.4823px 9px 0px;
    -moz-transform-origin: 69.4823px 9px 0px;
}
.gwd-span-1op0 {
    display: block;
    font-size: 18px;
    height: 4.83%;
    left: 26%;
    position: absolute;
    width: 30.05%;
    transform-origin: 37.0432px 9px 0px;
    -webkit-transform-origin: 37.0432px 9px 0px;
    -moz-transform-origin: 37.0432px 9px 0px;
    top: 58.98%;
}
.gwd-p-eens {
    font-size: 18px;
    height: 4.83%;
    left: 26%;
    position: absolute;
    top: 85.79%;
    width: 30.05%;
    transform-origin: 83.8209px 9px 0px;
    -webkit-transform-origin: 83.8209px 9px 0px;
    -moz-transform-origin: 83.8209px 9px 0px;
}
.gwd-span-gtcu {
    display: block;
    height: 4.56%;
    left: 26.04%;
    position: absolute;
    top: 101.88%;
    width: 21.88%;
    transform-origin: 13.1719px 8.67228px 0px;
    -webkit-transform-origin: 13.1719px 8.67228px 0px;
    -moz-transform-origin: 13.1719px 8.67228px 0px;
}
.gwd-span-8liv {
    font-size: 18px;
}
.gwd-span-1ire {
    display: block;
    font-size: 18px;
    height: 0%;
    left: 26%;
    position: absolute;
    top: 107.24%;
    width: 0%;
}
.gwd-span-18d9 {
    display: block;
    font-size: 18px;
    height: 0%;
    left: 26%;
    position: absolute;
    top: 112.6%;
    width: 0%;
}
.gwd-span-1vhc {
    display: block;
    height: 10.4688px;
    left: 212px;
    position: absolute;
    top: 0px;
    width: 6.03125px;
}
.gwd-input-nfm1 {
    position: absolute;
    width: 100px;
    height: 20px;
    transform-origin: 41px 23px 0px;
    -webkit-transform-origin: 41px 23px 0px;
    -moz-transform-origin: 41px 23px 0px;
    left: 227px;
    top: 74px;
}
.gwd-input-1klb {
    height: 11px;
    transform-origin: 38px 48px 0px;
    -webkit-transform-origin: 38px 48px 0px;
    -moz-transform-origin: 38px 48px 0px;
    left: 218px;
    top: 77px;
}
.gwd-input-rum2 {
    left: 280px;
    top: 180px;
}
.gwd-input-1jp9 {
    width: 293px;
    height: 38px;
    transform-origin: 108.519px 124.235px 0px;
    -webkit-transform-origin: 108.519px 124.235px 0px;
    -moz-transform-origin: 108.519px 124.235px 0px;
    left: 240px;
    top: 129px;
}
.gwd-input-1dmm {
    top: 27.61%;
    width: 15.41%;
    height: 2.95%;
    left: 40%;
}
.gwd-input-izy1 {
    top: 20.64%;
    width: 15.41%;
    height: 2.95%;
    left: 40%;
}
.gwd-input-19lk {
    top: 52.82%;
    width: 15.41%;
    height: 2.95%;
    left: 40%;
}
.gwd-input-12z0 {
    left: 352px;
    top: 220px;
}
.gwd-input-1a8q {
    left: 285px;
    top: 281px;
}
.gwd-input-1l8t {
    top: 283px;
}
.gwd-input-11fu {
    left: 335px;
    top: 300px;
}
.gwd-input-m94g {
    top: 86.06%;
    width: 45.15%;
    height: 10.19%;
    left: 40%;
}
.gwd-input-b96d {
    top: 101.88%;
    width: 15.41%;
    height: 2.95%;
    left: 40%;
}
.gwd-input-1j3v {
    left: 248px;
    top: 397px;
}
.gwd-input-11as {
    top: 112.87%;
    width: 15.41%;
    height: 2.95%;
    left: 40%;
}
.gwd-input-e7iq {
    top: 48.26%;
    width: 15.41%;
    height: 2.95%;
    left: 40%;
}
.gwd-input-v71y {
    top: 75.87%;
    width: 15.41%;
    height: 2.95%;
    left: 40%;
}
.gwd-input-1e4u {
    top: 80.43%;
    width: 15.41%;
    height: 2.95%;
    left: 40%;
}
.gwd-input-xw6g {
    top: 106.43%;
    width: 15.41%;
    height: 2.95%;
    left: 40%;
}
.gwd-input-wm69 {
    width: 45.15%;
    height: 10.19%;
    top: 34.58%;
    left: 40%;
}
.gwd-input-1rl7 {
    top: 58.98%;
    width: 45.15%;
    height: 10.19%;
    left: 40%;
}
.gwd-button-f5s4 {
    border-width: 2px;
    display: block;
    height: 5%;
    position: absolute;
    width: 16%;
    left: 40%;
    top: 123%;
}</style>
  <link href="https://fonts.googleapis.com/css?family=Lobster:regular" rel="stylesheet" type="text/css">
</head>

<body class="htmlNoPages">
  <svg data-gwd-shape="rectangle" class="gwd-rect-13rx" id="R1"></svg>
  <img src="logo.png" id="logo" class="gwd-img-kj77">
  <p class="gwd-p-6368 gwd-gen-1uk8gwdanimation text-tool-feedback" id="n1">Student Portal</p>
  <p class="gwd-p-jy67 text-tool-feedback">Name:</p>
  <p class="gwd-p-7nue text-tool-feedback">Date of Birth:</p>
  <p class="gwd-p-19st text-tool-feedback">Contact:</p>
  <p class="gwd-p-11p5 text-tool-feedback">Father's Name:</p>
  <p class="gwd-p-1dl9 gwd-gen-19h9gwdanimation">Mother's Name:</p>
  <p class="gwd-p-137k text-tool-feedback">Father's Occupation:</p>
  <p class="gwd-p-hz0d gwd-gen-1euigwdanimation">Mother's Occupation:</p><span class="gwd-span-1op0 text-tool-feedback">Previous&nbsp;</span>
  <p class="gwd-p-eens gwd-gen-kit9gwdanimation">Mother's Parents Phoneno:</p><span class="gwd-span-gtcu"><span class="gwd-span-8liv">Year:</span><br>
  
  </span><span class="gwd-span-1ire">Interests:</span><span class="gwd-span-18d9">Goals:</span><span class="gwd-span-1vhc text-tool-feedback"><br></span>
  <form method='POST'>
  <input type="text" id="text_1" class="gwd-input-nfm1 gwd-input-1klb gwd-input-rum2 gwd-input-e7iq gwd-gen-1wdogwdanimation" name='fname'>
  <input type="text" id="text_8" class="gwd-input-nfm1 gwd-input-1klb gwd-input-rum2 gwd-input-1a8q gwd-input-1l8t gwd-input-v71y gwd-gen-dlzegwdanimation" name='mname'>
  <input type="text" id="text_12" class="gwd-input-nfm1 gwd-input-1klb gwd-input-rum2 gwd-input-1a8q gwd-input-1l8t gwd-input-b96d gwd-gen-u2z9gwdanimation" name='sports'>
  <input type="text" id="text_10" class="gwd-input-nfm1 gwd-input-1klb gwd-input-rum2 gwd-input-1a8q gwd-input-1l8t gwd-input-11fu gwd-input-1e4u gwd-gen-jly0gwdanimation" name='mocc'>
  <input type="text" id="text_13" class="gwd-input-nfm1 gwd-input-1klb gwd-input-rum2 gwd-input-1a8q gwd-input-1l8t gwd-input-11fu gwd-input-1j3v gwd-input-11as gwd-gen-r9osgwdanimation" name='goal'>
  <input type="text" id="text_14" class="gwd-input-nfm1 gwd-input-1klb gwd-input-rum2 gwd-input-1a8q gwd-input-1l8t gwd-input-11fu gwd-input-1j3v gwd-input-xw6g gwd-gen-1szbgwdanimation" name='inter'>
  <input type="text" id="text_5" class="gwd-input-nfm1 gwd-input-1klb gwd-input-19lk gwd-gen-3hg8gwdanimation" name='focc'>
  <input type="text" id="text_4" class="gwd-input-nfm1 gwd-input-1klb gwd-input-izy1 gwd-gen-1xzxgwdanimation" name='name1'>
  <input type="text" id="text_3" class="gwd-input-nfm1 gwd-input-1klb gwd-input-1dmm gwd-gen-27tygwdanimation" name='dob'>
  <input type="text" id="text_2" class="gwd-input-nfm1 gwd-input-1klb gwd-input-1jp9 gwd-input-wm69 gwd-gen-11yrgwdanimation" name='con'>
  <input type="text" id="text_6" class="gwd-input-nfm1 gwd-input-1klb gwd-input-1jp9 gwd-input-12z0 gwd-input-1rl7 gwd-gen-jqh1gwdanimation"name='parentemail'>
  <input type="text" id="text_11" class="gwd-input-nfm1 gwd-input-1klb gwd-input-1jp9 gwd-input-12z0 gwd-input-m94g gwd-gen-1jbqgwdanimation" name='parentphone'>
  <input type='Submit' id="button_3" class="gwd-button-f5s4 gwd-gen-ysnygwdanimation" name='sub' value='Save Changes'><br>
</form>

</body></html>
