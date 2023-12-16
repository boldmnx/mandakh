function updateClock(){
    var now = new Date();
    var dname = now.getDay(),
    mo= now.getMonth(),
    dnum=now.getDate(),
    yr=now.getFullYear(),
    hou=now.getMinutes(),
    sec=now.getSeconds(),
    pe="AM";
    if ( hou == 0){
        hou = 12;
    }
    if( hou >12){
        hou = hou - 12;
        pe = "PM";
    }
    
    var months=["1-р сар","2-р сар","3-р сар","4-р сар","5-р сар","6-р сар","7-р сар","8-р сар","9-р сарr","10-р сар","11-р сар","12-р сар"];
    var week=["Ням","Даваа","Мягмар","Лхагва","Пүрэв","Баасан","Бямба"];
    var ids=["dayname","month","daynum","year","hour","minutes","seconds","period"];
    var values=[week[dname],months[mo],dnum,yr,hou,sec,pe];
    for(var i=0;i<ids.length; i++)
    document.getElementById(ids[i]).firstChild.nodeValue = values[i];

}

function initClock(){
updateClock();
window.setInterval("updateClock()", 1)
}



function validate(){
    var username=document.getElementById("username").value;
    var password=document.getElementById("password").value;

if(username=="Mandakh" && password=="8989"){
    alert("Амжилттай нэвтэрлээ");
    return false;
}
else{
    alert("Нэвтэрэлт амжилтгүй")
}
}

