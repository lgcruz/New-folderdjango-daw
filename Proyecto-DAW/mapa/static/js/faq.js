// JavaScript source code
$(window).ready(function(){
	$(".pregunta").click(function(){
		$.getJSON("data/results.json", function(result){
			alert(result)
			var x=1
			
			
			
			$.each(result[0], function(i, field){
			//  $("div").append(field + " ");
				a = $("<div>"+field+"</div>")
				$("table").append(a.html()) 
				x++;
			});
		});
	});
});