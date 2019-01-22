function validateForm(event) {
	let formName = event.target.parentElement.name;
	console.log(formName);
	if(formName == "signup") {	
		let companyname = document.forms[formName]["companyname"].value;
		let email = document.forms[formName]["email"].value;
		let companyid = document.forms[formName]["companyid"].value;
		let password = document.forms[formName]["password"].value; 
		if((companyname == "")||(companyid == "")||(email == "")||(password == "")) {
			alert("FILL ALL THE FIELDS!!");
			return false;
		}
		if(isNaN(companyid)) {
			alert("COMPANYID MUST BE A NUMBER!!");
			return false;
		}
		if(companyname.localeCompare(password) == 0) {
			alert("PASSWORD AND COMPANYNAME CAN'T BE SAME!!");
			return false;
		}
		if((email.split(".").length != 2)||(email.split("@").length != 2)) {
			alert("ENTER A VALID EMAIL!!");
			return false;
		}
	}
	else {
		let companyid = document.forms[formName]["companyid"].value;
		let password = document.forms[formName]["password"].value; 
		if((companyid == "")||(password = "")) {
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
			console.log("good to go");
			if(click == 'login') {
				console.log(event.target.parentElement);
				document.forms["login"].submit();
			}
			else {
				console.log(event.target.parentElement);
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
