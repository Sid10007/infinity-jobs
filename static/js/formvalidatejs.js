function validateForm(event) {
	let formName = event.target.parentElement.name;
	console.log(formName);
	if(formName == "signup") {	
		let username = document.forms[formName]["username"].value;
		let email = document.forms[formName]["email"].value;
		let userid = document.forms[formName]["userid"].value;
		let password = document.forms[formName]["password"].value; 
		if((username == "")||(userid == "")||(email == "")||(password == "")) {
			alert("FILL ALL THE FIELDS!!");
			return false;
		}
		if(isNaN(userid)) {
			alert("USERID MUST BE A NUMBER!!");
			return false;
		}
		if(username.localeCompare(password) == 0) {
			alert("PASSWORD AND USERNAME CAN'T BE SAME!!");
			return false;
		}
		if((email.split(".").length != 2)||(email.split("@").length != 2)) {
			alert("ENTER A VALID EMAIL!!");
			return false;
		}
	}
	else {
		let userid = document.forms[formName]["userid"].value;
		let password = document.forms[formName]["password"].value; 
		if((userid == "")||(password = "")) {
			alert("FILL ALL THE FIELDS!!");
			return false;
		}	
	}
	return true;
}

function detect(event) {
	let click = event.target.innerHTML.toLowerCase();
	//console.log(click);
	if(click == 'reset') {
		event.target.parentElement.reset();
		return false;
	}
	else {
		if(validateForm(event)) {
			if(click == 'login') {
				console.log(event.target.parentElement);
				document.forms["login"].submit();
			}
			else {
				//console.log(event.target.parentElement);
				console.log(document.forms["signup"]);
				document.forms["signup"].submit();
			}
		}
	}
};

let button = document.getElementsByClassName('button');
for (var i = 0; i < button.length; i++) {
	//console.log(x);
	button[i].addEventListener('click', detect);
}
