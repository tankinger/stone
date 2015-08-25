
function IsDigit(cCheck) 
{ 
return (('0'<=cCheck) && (cCheck<='9')); 
} 
function IsAlpha(cCheck) 
{ 
return ((('a'<=cCheck) && (cCheck<='z')) || (('A'<=cCheck) && (cCheck<='Z'))) 
} 
function IsValid() 
{ 
var struserName = reg.NewUserName.value; 
for (nIndex=0; nIndex<struserName.length; nIndex++) 
{ 
cCheck = struserName.charAt(nIndex); 
if (!(IsDigit(cCheck) || IsAlpha(cCheck))) 
{ 
return false; 
} 
} 
return true; 
} 


function IsValidDigit() 
{ 
var PhoneNumber = reg.PhoneNumber.value; 
for (nIndex=0; nIndex<PhoneNumber.length; nIndex++) 
{ 
cCheck = PhoneNumber.charAt(nIndex); 
if (!(IsDigit(cCheck))) 
{ 
return false; 
} 
} 
return true; 
}



function chkEmail(str) 
{ 
return str.search(/[\w\-]{1,}@[\w\-]{1,}\.[\w\-]{1,}/)==0?true:false 
} 
function docheck() 
{ 
if(reg.NewUserName.value=="") 
{ 
alert("请填写用户名"); 
return false; 
} 
else if(!IsValid()) 
{ 
alert("用户名只能使用字母和数字"); 
return false; 
} 
else if(reg.UserPassword.value=="") 
{ 
alert("请填写密码"); 
return false; 
} 
else if(reg.UserPassword.value != reg.CUserPassword.value) 
{ 
alert("两次密码不一致"); 
return false; 
} 
else if(!IsValidDigit() || reg.PhoneNumber.value=="") 
{ 
alert("请填写正确手机号"); 
return false; 
} 
else if(reg.UserType.value=="") 
{ 
alert("请填写用户的权限"); 
return false; 
} 

else if(reg.Email.value =="") 
{ 
alert("请填写邮箱"); 
return false; 
} 
else if(!chkEmail(reg.Email.value)) 
{ 
alert("请填写有效的Email地址"); 
return false; 
} 
else 
{ 
return true; 
} 
} 
