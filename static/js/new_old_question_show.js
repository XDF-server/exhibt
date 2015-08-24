$(function(){

	$('button[name=mark_btn]').on('click', function () {

		var mark = $(this).attr("id")
		var oldid = $("div#q_old_id").text()
		var newid = $("div#q_new_id").text()
		var this_btn = $(this)

		$.ajax({
			type : "post",
			url : "/mark",
			data:{"mark" : mark,"oldid" : oldid,"newid" : newid},
			success:function(msg){
				if (msg == 'ok'){

    					this_btn.button('loading');
				}
				else{
					this_btn.button('reset');
				}
			}
		});
	});

	$('button#add_mark').on('click',function() {
		
		var name = $("input#mark_data").val()
		var oldid = $("div#q_old_id").text()

		$.ajax({
			type : "post",
			url : "/addmark",
			data:{"name" : name,"oldid" : oldid},
			success:function(msg){
				if (msg == 'ok'){
					alert('添加成功');
				}
				else{
					alert('添加失败');
				}
			}
		});

	});
	
	$('button#pass').on('click',function() {
		var this_btn = $(this);
		var oldid = $("div#q_old_id").text()
		var newid = $("div#q_new_id").text()

		$.ajax({
			type : "post",
			url : "/verify",
			data: {"oldid":oldid,"newid":newid,"verify":0},
			success:function(msg){
				if (msg == 'ok'){
					this_btn.button("loading");
					$("#no").button("loading");
				}
				else{
					this_btn.button("reset");
					$("#no").button("reset");

				}
			}
		});

	});

	$('button#no').on('click',function() {
		var this_btn = $(this);
		var oldid = $("div#q_old_id").text()
		var newid = $("div#q_new_id").text()

		$.ajax({
			type : "post",
			url : "/verify",
			data: {"oldid":oldid,"newid":newid,"verify":1},
			success:function(msg){
				if (msg == 'ok'){
					this_btn.button("loading");
					$("#pass").button("loading");
				}
				else{
					this_btn.button("reset");
					$("#no").button("reset");

				}
			}
		});

	});

});
