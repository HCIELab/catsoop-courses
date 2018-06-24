var notables = document.getElementById("page_content").querySelectorAll("h2, h3");
var scroller = document.getElementById("navvo");
console.log("RUNNING");
console.log(notables);
var title = document.getElementById("content").querySelector("h1");

var lefty = document.getElementById("left_chunk");
lefty.classList.remove("col-md-2");
lefty.classList.add("col-md-3");
var righty = document.getElementById("right_chunk");
righty.classList.remove("col-md-2");
righty.classList.add("col-md-1");

var new_li = document.createElement('li');
new_li.classList.add("side_title");
new_li.innerHTML = title.innerHTML;
scroller.appendChild(new_li);

for(var i = 0; i < notables.length; i++){
	if (notables[i].parentElement.id=="page_content"){
		var new_li = document.createElement('li');
        new_li.classList.add("nav-item");
		var new_a = document.createElement('a');
        new_a.classList.add("nav-link");
		new_a.innerHTML = "      " + notables[i].innerHTML;
		notables[i].id="page_anchor_"+String(i);
		new_a.href = "#"+notables[i].id;
		new_a.classList.add("tblinky");
		new_li.appendChild(new_a);
		scroller.appendChild(new_li);
		console.log("ADDING");
	}
}
