function plot(planet)
{
	var nameText = "Planet name is ";
	d3.select("body").append("p")
						.text(nameText)
						.append()
						.text(planet.name)

	//console.log(planet)
	d3.select("body").append("br")
	var svgWidth = 300;
	var svgHeight = 300;
	var sunCX = svgWidth/2;
	var sunCY = svgHeight/2;
	var sunR = 3;


	var svgElement = d3.select("body").append("svg")
								.attr("width", svgWidth)
								.attr("height", svgHeight)
								.style("border", "1px solid black");

	var Sun = svgElement.append("circle")
						.attr("cx", sunCX)
						.attr("cy", sunCY)
						.attr("r", sunR)
						.style("fill", "orange")
	
}