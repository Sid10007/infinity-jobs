let tab = document.querySelectorAll('.navigation a');
for(let i = 0; i < tab.length; i++) {
	tab[i].addEventListener('click', swapTab);
}
function swapTab(event) {
	//console.log(event.target.innerHTML.toLowerCase());
	var tab = event.target.innerHTML.toLowerCase();
	//console.log(tab);
	try {	
		document.getElementById(tab).classList.remove("notselected");
		document.getElementById(tab).previousElementSibling.classList.add("notselected");
	}
	catch(err) {
		document.getElementById(tab).classList.remove("notselected");
		document.getElementById(tab).nextElementSibling.classList.add("notselected");	
	}
}