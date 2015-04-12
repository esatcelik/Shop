
function numb(e) {
    document.getElementById("dis").innerHTML = document.getElementById("dis").innerHTML + e.innerHTML;
}

function nclear() {
    document.getElementById("dis").innerHTML = "";
}

function calc() {
	var a = document.getElementById("dis").innerHTML;
	
	var b = a.split(/[+-/*]/) 
	fir = b[0];
	sec = b[1];
	
	a = eval(a);
	
	try {
    	d3.select("svg").remove(); 
	}
	catch(err) {}
	var yscale = d3.scale.linear()
    					.domain([Math.max(fir,sec,a), 0])
    					.range([0,255]);
	
	
	var axis = d3.svg.axis()
				.orient("left")
				.scale(yscale);
	
	var graph = d3.select(".graph")
				.append("svg")
				.attr("width",400)
				.attr("height",255);
	
	
	
	var bars = graph.selectAll("rect")
				.data([fir, sec, a])
				.enter()
					.append("rect")
					.attr("width",35)
					.attr("y",function(d){return yscale(d);})
					.attr("height", function(d) {return 255-yscale(d);})
					.attr("x", function(d,i) {return i*50;});
	
	graph.append("g")
		.attr("transform", "translate(245,10)")
		.call(axis);
    text0();
	document.getElementById("dis").innerHTML = a;
}

function text0() {
	document.getElementById("label0").innerHTML = "First &nbsp;&nbsp;Second  &nbsp;Result";
}
function chg(e) {
	
	return window.getComputedStyle(document.getElementById(e),null).backgroundColor;
}