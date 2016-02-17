//点击id为link_id的元素可以隐藏或显示id为第二个参数的元素
function display_table(link_id,id){ 
	var link_id = document.getElementById(link_id); 
	var id = document.getElementById(id); 
	if(id.style.display=='none'){ 
		id.style.display =""; 
		link_id.innerHTML = "隐藏"; 
	}else{ 
		id.style.display ="none"; 
		link_id.innerHTML = "回复"; 
	} 
}
//实现iframe自适应高度后隐藏，此函数的隐藏功能对某些手机无效 
function dyniframesize(down) {
	var pTar = null;
	if (document.getElementById){
		pTar = document.getElementById(down);
	}
	else{
		eval('pTar = ' + down + ';');
	}
	if (pTar && !window.opera){
		//begin resizing iframe
		pTar.style.display="block"
		if (pTar.contentDocument && pTar.contentDocument.body.offsetHeight){
			//ns6 syntax
			pTar.height = pTar.contentDocument.body.offsetHeight +30;
			pTar.width = pTar.contentDocument.body.scrollWidth+30;
		}
		else if (pTar.Document && pTar.Document.body.scrollHeight){
			//ie5+ syntax
			pTar.height = pTar.Document.body.scrollHeight;
			pTar.width = pTar.Document.body.scrollWidth;
		}
	}
	pTar.style="display:none";
} 
