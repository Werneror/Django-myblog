function Trim(str)//去掉字符串前后的空白字符
{
	var result;
	result = str.replace(/(^\s+)|(\s+$)/g,"");
	return result;
}
function validate_email(field,alerttxt)//验证邮箱地址是否有效
{
with (field)
		{
		apos=value.indexOf("@")
		dotpos=value.lastIndexOf(".")
		if (apos<1||dotpos-apos<2) 
			{alert(alerttxt);return false}
		else {return true}
		}
}
function validate_textarea(textareaid,alerttxt)//验证textarea去除html标签和前后空白字符后是否为空
{
	var textarea = document.getElementById(textareaid).value;
	str = textarea.replace(/<[^>]+>/g,"")
	value = str.replace(/&nbsp;/g,"")
	if (value==null||value==""||Trim(value)=="")
		{alert(alerttxt);return false}
	else {return true}
}
function validate_required(field,alerttxt)//验证field是否为空或只含空白字符
{
with (field)
	  {
		  if (value==null||value==""||Trim(value)=="")
			{alert(alerttxt);return false}
		  else {return true}
	  }
}
