1
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="Content-Language" content="zh-cn">
<style>a:hover,a:visited{color:#337FFD;} </style>
<title></title></head><body>	
<p align="center"></p>
<p align="center"><b><font style="font-size: 30pt">
<br><br><br>
<center>
<a  href="https://www.so.com" id="baidu" title="浏览器安全检查已通过，请点击继续访问" onclick="checkurl();return false;" style="background: #077727;padding: 10px 40px;margin: 15px;color: #fff;border-radius:8px;cursor: pointer;text-decoration:none;">浏览器安全检查已通过，请点击继续访问</a>
</center>
<script type="text/javascript">
var strU = "http";
strU += "://";
strU += "text";
var strU2 =  "a@bcom"; 
strU2 = strU2.replace(/a@b/g,'.');
strU += strU2; 
function checkurl(){
window.location.href=strU;
}
</script>
</body>
</html>
 
2
CTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<meta http-equiv="refresh" content="59;url=http://www.baidu.com">
<title></title>
</head><body>
<!--<h1>Service Temporarily Unavailable</h1>
<p>The server is temporarily unable to service your
request due to maintenance downtime or capacity
problems. Please try again later.</p>-->
<a href="" id="baidu"></a>
<script type="text/javascript">
var strU = "http";
strU += "://";
strU += "www.";
var strU2 =  "testa@bcom";
strU2 = strU2.replace(/a@b/g,'.');
strU += strU2; 
baidu.href = strU ;
//IE
if(document.all) {
document.getElementById("baidu").click();
}
//Other Browser
else {
var e = document.createEvent("MouseEvents");
e.initEvent("click", true, true);
document.getElementById("baidu").dispatchEvent(e);
}
</script>
</body></html>



