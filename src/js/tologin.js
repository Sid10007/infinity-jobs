function detect(event) {
	//console.log(event.target.innerHTML.toLowerCase());
	let fname = "login" + event.target.innerHTML.toLowerCase() + ".html";
	event.target.href = fname;
};

let button = document.getElementsByClassName('button');
for (var i = 0; i < button.length; i++) {
	//console.log(x);
	button[i].addEventListener('click', detect);
}
