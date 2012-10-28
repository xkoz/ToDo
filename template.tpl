<!DOCTYPE html>
<html>
<head>
	<title>Hello!</title>
</head>
<body>
<div style="width:80%; margin:0 auto;">
<p>Tasks: <b>{{count}}</b>.</p>
<form action="\add" method="POST" name="add_form">
	<textarea rows="2" cols="50" name="task"></textarea></br>
	<input type="submit" value="Send" />
</form>
<p>
<form action="\delete" method="POST" name="delete_form">
Current tasks
	%for task in tasks:
	    <div style="margin-top:5px;">
			<input type="checkbox" name="id_task" value="{{task['_id']}}"/>{{task['task']}}<br />
			<i>{{task['date']}}</i>
		</div>
	%end
</form>
</p>
</div>
</body>
</html>