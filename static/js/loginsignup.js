let tab = document.querySelectorAll('.loginform a');
for(let i = 0; i < tab.length; i++) {
	tab[i].addEventListener('click', swapTab);
}

function swapTab(event) {
	//console.log(event.target.innerHTML.toLowerCase());
	var tab1 = event.target.innerHTML.toLowerCase().split(" ");
	var tab = '';
	for(let i = 0; i < tab1.length; i++) {
		tab += tab1[i];
	}
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