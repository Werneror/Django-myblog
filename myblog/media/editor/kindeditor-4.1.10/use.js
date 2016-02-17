var editor ;
KindEditor.ready(function(K) { 
    var options = {
        height : '400px', 
        filterMode : true,
		width: '90%'
   }; 
   editor = K.create('#id_content', options); 
});
